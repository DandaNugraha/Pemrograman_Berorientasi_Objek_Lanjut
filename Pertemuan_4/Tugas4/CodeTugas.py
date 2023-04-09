class Artist:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

artist1 = Artist("Ariana Grande", "Amerika Serikat")
song1 = Song("thank u, next", artist1)

print("Judul Lagu:", song1.name)
print("Artist:", song1.artist.name)
print("Negara Asal Artist:", song1.artist.country)

class Tire:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

class Wheel:
    def __init__(self, position, tire):
        self.position = position
        self.tire = tire

tire1 = Tire("Michelin", 19)
wheel1 = Wheel("depan kiri", tire1)

print("Posisi Roda:", wheel1.position)
print("Merek Ban:", wheel1.tire.brand)
print("Ukuran Ban:", wheel1.tire.size)

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Bread:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

ingredient1 = Ingredient("tepung terigu", "500 gram")
ingredient2 = Ingredient("gula pasir", "100 gram")
bread1_ingredients = [ingredient1, ingredient2]
bread1 = Bread("roti tawar", bread1_ingredients)

print("Jenis Roti:", bread1.name)
print("Bahan-bahan:")
for ingredient in bread1.ingredients:
    print("- " + ingredient.amount + " " + ingredient.name)
