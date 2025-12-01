import unittest
from src.matek import Matek

class TestUnit(unittest.TestCase):
    def test_siman_osszead(self):
        m = Matek()
        self.assertEqual(m.osszead(1, 1), 2)