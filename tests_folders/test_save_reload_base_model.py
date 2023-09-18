#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel


def main():
    """
    Main function that reloads existing objects, prints them,
    creates a new object, saves it, and prints it.
    """
    try:
        # Reload existing objects
        all_objs = storage.all()
        print("-- Reloaded objects --")

        # Print all reloaded objects
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

        # Create a new object
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)

    except Exception as e:
        # Handle any exceptions/errors that occur
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
