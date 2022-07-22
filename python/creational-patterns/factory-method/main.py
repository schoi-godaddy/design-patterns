import animal_toy


def toy_testor(toy: animal_toy.AnimalToy) -> None:
    print("Client: Testing Animal Toy!")
    print(toy.make_sound())


if __name__ == "__main__":
    print("App: Launched with the CatToy.")
    toy_testor(animal_toy.CatToy())

    print("\n")

    print("App: Launched with the DogToy.")
    toy_testor(animal_toy.DogToy())
