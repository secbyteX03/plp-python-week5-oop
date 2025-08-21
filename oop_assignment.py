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