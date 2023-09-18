#!/usr/bin/python3
"""
    This module is for testing the BaseModel
    unittest classes:
        TestBaseModelId - line 12

"""
import os
import unittest
import models
import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelId(unittest.TestCase):
    """
        This test class is to test the
        ID assignment
    """

    def test_with_id(self):
        """
            get id of the BaseModel object instance
        """
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        self.assertEqual(model1.id, model1.id)
        self.assertEqual(model2.id, model2.id)
        self.assertEqual(model3.id, model3.id)

    def test_id_not_the_same(self):
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        self.assertNotEqual(model2.id, model1.id)
        self.assertNotEqual(model3.id, model2.id)
        self.assertNotEqual(model1.id, model3.id)


###
# TEST SAVE METHOD
class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


##
# TEST TO_DICT
class TestBaseModelToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(isinstance(bm.to_dict(), dict))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIn("id", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        bm_dict = bm.to_dict()
        self.assertIn("name", bm_dict)
        self.assertIn("my_number", bm_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = dt
        bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == '__main__':
    unittest.main()
