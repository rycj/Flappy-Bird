# Finální verze Flappy Bird

from config import *
from Menu import Menu


# Funkce main
def main():
    running: bool = True
    menu: bool = True
    lobby = Menu()
    # Hlavní smyčka
    while running:

        # Zapne menu
        lobby.draw()
        lobby.textchange()

        # Kontroluje menu
        while menu:
            menu = lobby.run()
        # Vrátí zpět do menu
        menu = True


# ...
if __name__ == main():
    main()
