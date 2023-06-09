class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_reamur(self):
        return (4/5) * self.celsius

    def to_kelvin(self):
        return self.celsius + 273.15

    def to_fahrenheit(self):
        return (9/5) * self.celsius + 32


temperature = TemperatureConverter(30)
fahrenheit = temperature.to_fahrenheit()
kelvin = temperature.to_kelvin()
reamur = temperature.to_reamur()

print(f"{temperature.celsius} derajat Celsius = {reamur} derajat Reamur")
print(f"{temperature.celsius} derajat Celsius = {kelvin} Kelvin")
print(f"{temperature.celsius} derajat Celsius = {fahrenheit} derajat Fahrenheit")