from inventory.inventory import MP_Inventory as Inventory
from ui.menu import Menu

def main():
    # Set up db
    inventory = Inventory()
    # Menu(inventory)
    menu = Menu()
    menu.mainMenu(inventory)
    exit()
    inventory.close()
main()