#!/usr/bin/env python
# encoding: utf-8

import unittest
import foo

class SimpleTest(unittest.TestCase):

    def test1(self):
        """TODO: Docstring for tset1.
        :returns: TODO

        """
        self.assertEqual(foo.divide(2,2),1)

    def test2(self):
        """TODO: Docstring for test2.
        :returns: TODO

        """
        self.assertSetEqual(foo.divide(2,1), 2)

if __name__ == "__main__":
    unittest.main()




