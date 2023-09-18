"""
This script demonstrates the usage of the BaseModel class and its methods.
"""

#!/usr/bin/python3
from models.base_model import BaseModel

try:
    # Create an instance of the BaseModel class
    my_model = BaseModel()

    # Set the name attribute of the model
    my_model.name = "My_First_Model"

    # Set the my_number attribute of the model
    my_model.my_number = 89

    # Print the id attribute of the model
    print(my_model.id)

    # Print the model object
    print(my_model)

    # Print the type of the created_at attribute of the model
    print(type(my_model.created_at))

    print("--")

    # Convert the model object to a dictionary
    my_model_json = my_model.to_dict()

    # Print the JSON representation of the model
    print(my_model_json)

    # Print the individual key-value pairs of the JSON representation
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key,
              type(my_model_json[key]), my_model_json[key]))

    print("--")

    # Create a new model object using the JSON representation
    my_new_model = BaseModel(**my_model_json)

    # Print the id attribute of the new model
    print(my_new_model.id)

    # Print the new model object
    print(my_new_model)

    # Print the type of the created_at attribute of the new model
    print(type(my_new_model.created_at))

    print("--")

    # Check if my_model and my_new_model are the same object
    print(my_model is my_new_model)

except Exception as e:
    # Handle any exceptions that occur during execution
    print(f"An error occurred: {e}")
