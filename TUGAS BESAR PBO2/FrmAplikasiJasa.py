import tkinter as tk
import json
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import Frame, Label, Entry, Button, ttk, YES, BOTH, END, StringVar, W
from Users import *
from Pemesanan import *
from Mekanik import *

class FrmLogin:
    def __init__(self):
        self.login_form = tk.Tk()
        self.login_form.geometry("300x250")
        self.login_form.title("Form Login")
        self.login_form.state('zoomed')  # Menampilkan form dengan zoomed

        # Judul
        lbl_title = tk.Label(self.login_form, text="Silahkan Login Terlebih Dahulu", font=("Arial", 20))
        lbl_title.pack(pady=10)

        self.lbl_username = tk.Label(self.login_form, text="Username:", font=("Arial", 12))
        self.lbl_username.pack()
        self.entry_username = tk.Entry(self.login_form, font=("Arial", 12))
        self.entry_username.pack()

        self.lbl_password = tk.Label(self.login_form, text="Password:", font=("Arial", 12))
        self.lbl_password.pack()
        self.entry_password = tk.Entry(self.login_form, show="*", font=("Arial", 12))
        self.entry_password.pack()

        self.btn_login = tk.Button(self.login_form, text="Login", command=self.login, font=("Arial", 12), bg="green",
                                   fg="white")
        self.btn_login.pack(pady=10)

        self.btn_register = tk.Button(self.login_form, text="Registrasi", command=self.open_register_form, font=("Arial", 12),
                                      bg="blue", fg="white")
        self.btn_register.pack()


    def login(self):
        u = self.entry_username.get()
        p = self.entry_password.get()
        A = Users()
        A.username = u
        A.passwd = p
        status, msg, user_id = A.login()

        print("Status:", status)
        print("Message:", msg)

        if status == "success":
            print("Login successful, user type:", msg["message"])  # Extract "message" field from msg
            if msg["message"] == "admin":
                self.login_form.withdraw()  # Hide the login form
                menu_form = MenuFormAdmin()
            elif msg["message"] == "pelanggan":
                print("Opening MenuFormPelanggan with username:", u)
                self.login_form.withdraw()  # Hide the login form
                menu_form = MenuFormPelanggan(u)  # Pass the username to MenuFormPelanggan
            else:
                messagebox.showinfo("showinfo", "User Tidak Dikenal")
        else:
            messagebox.showerror("Error", "Login failed. Please check your username and password.")
        
    def open_register_form(self):
        self.login_form.withdraw()
        register_form = FrmRegister(self.login_form)

class FrmRegister:
    def __init__(self, login_form):
        self.register_form = tk.Toplevel(login_form)
        self.register_form.geometry("300x250")
        self.register_form.title("Form Registrasi")
        self.register_form.state('zoomed')  # Menampilkan form dengan zoomed

        # Judul
        lbl_title = tk.Label(self.register_form, text="Registrasi", font=("Arial", 20))
        lbl_title.pack(pady=10)

        self.lbl_username = tk.Label(self.register_form, text="Username:", font=("Arial", 12))
        self.lbl_username.pack()
        self.entry_username = tk.Entry(self.register_form, font=("Arial", 12))
        self.entry_username.pack()

        self.lbl_password = tk.Label(self.register_form, text="Password:", font=("Arial", 12))
        self.lbl_password.pack()
        self.entry_password = tk.Entry(self.register_form, show="*", font=("Arial", 12))
        self.entry_password.pack()

        self.btn_register = tk.Button(self.register_form, text="Registrasi", command=self.register, font=("Arial", 12),
                                      bg="blue", fg="white")
        self.btn_register.pack(pady=10)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Semua Data Harus Diisi!")
            return

        A = Users()
        A.username = username
        A.passwd = password

        # Check if the username already exists
        existing_user = A.get_by_username(username)
        if existing_user:
            messagebox.showinfo("Error", "Username sudah ada.")
            return

        A.rolename = "pelanggan"  # Set default role name to "pelanggan"

        res = A.simpan()
        data = json.loads(res)
        status = data["status"]
        if status == "success":
            messagebox.showinfo("Success", "Registrasi Berhasil.")
        else:
            messagebox.showinfo("Error", "Registrasi Gagal.")

        self.register_form.destroy()
        login_form = FrmLogin()
        
class MenuFormPelanggan:
    def __init__(self, username):
        self.username = username
        self.menu_form = tk.Tk()
        self.menu_form.geometry("300x250")
        self.menu_form.title("Dashboard")
        self.menu_form.state('zoomed')  # Menampilkan form dengan zoomed
        self.user_id = self.load_user_id_by_username()

        # Judul
        lbl_title = tk.Label(self.menu_form, text=f"Selamat Datang Di Dashboard, '{self.username}', ID: {self.user_id}", font=("Arial", 20))
        lbl_title.pack(pady=10)

        self.btn_pemesanan = tk.Button(self.menu_form, text="Pesan Jasa", command=self.open_pemesanan_form,
                                       font=("Arial", 12), bg="green", fg="white")
        self.btn_pemesanan.pack()

        self.btn_data = tk.Button(self.menu_form, text="Data Pesanan Anda", command=self.open_data_form, font=("Arial", 12),
                                  bg="blue", fg="white")
        self.btn_data.pack()

        self.btn_logout = tk.Button(self.menu_form, text="Logout", command=self.logout, font=("Arial", 12),
                                    bg="red", fg="white")
        self.btn_logout.pack(pady=10)

    def load_user_id_by_username(self):
        A = Users()
        user_data = A.get_by_username(self.username)
        if user_data:
            user_id = user_data.get("id")
            return user_id
        else:
            messagebox.showinfo("showinfo", "Failed to get User ID by username.")
            self.menu_form.destroy()
            
    def open_pemesanan_form(self):
        pemesanan_root = tk.Tk()
        pemesanan_form = FrmPemesananPelanggan(pemesanan_root, "Form Pemesanan", self.user_id)
        pemesanan_root.mainloop()
        self.menu_form.destroy()

    def open_data_form(self):
        data_root = tk.Tk()
        data_form = FrmDataPelanggan(data_root, "Data Pesanan", self.user_id)
        data_root.mainloop()
        self.menu_form.destroy()

    def logout(self):
        self.menu_form.destroy()
        login_form = FrmLogin()

class FrmPemesananPelanggan:
    def __init__(self, parent, title, user_id):
        self.parent = parent
        self.parent.geometry("600x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.parent.state('zoomed')  # Menampilkan form dengan zoomed
        self.user_id = user_id
        
        # Judul
        lbl_title = tk.Label(self.parent, text=f"Pesan Jasa", font=("Arial", 20))
        lbl_title.pack(pady=10)

        self.aturKomponen()
        self.onClear()
        self.load_data()  # Load the data when the form is initialized

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='TANGGAL:', font=("Arial", 12)).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        Label(mainFrame, text='NAMA:', font=("Arial", 12)).grid(row=1, column=0, sticky='w', padx=5, pady=5)
        Label(mainFrame, text='TELEPON:', font=("Arial", 12)).grid(row=2, column=0, sticky='w', padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:', font=("Arial", 12)).grid(row=3, column=0, sticky='w', padx=5, pady=5)
        Label(mainFrame, text='JENIS JASA:', font=("Arial", 12)).grid(row=4, column=0, sticky='w', padx=5, pady=5)
        Label(mainFrame, text="""\nMenentukan Jenis Jasa\n
              1. Pilih kriteria jasa: Pemasangan, Perbaikan & Pemeliharaan\n
              2. Pilih barang: AC, TV, Kipas Angin, Mesin Cuci, Kulkas, Speaker, Oven, Radio, Sambungan Listrik, CCTV, WIFI\n
              3. Contoh Jenis Jasa: Perbaikan AC, Pemasangan CCTV, Pemeliharaan WIFI""", font=("Arial", 8)).grid(row=4, column=2, sticky='w', padx=5, pady=5)
        Label(mainFrame, text='KELUHAN:', font=("Arial", 12)).grid(row=5, column=0, sticky='w', padx=5, pady=5)
        Label(mainFrame, text="""\nKeterangan Lanjut\n
              1. Pastikan Data Yang Diisi Telah Benar\n
              2. Kami Akan Segera Menghubungi Anda Terkait Pesanan Via Nomor Telepon\n
              3. Jika Ada Perubahan Atau Pembatalan Pesanan Pada Jasa Silahkan Hubung Nomor Ini: 081-111-111-111\n""", font=("Arial", 8)).grid(row=6, column=0, sticky='w', padx=5, pady=5)

        self.txtTanggal = DateEntry(mainFrame, date_pattern='yyyy-mm-dd', font=("Arial", 12))
        self.txtTanggal.grid(row=0, column=1, padx=5, pady=5)

        self.txtNama = Entry(mainFrame, font=("Arial", 12))
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)

        self.txtTelepon = Entry(mainFrame, font=("Arial", 12))
        self.txtTelepon.grid(row=2, column=1, padx=5, pady=5)

        self.txtAlamat = Entry(mainFrame, font=("Arial", 12))
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)

        self.txtJenis_jasa = Entry(mainFrame, font=("Arial", 12))
        self.txtJenis_jasa.grid(row=4, column=1, padx=5, pady=5)

        self.txtKeluhan = Entry(mainFrame, font=("Arial", 12))
        self.txtKeluhan.grid(row=5, column=1, padx=5, pady=5)

        self.txtTotal_biaya = StringVar()
        self.txtTotal_biaya.set('Menghitung...')

        self.txtMekanik = StringVar()
        self.txtMekanik.set('Memilih...')

        self.txtKeterangan = StringVar()
        self.txtKeterangan.set('Belum ada')

        self.txtStatus = StringVar()
        self.txtStatus.set('Diproses...')

        self.btnSimpan = Button(mainFrame, text='Pesan', command=self.onSimpan, width=10, font=("Arial", 12),
                                bg="green", fg="white")
        self.btnSimpan.grid(row=7, column=0, padx=5, pady=5)

        self.btnClear = Button(mainFrame, text='Bersihkan Data', command=self.onClear, width=15, font=("Arial", 12),
                               bg="blue", fg="white")
        self.btnClear.grid(row=7, column=1, padx=5, pady=5)

        self.btnKembali = Button(mainFrame, text='Kembali', command=self.onKembali, width=10, font=("Arial", 12),
                                 bg="red", fg="white")
        self.btnKembali.grid(row=7, column=2, padx=5, pady=5)

        self.tree = ttk.Treeview(mainFrame)
        self.tree.pack(fill=BOTH, expand=YES)
        self.tree["columns"] = (
            "tanggal", "nama", "telepon", "alamat", "jenis_jasa", "keluhan", "total_biaya", "mekanik",
            "keterangan", "status")
        self.tree.heading("tanggal", text="Tanggal")
        self.tree.heading("nama", text="Nama")
        self.tree.heading("telepon", text="Telepon")
        self.tree.heading("alamat", text="Alamat")
        self.tree.heading("jenis_jasa", text="Jenis Jasa")
        self.tree.heading("keluhan", text="Keluhan")
        self.tree.heading("total_biaya", text="Total Biaya")
        self.tree.heading("mekanik", text="Mekanik")
        self.tree.heading("keterangan", text="Keterangan")
        self.tree.heading("status", text="Status")

    def onClear(self):
        self.txtTanggal.delete(0, END)
        self.txtNama.delete(0, END)
        self.txtTelepon.delete(0, END)
        self.txtAlamat.delete(0, END)
        self.txtJenis_jasa.delete(0, END)
        self.txtKeluhan.delete(0, END)
        self.btnSimpan.config(text="Simpan")

    def onSimpan(self):
        pemesanan = Pemesanan()

        # Get the latest kode_pemesanan
        last_kode_pemesanan = pemesanan.get_latest_kode_pemesanan()
        new_kode_pemesanan = last_kode_pemesanan + 1

        # Retrieve other input values
        tanggal = self.txtTanggal.get()
        nama = self.txtNama.get()
        telepon = self.txtTelepon.get()
        alamat = self.txtAlamat.get()
        jenis_jasa = self.txtJenis_jasa.get()
        keluhan = self.txtKeluhan.get()
        total_biaya = self.txtTotal_biaya.get()
        mekanik = self.txtMekanik.get()
        keterangan = self.txtKeterangan.get()
        status = self.txtStatus.get()

        # Create a new Pemesanan object and set its properties
        new_pemesanan = Pemesanan()
        new_pemesanan.kode_pemesanan = new_kode_pemesanan
        new_pemesanan.id_user = self.user_id
        new_pemesanan.tanggal = tanggal
        new_pemesanan.nama = nama
        new_pemesanan.telepon = telepon
        new_pemesanan.alamat = alamat
        new_pemesanan.jenis_jasa = jenis_jasa
        new_pemesanan.keluhan = keluhan
        new_pemesanan.total_biaya = total_biaya
        new_pemesanan.mekanik = mekanik
        new_pemesanan.keterangan = keterangan
        new_pemesanan.status = status

        # Save the new pemesanan data to the database
        result = new_pemesanan.simpan()

        # Show the result in a messagebox
        if result == 'success':
            messagebox.showinfo("Sukses", "Pemesanan berhasil disimpan.")
        else:
            messagebox.showwarning("Sukses", "Berhasil menyimpan pemesanan.")

        self.onClear()
        self.parent.destroy()

    def onKeluar(self):
        self.parent.destroy()

    def onKembali(self):
        self.parent.destroy()

class FrmDataPelanggan:
    def __init__(self, parent, title, user_id):
        self.user_id = user_id
        self.parent = parent
        self.parent.geometry("600x400")  # Adjusted width and height for better visibility
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.parent.state('zoomed')  # Menampilkan form dengan zoomed
        # Judul
        lbl_title = tk.Label(self.parent, text=f"Data Pesanan Anda, ID: {self.user_id}", font=("Arial", 20))
        lbl_title.pack(pady=10)
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        self.btnKembali = Button(mainFrame, text='Kembali', command=self.onKembali, width=10, font=("Arial", 12),
                                 bg="red", fg="white")
        self.btnKembali.pack(pady=10)

        # define columns
        columns = (
            'id_pemesanan', 'kode_pemesanan', 'id_user', 'tanggal', 'nama', 'telepon', 'alamat', 'jenis_jasa',
            'keluhan', 'total_biaya', 'mekanik', 'keterangan', 'status')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_pemesanan', text='ID')
        self.tree.column('id_pemesanan', width="50")
        self.tree.heading('kode_pemesanan', text='KODE')
        self.tree.column('kode_pemesanan', width="50")
        self.tree.heading('id_user', text='ID USER')
        self.tree.column('id_user', width="50")
        self.tree.heading('tanggal', text='TANGGAL')
        self.tree.column('tanggal', width="70")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="70")
        self.tree.heading('telepon', text='TELEPON')
        self.tree.column('telepon', width="70")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="220")
        self.tree.heading('jenis_jasa', text='JENIS JASA')
        self.tree.column('jenis_jasa', width="105")
        self.tree.heading('keluhan', text='KELUHAN')
        self.tree.column('keluhan', width="220")
        self.tree.heading('total_biaya', text='TOTAL BIAYA')
        self.tree.column('total_biaya', width="80")
        self.tree.heading('mekanik', text='MEKANIK')
        self.tree.column('mekanik', width="70")
        self.tree.heading('keterangan', text='KETERANGAN')
        self.tree.column('keterangan', width="220")
        self.tree.heading('status', text='STATUS')
        self.tree.column('status', width="70")
        # set tree position
        self.tree.place(x=0, y=50)

    def onReload(self, event=None):
        # Get data pemesanan based on id_user
        obj = Pemesanan()
        result = obj.get_by_id_user(self.user_id)  # Use self.user_id here to filter data by user ID
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, d in enumerate(result):
            self.tree.insert("", i, values=(
                d["id_pemesanan"], d["kode_pemesanan"], d["id_user"], d["tanggal"], d["nama"], d["telepon"],
                d["alamat"], d["jenis_jasa"], d["keluhan"], d["total_biaya"], d["mekanik"], d["keterangan"],
                d["status"]))
            
    def TampilkanData(self, event=None):
        selected_item = self.tree.selection()
        if selected_item:
            kode_pemesanan = self.tree.item(selected_item)['values'][1]  # Get the kode_pemesanan from the selected item
            obj = Pemesanan()
            res = obj.get_by_kode_pemesanan(kode_pemesanan)
            self.txtKode_pemesanan.delete(0, END)
            self.txtKode_pemesanan.insert(END, obj.kode_pemesanan)
            self.txtId_user.delete(0, END)
            self.txtId_user.insert(END, obj.id_user)
            self.txtNama.delete(0, END)
            self.txtNama.insert(END, obj.nama)
            self.txtTelepon.delete(0, END)
            self.txtTelepon.insert(END, obj.telepon)
            self.txtAlamat.delete(0, END)
            self.txtAlamat.insert(END, obj.alamat)
            self.txtJenis_jasa.delete(0, END)
            self.txtJenis_jasa.insert(END, obj.jenis_jasa)
            self.txtKeluhan.delete(0, END)
            self.txtKeluhan.insert(END, obj.keluhan)
            self.txtTotal_biaya.delete(0, END)
            self.txtTotal_biaya.insert(END, obj.total_biaya)
            self.txtMekanik.delete(0, END)
            self.txtMekanik.insert(END, obj.mekanik)
            self.txtKeterangan.delete(0, END)
            self.txtKeterangan.insert(END, obj.keterangan)
            self.txtStatus.delete(0, END)
            self.txtStatus.insert(END, obj.status)
        self.onReload()

    def onKeluar(self):
        self.parent.destroy()

    def onKembali(self):
        self.parent.destroy()

class MenuFormAdmin:
    def __init__(self):
        self.menu_form = tk.Tk()
        self.menu_form.geometry("300x250")
        self.menu_form.title("Dashboard")
        self.menu_form.state('zoomed')  # Menampilkan form dengan zoomed

        # Judul
        lbl_title = tk.Label(self.menu_form, text="Dashboard", font=("Arial", 20))
        lbl_title.pack(pady=10)

        self.btn_pemesanan = tk.Button(self.menu_form, text="Data Pemesanan", command=self.open_pemesanan_form,
                                       font=("Arial", 12), bg="green", fg="white")
        self.btn_pemesanan.pack()

        self.btn_data = tk.Button(self.menu_form, text="Data Mekanik", command=self.open_mekanik_form, font=("Arial", 12),
                                  bg="blue", fg="white")
        self.btn_data.pack()

        self.btn_logout = tk.Button(self.menu_form, text="Logout", command=self.logout, font=("Arial", 12),
                                    bg="red", fg="white")
        self.btn_logout.pack(pady=10)

    def open_pemesanan_form(self):
        pemesanan_root = tk.Tk()
        pemesanan_form = FrmPemesananAdmin(pemesanan_root, "Form Pemesanan")
        pemesanan_root.mainloop()
        self.menu_form.destroy()
        
    def open_mekanik_form(self):
        mekanik_root = tk.Tk()
        pemesanan_form = FrmMekanik(mekanik_root, "Form Mekanik")
        mekanik_root.mainloop()
        self.menu_form.destroy()

    def logout(self):
        self.menu_form.destroy()
        login_form = FrmLogin()
        
class FrmPemesananAdmin:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        parent.state('zoomed')
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_PEMESANAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_USER:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TELEPON:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENIS_JASA:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KELUHAN:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TOTAL_BIAYA:').grid(row=8, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='MEKANIK:').grid(row=9, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KETERANGAN:').grid(row=10, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STATUS:').grid(row=11, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_pemesanan = Entry(mainFrame) 
        self.txtKode_pemesanan.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_pemesanan.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtId_user = Entry(mainFrame) 
        self.txtId_user.grid(row=1, column=1, padx=5, pady=5)
        # Text box
        self.txtTanggal = DateEntry(mainFrame, date_pattern='yyyy-mm-dd')
        self.txtTanggal.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtTelepon = Entry(mainFrame) 
        self.txtTelepon.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=5, column=1, padx=5, pady=5)
        # Textbox
        self.txtJenis_jasa = Entry(mainFrame) 
        self.txtJenis_jasa.grid(row=6, column=1, padx=5, pady=5)
        # Textbox
        self.txtKeluhan = Entry(mainFrame) 
        self.txtKeluhan.grid(row=7, column=1, padx=5, pady=5)
        # Textbox
        self.txtTotal_biaya = Entry(mainFrame) 
        self.txtTotal_biaya.grid(row=8, column=1, padx=5, pady=5)
        # Textbox
        self.txtMekanik = Entry(mainFrame) 
        self.txtMekanik.grid(row=9, column=1, padx=5, pady=5)
        # Textbox
        self.txtKeterangan = Entry(mainFrame) 
        self.txtKeterangan.grid(row=10, column=1, padx=5, pady=5)
       # Textbox
        self.txtStatus = Entry(mainFrame) 
        self.txtStatus.grid(row=11, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnKeluar = Button(mainFrame, text="Kembali", command=self.onKeluar, width=10)
        self.btnKeluar.grid(row=3, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_pemesanan','kode_pemesanan','id_user','tanggal','nama','telepon','alamat','jenis_jasa','keluhan','total_biaya','mekanik','keterangan','status')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_pemesanan', text='ID')
        self.tree.column('id_pemesanan', width="50")
        self.tree.heading('kode_pemesanan', text='KODE')
        self.tree.column('kode_pemesanan', width="50")
        self.tree.heading('id_user', text='ID USER')
        self.tree.column('id_user', width="50")
        self.tree.heading('tanggal', text='TANGGAL')
        self.tree.column('tanggal', width="70")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="70")
        self.tree.heading('telepon', text='TELEPON')
        self.tree.column('telepon', width="70")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="220")
        self.tree.heading('jenis_jasa', text='JENIS JASA')
        self.tree.column('jenis_jasa', width="105")
        self.tree.heading('keluhan', text='KELUHAN')
        self.tree.column('keluhan', width="220")
        self.tree.heading('total_biaya', text='TOTAL BIAYA')
        self.tree.column('total_biaya', width="80")
        self.tree.heading('mekanik', text='MEKANIK')
        self.tree.column('mekanik', width="70")
        self.tree.heading('keterangan', text='KETERANGAN')
        self.tree.column('keterangan', width="220")
        self.tree.heading('status', text='STATUS')
        self.tree.column('status', width="70")
        # set tree position
        self.tree.place(x=0, y=400)
        
    def onClear(self, event=None):
        self.txtKode_pemesanan.delete(0,END)
        self.txtKode_pemesanan.insert(END,"")
        self.txtId_user.delete(0,END)
        self.txtId_user.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtTelepon.delete(0,END)
        self.txtTelepon.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.txtJenis_jasa.delete(0,END)
        self.txtJenis_jasa.insert(END,"")
        self.txtKeluhan.delete(0,END)
        self.txtKeluhan.insert(END,"")
        self.txtTotal_biaya.delete(0,END)
        self.txtTotal_biaya.insert(END,"")
        self.txtMekanik.delete(0,END)
        self.txtMekanik.insert(END,"")
        self.txtKeterangan.delete(0,END)
        self.txtKeterangan.insert(END,"")
        self.txtStatus.delete(0,END)
        self.txtStatus.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pemesanan
        obj = Pemesanan()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_pemesanan"],d["kode_pemesanan"],d["id_user"],d["tanggal"],d["nama"],d["telepon"],d["alamat"],d["jenis_jasa"],d["keluhan"],d["total_biaya"],d["mekanik"],d["keterangan"],d["status"]))
    def onCari(self, event=None):
        kode_pemesanan = self.txtKode_pemesanan.get()
        obj = Pemesanan()
        a = obj.get_by_kode_pemesanan(kode_pemesanan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_pemesanan = self.txtKode_pemesanan.get()
        obj = Pemesanan()
        res = obj.get_by_kode_pemesanan(kode_pemesanan)
        self.txtKode_pemesanan.delete(0,END)
        self.txtKode_pemesanan.insert(END,obj.kode_pemesanan)
        self.txtId_user.delete(0,END)
        self.txtId_user.insert(END,obj.id_user)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtTelepon.delete(0,END)
        self.txtTelepon.insert(END,obj.telepon)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.txtJenis_jasa.delete(0,END)
        self.txtJenis_jasa.insert(END,obj.jenis_jasa)
        self.txtKeluhan.delete(0,END)
        self.txtKeluhan.insert(END,obj.keluhan)
        self.txtTotal_biaya.delete(0,END)
        self.txtTotal_biaya.insert(END,obj.total_biaya)
        self.txtMekanik.delete(0,END)
        self.txtMekanik.insert(END,obj.mekanik)
        self.txtKeterangan.delete(0,END)
        self.txtKeterangan.insert(END,obj.keterangan)
        self.txtStatus.delete(0,END)
        self.txtStatus.insert(END,obj.status)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_pemesanan = self.txtKode_pemesanan.get()
        id_user = self.txtId_user.get()
        tanggal = self.txtTanggal.get()
        nama = self.txtNama.get()
        telepon = self.txtTelepon.get()
        alamat = self.txtAlamat.get()
        jenis_jasa = self.txtJenis_jasa.get()
        keluhan = self.txtKeluhan.get()
        total_biaya = self.txtTotal_biaya.get()
        mekanik = self.txtMekanik.get()
        keterangan = self.txtKeterangan.get()
        status = self.txtStatus.get()
        # create new Object
        obj = Pemesanan()
        obj.kode_pemesanan = kode_pemesanan
        obj.id_user = id_user
        obj.tanggal = tanggal
        obj.nama = nama
        obj.telepon = telepon
        obj.alamat = alamat
        obj.jenis_jasa = jenis_jasa
        obj.keluhan = keluhan
        obj.total_biaya = total_biaya
        obj.mekanik = mekanik
        obj.keterangan = keterangan
        obj.status = status
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_pemesanan(kode_pemesanan)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_pemesanan = self.txtKode_pemesanan.get()
        obj = Pemesanan()
        obj.kode_pemesanan = kode_pemesanan
        if(self.ditemukan==True):
            res = obj.delete_by_kode_pemesanan(kode_pemesanan)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
class FrmMekanik:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        parent.state('zoomed')
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_MEKANIK:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TELEPON:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='SPESIALIS:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STATUS:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_mekanik = Entry(mainFrame) 
        self.txtKode_mekanik.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_mekanik.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtTelepon = Entry(mainFrame) 
        self.txtTelepon.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtSpesialis = Entry(mainFrame) 
        self.txtSpesialis.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtStatus = Entry(mainFrame) 
        self.txtStatus.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnKeluar = Button(mainFrame, text="Kembali", command=self.onKeluar, width=10)
        self.btnKeluar.grid(row=3, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_mekanik','kode_mekanik','nama','telepon','alamat','spesialis','status')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_mekanik', text='ID_MEKANIK')
        self.tree.column('id_mekanik', width="100")
        self.tree.heading('kode_mekanik', text='KODE_MEKANIK')
        self.tree.column('kode_mekanik', width="100")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="150")
        self.tree.heading('telepon', text='TELEPON')
        self.tree.column('telepon', width="200")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="250")
        self.tree.heading('spesialis', text='SPESIALIS')
        self.tree.column('spesialis', width="250")
        self.tree.heading('status', text='STATUS')
        self.tree.column('status', width="100")
        # set tree position
        self.tree.place(x=0, y=230)
        
    def onClear(self, event=None):
        self.txtKode_mekanik.delete(0,END)
        self.txtKode_mekanik.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtTelepon.delete(0,END)
        self.txtTelepon.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.txtSpesialis.delete(0,END)
        self.txtSpesialis.insert(END,"")
        self.txtStatus.delete(0,END)
        self.txtStatus.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mekanik
        obj = Mekanik()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_mekanik"],d["kode_mekanik"],d["nama"],d["telepon"],d["alamat"],d["spesialis"],d["status"]))
    def onCari(self, event=None):
        kode_mekanik = self.txtKode_mekanik.get()
        obj = Mekanik()
        a = obj.get_by_kode_mekanik(kode_mekanik)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_mekanik = self.txtKode_mekanik.get()
        obj = Mekanik()
        res = obj.get_by_kode_mekanik(kode_mekanik)
        self.txtKode_mekanik.delete(0,END)
        self.txtKode_mekanik.insert(END,obj.kode_mekanik)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtTelepon.delete(0,END)
        self.txtTelepon.insert(END,obj.telepon)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.txtSpesialis.delete(0,END)
        self.txtSpesialis.insert(END,obj.spesialis)
        self.txtStatus.delete(0,END)
        self.txtStatus.insert(END,obj.status)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_mekanik = self.txtKode_mekanik.get()
        nama = self.txtNama.get()
        telepon = self.txtTelepon.get()
        alamat = self.txtAlamat.get()
        spesialis = self.txtSpesialis.get()
        status = self.txtStatus.get()
        # create new Object
        obj = Mekanik()
        obj.kode_mekanik = kode_mekanik
        obj.nama = nama
        obj.telepon = telepon
        obj.alamat = alamat
        obj.spesialis = spesialis
        obj.status = status
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_mekanik(kode_mekanik)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_mekanik = self.txtKode_mekanik.get()
        obj = Mekanik()
        obj.kode_mekanik = kode_mekanik
        if(self.ditemukan==True):
            res = obj.delete_by_kode_mekanik(kode_mekanik)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    login_form = FrmLogin()
    login_form.login_form.mainloop()
