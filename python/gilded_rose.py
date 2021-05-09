# -*- coding: utf-8 -*-
import abc


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class BaseItem:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @abc.abstractmethod
    def update_quality(self):
        pass


class Item(BaseItem):
    def update_quality(self):
        if self.name != "Aged Brie" and self.name != "Backstage passes to a TAFKAL80ETC concert":
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.name != "Aged Brie":
                if self.quality > 0:
                    if self.name != "Sulfuras, Hand of Ragnaros":
                        self.quality = self.quality - 1
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1


class FooItem(BaseItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        delta_quality = -1
        if self.sell_in <= 0:
            delta_quality *= 2
        if self.quality > 0:
            self.quality = self.quality + delta_quality


class AgedBrieItem(BaseItem):
    def __init__(self, sell_in, quality):
        super().__init__("Ages Brie", sell_in, quality)

    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1


class SulfurasItem(BaseItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """Sulfuras", being a legendary item, never has to be sold or decreases in Quality"""
        pass


class BackstageItem(BaseItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """Sulfuras", being a legendary item, never has to be sold or decreases in Quality"""
        if self.quality < 50:
            self.quality = self.quality + 1
        if self.sell_in < 11:
            if self.quality < 50:
                self.quality = self.quality + 1
        if self.sell_in < 6:
            if self.quality < 50:
                self.quality = self.quality + 1
        if self.sell_in <= 0:
            self.quality = 0


class ConjuredItem(BaseItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """"Conjured" items degrade in Quality twice as fast as normal items"""
        delta_quality = -2
        if self.sell_in <= 0:
            delta_quality *= 2
        if self.quality > 0:
            self.quality = self.quality + delta_quality
