"""
This script demonstrates the usage of the BaseModel class and its methods.
"""

#!/usr/bin/python3
from models.base_model import BaseModel

try:
    # Create an instance of the BaseModel class
    my_model = BaseModel()

    # Set the name attribute of the model
    my_model.name = "My First Model"

    # Set the my_number attribute of the model
    my_model.my_number = 89

    # Print the model object
    print(my_model)

    # Save the model to a file
    my_model.save()

    # Print the updated model object after saving
    print(my_model)

    # Convert the model object to a dictionary
    my_model_json = my_model.to_dict()

    # Print the JSON representation of the model
    print(my_model_json)

    # Print the individual key-value pairs of the JSON representation
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key,
              type(my_model_json[key]), my_model_json[key]))

except Exception as e:
    # Handle any exceptions that occur during execution
    print(f"An error occurred: {e}")
