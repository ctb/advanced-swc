#! /usr/bin/env python
import unittest
import random

class Test(unittest.TestCase):
    def setUp(self):
        self.seq = range(0, 10)
        random.shuffle(self.seq)

    def tearDown(self):
        del self.seq

    def test_basic_sort(self):
        self.seq.sort()
        self.assertEqual(self.seq, range(0, 10))

    def test_reverse(self):
        self.seq.sort()
        self.seq.reverse()
        self.assertEqual(self.seq, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_destruct(self):
        self.seq.sort()
        del self.seq[-1]
        self.assertEqual(self.seq, range(0, 9))

unittest.main()
