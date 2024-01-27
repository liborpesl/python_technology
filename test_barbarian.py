from unittest.mock import Mock

from barbarian import Barbarian
from weapon import Weapon


# dvakrat shift

def test_attack_with_damage():
    weapon_damage = 25
    barbarian_damage = 60

    mock_weapon = Mock(spec=Weapon)
    mock_weapon.attack.return_value = weapon_damage

    barbarian = Barbarian(barbarian_damage, 60, mock_weapon)

    assert barbarian.attack() == weapon_damage + barbarian_damage + 15