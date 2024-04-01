# M Nahrowi
#  Class and Objek

class Mobil:
    def __init__ (self, name , merk, color, price) -> any :
        self.name = name
        self.merk = merk
        self.color = color 
        self.price = price


mobil_1 = Mobil("Avanza", "Toyota", "Silver", 100000000)


print(mobil_1.name)