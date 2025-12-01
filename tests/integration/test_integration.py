import unittest
from src.matek import Matek

class TestInt(unittest.TestCase):
    def test_tobbszoros_osszeadas(self):
        m = Matek()
        # Ez egy "folyamatot" szimulál: kétszer adunk össze
        elso = m.osszead(1, 1)
        vegso = m.osszead(elso, 1)
        self.assertEqual(vegso, 3)