"""
Welcom message

set up and loading

menu
    - Play
        - if there is a character created, have load option on top
        - create character
        - Ask to create a new save world/ load world
    - Character managment
        - creating
        - edit
        - delete
    - settings
        - Manage Content
            - Equipment
            - Roles
            - Powers
            - Enemies
        - game settings (not sure yet)
            - difficulyy
            - number of levels?

"""
import os

from loguru import logger

from funclg.managers import build_manager_menu
from funclg.utils.menu_funcs import Menu, save_exit

GAME_NAME = "FUNCLG"


def build_main_menu():
    """Contructs the main menu for the game"""
    menu = Menu("Main Menu", "Please choice an option:", has_return=False)
    menu.add_item("Play", None)  # TODO: add play instance
    menu.add_item("Manage Game", build_manager_menu())
    menu.add_item("Exit", save_exit)
    return menu


def game_set_up():
    logger.info(f"Setting up {GAME_NAME}")
    # Set up data folder
    data_path = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(data_path):
        os.mkdir(data_path)
        logger.debug(f"Creating data path: {data_path}")

    globals()["DATA_PATH"] = data_path

    # Builds Menus
    logger.info("Menuas Loadas...")
    return build_main_menu()


def main():
    main_menu = game_set_up()
    try:
        while True:
            main_menu.print_menu()

    except KeyboardInterrupt:
        print()
        save_exit()


if __name__ == "__main__":
    main()
