import unittest
from main import k
import math

class TestSum(unittest.TestCase):

    def test_k(self):
        self.assertAlmostEquals(k(1),2.7553832111)