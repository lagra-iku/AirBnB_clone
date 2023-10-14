import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.base_model = BaseModel()

    def test_id_generation(self):
        """Test that a unique ID is generated for each BaseModel instance."""
        base_model2 = BaseModel()
        self.assertNotEqual(self.base_model.id, base_model2.id)

    def test_created_at_type(self):
        """Test that the 'created_at' attribute is a datetime object."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        """Test that the 'updated_at' attribute is a datetime object."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        """Test that the 'save' method updates the 'updated_at' attribute."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test the 'to_dict' method for creating a dict.representation."""
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("id", model_dict)

    def test_str_method(self):
        """Test the string representation of the BaseModel instance."""
        model_str = str(self.base_model)
        self.assertIn(self.base_model.__class__.__name__, model_str)
        self.assertIn(self.base_model.id, model_str)


if __name__ == '__main__':
    unittest.main()
