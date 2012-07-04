#! /usr/bin/env python
import unittest
class Test(unittest.TestCase):
    def test_me(self):
        seq = [ 5, 4, 1, 3, 2 ]
        seq.sort()
        self.assertEqual(seq, [1, 2, 3, 4, 5])

unittest.main()
