from dest.action import add_destination, print_destination
from storage.load_save import save, load
from icecream import ic # to import ic from icecream package (inside venv!!!)



my_destinations = []


def menu():
    load()
    ic () # using icecream, switches print with ic
    while True:
        ic("1-add")
        ic("2-list")
        ic("3-load")
        ic("4-save")
        ic("5-exit")
        selection = input("Your command? ")
        if selection == "1":
            add_destination(my_destinations)
        if selection == "2":
            print_destination(my_destinations)
            pass
        if selection == "3":
            load()
        if selection == "4":
            save()
        if selection == "5":
            save()
            exit()

if __name__ == "__main__":    
    menu()                    
# so you will only start the program using the main file (app.py f.e)