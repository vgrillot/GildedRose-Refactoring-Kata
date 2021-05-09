# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def assertGildedRoseItem(self, item, expected_quality, nb_days=1):
        """run quality test on one item"""
        self.assertIsNotNone(item, "Item is mandatory for test")
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(expected_quality, items[0].quality)

    def test_foo(self):
        self.assertGildedRoseItem(
            Item("foo", 0, 0),
            0)


if __name__ == '__main__':
    unittest.main()
