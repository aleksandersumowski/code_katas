import unittest
import ipdb
from chop import chop

class tests(unittest.TestCase):
    def test_returns_minus_one_when_array_empty(self):
        self.assertEquals(chop(2,[]),-1)
    def test_returns_zero_when_only_number(self):
        self.assertEquals(chop(2,[2]),0)
    def test_returns_minus_one_when_not_single_element(self):
        self.assertEquals(chop(2, [3]), -1)
    def test_returns_minus_one_when_not_present(self):
        self.assertEquals(chop(2, [1,3,4,5,5,5,5,5,56]), -1)
    def test_returns_position_when_prestn(self):
        self.assertEquals(chop(2, [1,2]), 1)
    def test_returns_positions_one(self):
        self.assertEquals(chop(1, [1, 3, 5]), 0)
    def test_returns_positions_two(self):
        self.assertEquals(chop(3, [1, 3, 5]), 1)
    def test_returns_positions_three(self):
        self.assertEquals(chop(5, [1, 3, 5]), 2)
        self.assertEquals(chop(1, [1, 2, 3, 4, 5]), 0)
        self.assertEquals(chop(2, [1, 2, 3, 4, 5]), 1)
        self.assertEquals(chop(3,  [1, 2, 3, 4, 5]), 2)
        self.assertEquals(chop(4, [1, 2, 3, 4, 5]), 3)
        self.assertEquals(chop(5,  [1, 2, 3, 4, 5]), 4)
        self.assertEquals(chop(3, [1, 2, 3, 4, 5, 6]), 2)
        self.assertEquals(chop(5, [1, 2, 3, 4, 5, 6]), 4)

