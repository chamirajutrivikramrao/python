#abstraction
from abc import ABC,abstractmethod
class vehical(ABC):
    @abstractmethod
    def clutch(self):
        pass
class bike(vehical):
    def clutch(self):
        print("bike moves")
b1=bike()
b1.clutch()
