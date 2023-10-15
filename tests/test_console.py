import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for the HBNBCommand class in console.py.
    """

    def setUp(self):
        """
    Set up a clean HBNBCommand instance before each test.
    """
        self.console = HBNBCommand()

    def tearDown(self):
        """
    Clean up and remove the HBNBCommand instance after each test.
    """
        self.console = None

    def test_create(self):
        """
    Test the 'create' command to create an instance and check the output.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        """
        Test the 'show' command to show an instance and check the output.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            self.assertTrue(len(created_output) > 0

            with patch('sys.stdout', new_callable=StringIO) as mock_stdout_show:
                cmd = f"show BaseModel {created_output}"
                self.console.onecmd(cmd)
                show_output = mock_stdout_show.getvalue().strip()
                self.assertEqual(show_output, str(eval(show_output)))

    def test_destroy(self):
        """
        Test the 'destroy' command to delete an instance and check the output.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            self.assertTrue(len(created_output) > 0

            with patch('sys.stdout', new_callable=StringIO) as mock_stdout_destroy:
                cmd = f"destroy BaseModel {created_output}"
                self.console.onecmd(cmd)
                destroy_output = mock_stdout_destroy.getvalue().strip()
                self.assertEqual(destroy_output, "")

    def test_all(self):
        """
        Test the 'all' command to list instances and check the output.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            all_output = mock_stdout.getvalue().strip()
            self.assertTrue(len(all_output) == 0)

    def test_update(self):
        """
        Test the 'update' command to modify an instance and check the output.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            self.assertTrue(len(created_output) > 0

            with patch('sys.stdout', new_callable=StringIO) as mock_stdout_update:
                cmd = f"update BaseModel {created_output} name 'New Name'"
                self.console.onecmd(cmd)
                update_output = mock_stdout_update.getvalue().strip()
                self.assertEqual(update_output, "")

    def test_count(self):
        """
        Test the 'count' command to count instances and check the output.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            cmd = "count BaseModel"
            self.console.onecmd(cmd)
            count_output = mock_stdout.getvalue().strip()
            self.assertTrue(count_output.isdigit())


if __name__ == '__main':
    unittest.main()
