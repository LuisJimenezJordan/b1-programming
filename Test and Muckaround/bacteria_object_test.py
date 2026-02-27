class environment:
    def __init__(self, oxygen, pH, temperature):
        self.oxygen = oxygen
        self.pH = pH
        self.temperature = temperature

### function to retrieve values to populate the environment object
def get_environment_values():
    oxygen_value = print(input("Is oxygen present?: ").strip().lower())
    oxygen = (oxygen_value == "yes")

    while True:
        try:
            pH = float(input("Enter pH (0-14): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            temperature = float(input("Enter temperature (in degrees C): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    return environment(oxygen, pH, temperature)

###

class order:
    ordertype = "Enterobacterales"
    def respiration(self):
        self.fac_an = True

class family(order):
    familytype = "Enterobacteriaceae"

class genus(family):
    genustype = "Escherichia"
    def motility(self):
        self.flagella = True

class species(genus):
    speciestype = "coli"

class organism_status:
    def __init__(self, species):
        self.species = species

    def display_info(self):
        print(f"Complete organism name is "
              f"{self.species.ordertype} "
              f"{self.species.familytype} "
              f"{self.species.genustype} "
              f"{self.species.speciestype}"
              )

ID_3957 = species()
habitat_293 = get_environment_values()
bacteria = organism_status(ID_3957)
bacteria.display_info()

"""class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0 # optional: to show driving simulation

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def drive(self, distance):
        self.mileage += distance
        print(f"Driving {distance} km... Total mileage is now {self.mileage} km.")

# --- Example usage ---
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()
my_car.drive(50)
my_car.drive(120)"""
