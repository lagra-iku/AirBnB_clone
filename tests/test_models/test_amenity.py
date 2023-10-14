import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up an Amenity instance for testing."""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test that the Amenity class has the 'name' attribute."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, '')

    def test_name_assignment(self):
        """Test assigning a value to the 'name' attribute."""
        self.amenity.name = 'Swimming Pool'
        self.assertEqual(self.amenity.name, 'Swimming Pool')

    def test_to_dict_method(self):
        """Test the 'to_dict' method for creating a dict. representation."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("__class__", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("id", amenity_dict)


if __name__ == '__main__':
    unittest.main()
