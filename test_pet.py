from pet import Pet, PetHouse
import pytest

pet1 = Pet("prasatko")
pet2 = Pet("konicek")
pet3 = Pet("oslicek")
pet4 = Pet("kravicka")


@pytest.mark.parametrize("input_value, expected_output", [((pet1, pet2), 3), (pet2, 2)])
def test_pet_in_house_list(input_value,expected_output):
    house = PetHouse()
    house.visit(input_value)
    house.number_of_pets() == expected_output
    house.leave(input_value)
    house.number_of_pets() == expected_output
