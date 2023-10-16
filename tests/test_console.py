import os
import sys
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommandMethods(unittest.TestCase):
    def test_do_create(self):
        """Test the 'create' command in the console."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            created_output = output.getvalue().strip()
            self.assertIn("created", created_output)

    def test_do_show(self):
        """Test the 'show' command in the console."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
            shown_output = output.getvalue().strip()
            self.assertIn("BaseModel", shown_output)

    def test_do_destroy(self):
        """Test the 'destroy' command in the console."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
            destroyed_output = output.getvalue().strip()
            self.assertIn("BaseModel", destroyed_output)

    def test_do_update(self):
        """Test the 'update' command in the console."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel 1 name 'NewName'")
            update_output = output.getvalue().strip()
            self.assertIn("BaseModel", update_output)

    def test_do_count(self):
        """Test the 'count' command in the console."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("count BaseModel")
            count_output = output.getvalue().strip()
            self.assertEqual(count_output, '1')
