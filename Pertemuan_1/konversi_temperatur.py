class Fahrenheit:
    def __init__(self, temp):
        self.temp = temp
        
    def to_celsius(self):
        return (self.temp - 32) * 5 / 9

    def to_reamur(self):
        return (self.temp - 32) * 4 / 9

    def to_kelvin(self):
        return (self.temp - 32) * 5 / 9 + 273.15

fahrenheit = Fahrenheit(30)
celcius = int(fahrenheit.to_celsius())
kelvin = int(fahrenheit.to_kelvin())
reamur = int(fahrenheit.to_reamur())

print(f"{fahrenheit.temp} derajat Fahrenheit = {celcius} derajat Celcius")
print(f"{fahrenheit.temp} derajat Fahrenheit = {kelvin} derajat Kelvin")
print(f"{fahrenheit.temp} derajat Fahrenheit = {reamur} derajat Reamur\n")

class Reamur:
    def __init__(self, temp):
        self.temp = temp

    def to_celsius(self):
        return self.temp * 5 / 4

    def to_fahrenheit(self):
        return self.temp * 9 / 4 + 32

    def to_kelvin(self):
        return self.temp * 5 / 4 + 273.15

reamur = Reamur(30)
celcius = reamur.to_celsius()
kelvin = reamur.to_kelvin()
fahrenheit = reamur.to_fahrenheit()

print(f"{reamur.temp} derajat Reamur = {celcius} derajat Celcius")
print(f"{reamur.temp} derajat Reamur = {kelvin} derajat Kelvin")
print(f"{reamur.temp} derajat Reamur = {fahrenheit} derajat Fahrenheit\n")

class Kelvin:
    def __init__(self, temp):
        self.temp = temp

    def to_celsius(self):
        return self.temp - 273.15

    def to_fahrenheit(self):
        return (self.temp - 273.15) * 9 / 5 + 32

    def to_reamur(self):
        return (self.temp - 273.15) * 4 / 5
        
kelvin = Kelvin(30)
celcius = round(kelvin.to_celsius(), 1)
fahrenheit = round(kelvin.to_fahrenheit(), 1)
reamur = round(kelvin.to_reamur(), 1)

print(f"{kelvin.temp} derajat Kelvin = {celcius} derajat Celcius")
print(f"{kelvin.temp} derajat Kelvin = {fahrenheit} derajat Fahrenheit")
print(f"{kelvin.temp} derajat Kelvin = {reamur} derajat Reamur")