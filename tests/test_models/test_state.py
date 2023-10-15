import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up a State instance for testing."""
        self.state = State()

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test that the State class has the 'name' attribute."""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, '')

    def test_name_assignment(self):
        """Test assigning a value to the 'name' attribute."""
        self.state.name = 'California'
        self.assertEqual(self.state.name, 'California')

    def test_to_dict_method(self):
        """Test the 'to_dict' method for creating a dict representation."""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("__class__", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("id", state_dict)


if __name__ == '__main__':
    unittest.main()
