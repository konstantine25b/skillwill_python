from abc import ABC, abstractmethod

class LivingBeing(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def __repr__(self):
        return self.__str__()

class Machine(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def __repr__(self):
        return self.__str__()

class Animal(LivingBeing):
    def __init__(self, name, species):
        self.__name = name
        self.__species = species

    def __str__(self):
        return f"Animal(Name: {self.__name}, Species: {self.__species})"

    def sound(self):
        return "Animal sound"

    def move(self):
        return "Animal movement"

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

class Vehicle(Machine):
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    def __str__(self):
        return f"Vehicle(Make: {self.__make}, Model: {self.__model})"

    def start_engine(self):
        return "Engine started"

    def stop_engine(self):
        return "Engine stopped"

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.__breed = breed

    def __str__(self):
        return f"Dog(Name: {self.name}, Breed: {self.__breed})"

    def sound(self):
        return "Bark"

    def move(self):
        return "Run"

    @property
    def breed(self):
        return self.__breed

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self._fuel_type = fuel_type  # Protected data

    def __str__(self):
        return f"Car(Make: {self.make}, Model: {self.model}, Fuel Type: {self._fuel_type})"

    def start_engine(self):
        if self._fuel_type not in ["Petrol", "Diesel", "Electric"]:
            raise ValueError("Invalid fuel type")
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        if value not in ["Petrol", "Diesel", "Electric"]:
            raise ValueError("Invalid fuel type")
        self._fuel_type = value

class SoundMixin:
    def make_sound(self):
        return "This is a sound"

class AnimalWithSound(Animal, SoundMixin):
    def __init__(self, name, species):
        super().__init__(name, species)

    def sound(self):
        return super().sound() + " " + self.make_sound()


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        if isinstance(pet, Animal):
            self.pets.append(pet)
        else:
            raise TypeError("Only animals can be added as pets")

    def __str__(self):
        pets_str = ', '.join(str(pet) for pet in self.pets)
        return f"Owner(Name: {self.name}, Pets: [{pets_str}])"



