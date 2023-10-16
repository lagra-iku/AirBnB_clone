import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommandMethods(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_do_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.do_EOF(""))
            self.assertEqual("", output.getvalue())

    def test_do_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.do_quit(""))
            self.assertEqual("", output.getvalue())

    def test_emptyline(self):
        """Test emptyline method."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.emptyline()
            self.assertEqual("", output.getvalue())

    def test_do_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_create("BaseModel")
            created_output = output.getvalue()
            self.assertIn("created", created_output)
            self.assertIn("BaseModel", created_output)

    def test_do_show(self):
        """Test show command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_show("BaseModel 1234-5678")
            shown_output = output.getvalue()
            self.assertIn("BaseModel", shown_output)
            self.assertIn("1234-5678", shown_output)

    def test_do_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_destroy("BaseModel 1234-5678")
            destroyed_output = output.getvalue()
            self.assertIn("BaseModel", destroyed_output)
            self.assertIn("1234-5678", destroyed_output)

    def test_do_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_all("BaseModel")
            all_output = output.getvalue()
            self.assertIn("BaseModel", all_output)

    def test_do_update(self):
        """Test update command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_update("BaseModel 1234-5678 attribute value")
            update_output = output.getvalue()
            self.assertIn("BaseModel", update_output)
            self.assertIn("1234-5678", update_output)
            self.assertIn("attribute", update_output)
            self.assertIn("value", update_output)

    def test_do_count(self):
        """Test count command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.do_count("BaseModel")
            count_output = output.getvalue()
            self.assertIn("BaseModel", count_output)


if __name__ == '__main__':
    unittest.main()

