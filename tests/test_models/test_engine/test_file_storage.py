import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the FileStorage instance and test data."""
        self.file_storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.save()
        self.file_path = "file.json"

    def tearDown(self):
        """Remove the test file created during the tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """Test the 'all' method to return a dictionary of objects."""
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn(
            f"{self.base_model.__class__.__name__}.{self.base_model.id}",
            all_objects
        )

    def test_new_method(self):
        """Test the 'new' method to add objects to the dictionary."""
        new_base_model = BaseModel()
        self.file_storage.new(new_base_model)
        all_objects = self.file_storage.all()
        self.assertIn(
            f"{new_base_model.__class__.__name__}.{new_base_model.id}",
            all_objects
        )

    def test_save_method(self):
        """Test the 'save' method to serialize objects to a JSON file."""
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_method(self):
        """Test the 'reload' method to deserialize objects from a JSON file"""
        self.file_storage.save()
        self.file_storage.reload()
        all_objects = self.file_storage.all()
        self.assertIn(
            f"{self.base_model.__class__.__name__}.{self.base_model.id}",
            all_objects
        )


if __name__ == '__main__':
    unittest.main()
