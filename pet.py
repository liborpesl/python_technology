class Pet:
    def __init__(self, pet):
        self.pet = pet

    def __str__(self):
        return f'{self.pet}'


class PetHouse:
    def __init__(self, pet_in_house=None):
        if pet_in_house is None:
            pet_in_house = []
        self.pets = pet_in_house.copy()

    def visit(self, pet):
        if pet in self.pets:
            print(f"{pet} is already in the house")
        else:
            self.pets.append(pet)

    def leave(self, pet):
        if pet in self.pets:
            self.pets.remove(pet)
        else:
            print(f"{pet} is not in the house")

    def list(self):
        print("Pets in the house")
        for i in self.pets:
            print(i)

    def number_of_pets(self):
        return len(self.pets)
