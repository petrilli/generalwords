#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_generalwords
----------------------------------

All the tests for the generalword module. Simple module, simple tests.
"""

import unittest

from generalwords import get_word


class TestGeneralwords(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_word(self):
        self.assertIsNotNone(get_word())

    def test_get_word_is_somewhat_random(self):
        sample_size = 100
        words = set(get_word() for i in range(sample_size))
        self.assertAlmostEqual(len(words), sample_size,
                               delta=int((sample_size * 0.1)))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
