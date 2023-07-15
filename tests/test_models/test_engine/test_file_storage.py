#!/usr/bin/python3
""" TEST_CASES for FileStrorage class
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Unittest for filestorage"""

    def setUp(self):
        """Setting Instantiation"""
        self.storage = FileStorage()
        self.storage.reload()

    def test_all(self):
        """Testing the all() method"""
        o = BaseModel()
        self.storage.new(o)
        self.assertEqual(
            self.storage.all(), {o.__class__.__name__ + "." + o.id: o})

    def test_new_user(self):
        """Testing the new() method"""
        user = User()
        self.storage.new(user)
        self.assertIn("User." + user.id, self.storage.all())


if __name__ == "__main__":
    unittest.main()
