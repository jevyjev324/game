"""
Programmer: Jevin Evans
Date: 6.19.2022
Description: A manager class for creating, updating, and removing equipment.
"""

from funclg.character.equipment import BodyEquipment, WeaponEquipment
from funclg.utils.data_mgmt import load_data
from funclg.utils.input_validation import choice_validation

EQUIPMENT_DATABASE = "equipment.json"


def _equipment_set_up(action: str):
    equipment_data = load_data(EQUIPMENT_DATABASE)
    print(f"What type of equipment do you want to {action}?\n1. Body Equipment\n2. Weapons")
    if choice_validation(2) == 1:
        return "body_armor"
    return "weapon"


def _new_weapon():
    print("TODO: Build New Weapon Section")


def _new_body_armor():
    print("TODO: Build New Body Armor Section")


def _edit_weapon():
    print("TODO: Build Edit Weapon Section")


def _edit_body_armor():
    print("TODO: Build Edit Body Armor Section")


def _delete_weapon():
    print("TODO: Build Delete Weapon Section")


def _delete_body_armor():
    print("TODO: Build Delete Body Armor Section")


def build_equipment():
    print("TODO: Build New Equipment")
    choice = _equipment_set_up("New")
    if choice == "weapon":
        _new_weapon()
    else:
        _new_body_armor()


def edit_equipment():
    print("TODO: Build Edit Equipment Section")


def delete_equipment():
    print("TODO: Build Delete Equipment Section")


EQUIPMENT_MENU = {
    "name": "Manage Equipment",
    "description": "This the menu to create armor and weapons for characters to use.",
    "menu_items": [
        {"name": "New Equipment", "action": build_equipment},
        {"name": "Edit Equipment", "action": edit_equipment},
        {"name": "Delete Equipment", "action": delete_equipment},
    ],
}
