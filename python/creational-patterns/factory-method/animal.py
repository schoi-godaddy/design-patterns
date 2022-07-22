from abc import ABC, abstractmethod


class Animal(ABC):
    """
    The Animal interface declares the operations that all concrete Animals
    must implement.
    """

    @abstractmethod
    def cry(self) -> str:
        pass


class Dog(Animal):
    def cry(self) -> str:
        return "Woof, Woof!"


class Cat(Animal):
    def cry(self) -> str:
        return "Meow, Meow!"
