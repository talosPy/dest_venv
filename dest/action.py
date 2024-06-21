# Place ***my_destinations*** inside the function params so the functions will recognise it
# IMPORTANT : Don't forget to add the my_destinations to the app.py params so it will call it.

def add_destination(my_destinations):
    # CAN ALSO : from app import my_destinations (without params in functions)
    # NOT a good practice!!!
    new_destination = input('Choose Destination')
    my_destinations.append(new_destination)
    

def print_destination(my_destinations):
    print(my_destinations)


