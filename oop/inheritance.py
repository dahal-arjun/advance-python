class Vehicle:
    """
    Vehicle class is the parent class for your example.

    We are assuming these functions are the basic functionality of a vehicle.
    We will explore more about the advantages and disadvantages of inheritance.
    We will also learn more about composition over inheritance.

    For now, let's assume that our Vehicle must start_engine and stop_engine.
    This demonstrates the basic concept of relationships like IS A and HAS A between classes.
    We will focus on OOP principles for now; later, we will learn more about UML
    notations, compositions, and design patterns.
    """

    def __init__(self, make: str, model: str, year:int) -> None:
        """
        The __init__ method is executed first when an object is created.
        This method initializes the Vehicle instance with make, model, and name.

        Example:
            Vehicle(make="Kawasaki", model="H2", year="2024")
        """
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine has started.")

    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine has stopped.")

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"



class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, num_doors:int) -> None:
        """
        The only new feature we have added here is, num_doors.
        while other inputs are same as the parent class.

        We are intorducing a new feature for the car which might only be in car but not
        on other vehicles.

        The make model and year are the three attributes we require and we are saying
        without these three things nothing is vechicle. We must have make, model and year
        for the anything to be vehicle.
        """
        super().__init__(make, model, year)
        """
            Once we satify all the requirements of the vehicle. Then, we are working on the
            additional feature for the Car. We are passing the num_doors which is specific to
            our car only. Other vehicle might not have the doors.
        """
        self.num_doors = num_doors

    """
        We can add additional features specific to the car. These features will be only for the car.
        Not other siblings of the Car.
    """
    def open_trunk(self):
        """
            This is specific feature for the car. Here we don't care about other types of vehicle.
            We only want this open_trunk feature implemented on the car only.
        """
        print(f"The trunk of the {self.make} {self.model} is now open.")

    def close_trunk(self):
        print(f"The trunk of the {self.make} {self.model} is now closed.")


    def display_info(self):
        """
            This is the example where we are overriding the original display method.
            As we also want to display the no of doors and the previous display method
            does not have the implemntation to show the doors.
        """
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make:str, model:str, year:int, has_sidecar:bool):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def pop_wheelie(self):
        print(f"The {self.make} {self.model} pops a wheelie!")

    def display_info(self):
        super().display_info()
        sidecar_status = "has a sidecar." if self.has_sidecar else "does not have a sidecar."
        print(f"This motorcycle {sidecar_status}")


# creating the objects for vehicle and the Car class
car = Car(
    make="Toyota",
    model="Corolla",
    year=2020,
    num_doors=4
)

car.display_info()

motor_bike = Motorcycle(
    make="Kawasaki",
    model="Ninja H2",
    year=2024,
    has_sidecar=False
)

motor_bike.display_info()
