# Base Class
class Smartphone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def display_info(self):
        return f"{self.brand} {self.model} costs ${self.price} with {self.storage}GB storage."

    def make_call(self, number):
        return f"Dialing {number} from {self.model}..."

# Inherited Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, storage, gpu_power):
        super().__init__(brand, model, price, storage)
        self.gpu_power = gpu_power

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} It's a gaming phone with GPU power: {self.gpu_power}."

    def launch_game(self, game_name):
        return f"Launching {game_name} on {self.model} with top-notch graphics."

# Example Usage
phone = Smartphone("Apple", "iPhone 14", 999, 128)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1199, 256, "Adreno 730")

print(phone.display_info())
print(phone.make_call("123-456-7890"))

print(gaming_phone.display_info())
print(gaming_phone.launch_game("Call of Duty Mobile"))



# Acitvity 2
class Vehicle:
    def move(self):
        return "This vehicle moves in a unique way."

class Car(Vehicle):
    def move(self):
        return "Driving on roads 🚗."

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️."

class Boat(Vehicle):
    def move(self):
        return "Sailing on water ⛵."

class Animal:
    def move(self):
        return "This animal moves differently."

class Bird(Animal):
    def move(self):
        return "Flying with wings 🦅."

class Fish(Animal):
    def move(self):
        return "Swimming in water 🐟."

class Horse(Animal):
    def move(self):
        return "Galloping on land 🐎."

# Example Usage
vehicles = [Car(), Plane(), Boat()]
animals = [Bird(), Fish(), Horse()]

print("Vehicle Movements:")
for vehicle in vehicles:
    print(vehicle.move())

print("\nAnimal Movements:")
for animal in animals:
    print(animal.move())
