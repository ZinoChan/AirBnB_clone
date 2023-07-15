#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest for filestorage"""

    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()

    def test_all(self):
        o = BaseModel()
        self.storage.new(o)
        self.assertEqual(
            self.storage.all(), {o.__class__.__name__ + "." + o.id: o})
