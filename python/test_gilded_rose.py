# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, AgedBrieItem, SulfurasItem, BackstageItem, ConjuredItem


class GildedRoseTest(unittest.TestCase):

    def assertGildedRoseItem(self, item, expected_quality, nb_days=1):
        """run quality test on one item"""
        self.assertIsNotNone(item, "Item is mandatory for test")
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)
        self.assertEquals(expected_quality, items[0].quality)
        return item

    def test_foo_ager(self):
        """ensure  item age change"""
        item = self.assertGildedRoseItem(
            Item("foo", 10, 5),
            4)
        self.assertEquals(9, item.sell_in)

    def test_foo_not_passed(self):
        """a not passed item has -1 quality / day"""
        self.assertGildedRoseItem(
            Item("foo", 10, 5),
            4)

    def test_foo_not_passed(self):
        """a not passed item has -1 quality / day"""
        self.assertGildedRoseItem(
            Item("foo", 10, 5),
            4)

    def test_foo_passed(self):
        """a passed item has double decrease quality / day, -2 for standard item"""
        self.assertGildedRoseItem(
            Item("foo", -1, 5),
            3)

    def test_dex_vest(self):
        self.assertGildedRoseItem(
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            19)

    def test_aged_brie(self):
        """"Aged Brie" actually increases in Quality the older it gets"""
        self.assertGildedRoseItem(
            AgedBrieItem(sell_in=2, quality=0),
            1)

    def test_mongoose_elixir(self):
        self.assertGildedRoseItem(
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            6)

    def test_suluras(self):
        """"Sulfuras", being a legendary item, never has to be sold or decreases in Quality"""
        self.assertGildedRoseItem(
            SulfurasItem(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            80)

    def test_backstage_15days(self):
        """"Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;"""
        self.assertGildedRoseItem(
            BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            21)

    def test_backstage_10days_max50(self):
        """Quality increases by 2 when there are 10 days or less"""
        self.assertGildedRoseItem(
            BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            50)

    def test_backstage_5days_max50(self):
        """and by 3 when there are 5 days or less"""
        self.assertGildedRoseItem(
            BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            50)

    def test_backstage_10days(self):
        """Quality increases by 2 when there are 10 days or less"""
        self.assertGildedRoseItem(
            BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10),
            12)

    def test_backstage_5days(self):
        """and by 3 when there are 5 days or less"""
        self.assertGildedRoseItem(
            BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10),
            13)

    def test_backstage_0(self):
        """Quality drops to 0 after the concert"""
        self.assertGildedRoseItem(
            BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=49),
            0)

    def test_conjured_mana_cake(self):
        self.assertGildedRoseItem(
            ConjuredItem(name="Conjured Mana Cake", sell_in=3, quality=6),
            4)


if __name__ == '__main__':
    unittest.main()
