from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        return "car stopped"

class SportCar(Car):
    
    def start_engine(self):
        message = super().start_engine()
        return f"{message}. Max speed is {self.max_speed}"

    def stop_engine(self):
        message = super().stop_engine()
        self.current_speed = 0
        return f"{message}. Current speed is {self.current_speed}"
