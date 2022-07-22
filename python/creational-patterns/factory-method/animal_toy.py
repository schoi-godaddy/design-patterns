from abc import ABC, abstractmethod
import animal


class AnimalToy(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def make_sound(self) -> str:
        animal = self.factory_method()

        result = f"Animal: New animal! {animal.cry()}"

        return result


class DogToy(AnimalToy):
    def factory_method(self) -> animal.Dog:
        return animal.Dog()


class CatToy(AnimalToy):
    def factory_method(self) -> animal.Cat:
        return animal.Cat()
