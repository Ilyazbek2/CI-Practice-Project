import unittest
import os
from pathlib import Path

from head_file import head_file


class TestHeadFile(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path("tests/tmp")
        self.test_dir.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        for file in self.test_dir.glob("*"):
            file.unlink()

    def test_empty_file(self):
        path = self.test_dir / "empty.txt"
        path.write_text("")
        result = head_file(str(path))
        self.assertEqual(result["status"], 200)
        self.assertTrue(result["is_text"])
        self.assertEqual(result["content"], "")

    def test_missing_file(self):
        path = self.test_dir / "missing.txt"
        result = head_file(str(path))
        self.assertEqual(result["status"], 404)

    def test_binary_file(self):
        path = self.test_dir / "binary.bin"
        path.write_bytes(b"\x00\x01\x02\x03")
        result = head_file(str(path))
        self.assertEqual(result["status"], 200)
        self.assertFalse(result["is_text"])
        self.assertEqual(result["content"], "<binary>")

    def test_text_file(self):
        path = self.test_dir / "hello.txt"
        path.write_text("Hello, world!")
        result = head_file(str(path))
        self.assertEqual(result["status"], 200)
        self.assertTrue(result["is_text"])
        self.assertIn("Hello", result["content"])

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            head_file(123)  # передаём не строку
