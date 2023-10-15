import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up a City instance for testing."""
        self.city = City()

    def test_inheritance(self):
        """Test that City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test that the City class has the 'state_id' and 'name' attributes."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')

    def test_state_id_assignment(self):
        """Test assigning a value to the 'state_id' attribute."""
        self.city.state_id = 'TX'
        self.assertEqual(self.city.state_id, 'TX')

    def test_name_assignment(self):
        """Test assigning a value to the 'name' attribute."""
        self.city.name = 'Austin'
        self.assertEqual(self.city.name, 'Austin')

    def test_to_dict_method(self):
        """Test the 'to_dict' method for creating a dict.  representation."""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("__class__", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("id", city_dict)


if __name__ == '__main__':
    unittest.main()
