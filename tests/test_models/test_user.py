import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up a User instance for testing."""
        self.user = User()

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test that the User class has all the specified attributes."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_email_assignment(self):
        """Test assigning a value to the 'email' attribute."""
        self.user.email = 'test@example.com'
        self.assertEqual(self.user.email, 'test@example.com')

    def test_to_dict_method(self):
        """Test the 'to_dict' method for creating a dict. representation."""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("id", user_dict)


if __name__ == '__main__':
    unittest.main()
