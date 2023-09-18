#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
user = User()
user.first_name = "olamilekan"
user.last_name = "akintola"
user.email = "akintola14@gmail.com"

user.save()

place = Place()
place.user_id


