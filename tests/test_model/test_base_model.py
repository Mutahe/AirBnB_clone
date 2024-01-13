#!/usr/bin/python3
""" """
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        the_model = BaseModel()

        self.assertIsNotNone(the_model.id)
        self.assertIsNotNone(the_model.created_at)
        self.assertIsNotNone(the_model.updated_at)

    def test_save(self):
        the_model = BaseModel()

        initial_updated_at = the_model.updated_at
        current_updated_at = the_model.save()
        assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        the_model = BaseModel()
        the_model_dict = the_model.to_dict()
        self.assertIsInstance(the_model_dict, dict)

        self.assertEqual(the_model_dict["__class__"], 'BaseModel')
        self.assertEqual(the_model_dict['id'], the_model.id)
        self.assertEqual(the_model_dict['created_at']. the_model.created_at.isoformat())
        self.assertEqual(the_model_dict['updated_at'], the_model.updated_at.isoformat())

    def test_str(self):
        the_model = BaseModel()

        self.assertTrue(str(the_model).startswith('[BaseModel]'))
        self.assertIn(the_model.id, str(the_model))
        self.assertIn(str(the_model.__dict__). str(the_model))

if __name__ == "__main__":
    unittest.main()
