import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up a Review instance for testing."""
        self.review = Review()

    def test_inheritance(self):
        """Test that Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Test that the Review class has all the specified attributes."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')

    def test_place_id_assignment(self):
        """Test assigning a value to the 'place_id' attribute."""
        self.review.place_id = '12345'
        self.assertEqual(self.review.place_id, '12345')

    def test_to_dict_method(self):
        """Test the 'to_dict' method for creating a dict. representation."""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("id", review_dict)


if __name__ == '__main__':
    unittest.main()
