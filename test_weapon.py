import random
from unittest.mock import patch

from weapon import Weapon


def test_attack_with_broken_weapon():
    weapon = Weapon(10, 20, 15, 10, 10)

    # with patch.object(weapon, "health", 5):
    #     assert weapon.health == 15

    # assert weapon.attack() == 15

    # option + enter - mac
    # alt + enter - windows

    with patch.object(random, "randint", side_effect=[8, 2]):
        # attack = weapon.attack()

        # print(attack)
        assert weapon.health == 15  # vychozi stav
        assert weapon.attack() == 12
        assert weapon.health == 16  # stav po zavolani metody attack

