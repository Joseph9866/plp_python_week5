# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage_capacity):
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity

    def turn_on(self):
        print(f"{self.brand} {self.model} is turning on...")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turning off...")

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage_capacity} GB"


# Derived class: SmartphoneWithCamera (inherits from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage_capacity, camera_quality):
        super().__init__(brand, model, storage_capacity)
        self.camera_quality = camera_quality

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} camera quality.")

    def turn_on(self):
        # Polymorphism: Different behavior for turning on with a camera
        print(f"{self.brand} {self.model} with {self.camera_quality} camera is powering up...")

    def get_info(self):
        # Overriding get_info to include camera quality
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage_capacity} GB, Camera: {self.camera_quality} MP"


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128)
phone2 = SmartphoneWithCamera("Apple", "iPhone 13", 256, 12)

# Access methods
print(phone1.get_info())
phone1.turn_on()
phone1.turn_off()

print("\n" + phone2.get_info())
phone2.turn_on()
phone2.take_photo()
phone2.turn_off()
