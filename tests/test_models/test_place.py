#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import os
import models
import unittest
import datetime
from time import sleep
from models.place import Place
from models.base_model import BaseModel


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def setUp(self):
        self.place = Place()

    def test_instantiates(self):
        self.assertIsInstance(self.place, BaseModel)
        self.assertIsInstance(self.place, Place)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.place, models.storage.all().values())

    def test_city_id_attribute(self):
        self.assertEqual(str, type(self.place.city_id))
        self.assertIn("city_id", dir(self.place))
        self.assertNotIn("city_id", self.place.__dict__)

    def test_two_places_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_places_different_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)


class TestPlaceSave(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


class TestPlaceToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def setUp(self):
        self.place = Place()

    def test_to_dict_type(self):
        self.assertIsInstance(self.place.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        pl_dict = self.place.to_dict()
        self.assertIn("id", pl_dict)
        self.assertIn("created_at", pl_dict)
        self.assertIn("updated_at", pl_dict)
        self.assertIn("__class__", pl_dict)

    def test_to_dict_output(self):
        dt = datetime.today()
        self.place.id = "123456"
        self.place.created_at = self.place.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(self.place.to_dict(), tdict)


if __name__ == "__main__":
    unittest.main()
