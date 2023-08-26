# Alinura Sultanova
# 08.17.2023

#Problem Python Class ‘car’:

class Car:
    def __init__(self, model, year, color):
        """
        Initializes the Car object with model, year, and color attributes.
        
        Parameters:
        model (str): The model of the car.
        year (int): The year of manufacture.
        color (str): The color of the car.
        """
        self.model = model
        self.year = year
        self.color = color
    
    def get_model(self):
        """
        Returns the model of the car.
        
        Returns:
        str: The model of the car.
        """
        return self.model
    
    def get_year(self):
        """
        Returns the year of manufacture of the car.
        
        Returns:
        int: The year of manufacture.
        """
        return self.year
    
    def get_color(self):
        """
        Returns the color of the car.
        
        Returns:
        str: The color of the car.
        """
        return self.color
    
    def fullspecs(self):
        """
        Returns the full specifications of the car.
        
        Returns:
        str: The full specifications of the car.
        """
        return self.model + ' ' + str(self.year) + ' ' + self.color

# Create Car instances
car1 = Car("Sports", 2012, "Blue")
car2 = Car("Sedan", 2020, "Black")

# Test the methods
print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())

# finish