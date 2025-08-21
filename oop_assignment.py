# PLP Python Week 5 - OOP Assignment
# Assignment 1: Smartphone Class with Inheritance

class Smartphone:
    """Base class representing a smartphone"""
    
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
        self.is_on = False
        self.apps_installed = []
    
    def power_on(self):
        """Turn on the smartphone"""
        self.is_on = True
        return f"{self.brand} {self.model} is now ON"
    
    def power_off(self):
        """Turn off the smartphone"""
        self.is_on = False
        return f"{self.brand} {self.model} is now OFF"
    
    def install_app(self, app_name):
        """Install an app on the smartphone"""
        if self.is_on:
            self.apps_installed.append(app_name)
            return f"{app_name} installed successfully!"
        else:
            return "Please turn on the phone first"
    
    def get_info(self):
        """Get smartphone information"""
        return f"{self.brand} {self.model} - {self.storage}GB storage, {self.battery_life}h battery"

# Inheritance: Gaming Smartphone
class GamingSmartphone(Smartphone):
    """Gaming smartphone with additional gaming features"""
    
    def __init__(self, brand, model, storage, battery_life, cooling_system, refresh_rate):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate  # in Hz
        self.gaming_mode = False
    
    def activate_gaming_mode(self):
        """Activate gaming mode for better performance"""
        if self.is_on:
            self.gaming_mode = True
            return f"Gaming mode activated! {self.refresh_rate}Hz refresh rate enabled"
        else:
            return "Please turn on the phone first"
    
    def get_info(self):
        """Override parent method with gaming-specific info"""
        base_info = super().get_info()
        return f"{base_info}, {self.refresh_rate}Hz display, {self.cooling_system} cooling"
    
# Assignment 2: Polymorphism Challenge - Vehicles

class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        """Base move method - to be overridden by subclasses"""
        return f"{self.name} is moving"
    
    def get_info(self):
        """Get vehicle information"""
        return f"{self.name} - Max speed: {self.speed} km/h"

class Car(Vehicle):
    """Car class with driving movement"""
    
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type
    
    def move(self):
        """Cars drive on roads"""
        return f"{self.name} is driving on the road 🚗"
    
    def honk(self):
        """Cars can honk"""
        return f"{self.name} goes BEEP BEEP!"

class Plane(Vehicle):
    """Plane class with flying movement"""
    
    def __init__(self, name, speed, altitude):
        super().__init__(name, speed)
        self.altitude = altitude  # in feet
    
    def move(self):
        """Planes fly in the air"""
        return f"{self.name} is flying at {self.altitude} feet ✈️"
    
    def takeoff(self):
        """Planes can take off"""
        return f"{self.name} is taking off!"

class Boat(Vehicle):
    """Boat class with sailing movement"""
    
    def __init__(self, name, speed, boat_type):
        super().__init__(name, speed)
        self.boat_type = boat_type
    
    def move(self):
        """Boats sail on water"""
        return f"{self.name} is sailing on the water ⛵"
    
    def anchor(self):
        """Boats can drop anchor"""
        return f"{self.name} has dropped anchor!"

class Bicycle(Vehicle):
    """Bicycle class with pedaling movement"""
    
    def __init__(self, name, speed, gear_count):
        super().__init__(name, speed)
        self.gear_count = gear_count
    
    def move(self):
        """Bicycles are pedaled"""
        return f"{self.name} is being pedaled 🚴"
    
    def ring_bell(self):
        """Bicycles have bells"""
        return f"{self.name} goes RING RING!"

# Demonstration function
def demonstrate_polymorphism(vehicles):
    """Demonstrate polymorphism with different vehicles"""
    print("===============================================")
    for vehicle in vehicles:
        print(f"{vehicle.get_info()}")
        print(f"Movement: {vehicle.move()}")
        print("-" * 40)
    print("End of Polymorphism Demo\n")
# Main execution
if __name__ == "__main__":
    print("🏗️ ASSIGNMENT 1: SMARTPHONE CLASS DEMO 🏗️")
    print("=" * 50)
    
    # Create regular smartphone
    phone1 = Smartphone("Apple", "iPhone 15", 256, 20)
    print(phone1.get_info())
    print(phone1.power_on())
    print(phone1.install_app("Instagram"))
    print(phone1.install_app("TikTok"))
    print(f"Apps installed: {phone1.apps_installed}")
    print()
    
    # Create gaming smartphone (inheritance)
    gaming_phone = GamingSmartphone("ASUS", "ROG Phone 8", 512, 18, "Vapor Chamber", 165)
    print(gaming_phone.get_info())
    print(gaming_phone.power_on())
    print(gaming_phone.activate_gaming_mode())
    print()
    print("🎭 ASSIGNMENT 2: POLYMORPHISM CHALLENGE 🎭")
    print("=" * 50)
    print("🏎️ VEHICLES POLYMORPHISM DEMO 🏎️")
    
    # Create different vehicles
    vehicles = [
        Car("Tesla Model S", 250, "Electric"),
        Plane("Boeing 737", 850, 35000),
        Boat("Ocean Explorer", 45, "Yacht"),
        Bicycle("Mountain Bike", 30, 21)
    ]
    
    # Demonstrate polymorphism
    demonstrate_polymorphism(vehicles)
    
    # Show individual special methods
    print("=== Special Vehicle Actions ===")
    car = vehicles[0]
    plane = vehicles[1]
    boat = vehicles[2]
    bike = vehicles[3]
    
    print(car.honk())
    print(plane.takeoff())
    print(boat.anchor())
    print(bike.ring_bell())
    print("=" * 50)
    print("🏁 End of Assignment Demo 🏁")