class Kakek:
    def __init__(self):
        print("Kakek")

class Ayah(Kakek):
    def __init__(self):
        print('a', super())
        super().__init__()
        print("Ayah")

class Ibu(Kakek):
    def __init__(self):
        print('i', super())
        super().__init__()
        print("Ibu")


class Anak(Ayah, Ibu):
    def __init__(self):
        print('k', super())
        super().__init__()
        print("Anak")

k = Anak()