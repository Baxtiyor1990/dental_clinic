
import unittest
from dental_clinic.main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(-3, 3), 0)

if __name__ == '__main__':
    unittest.main()
