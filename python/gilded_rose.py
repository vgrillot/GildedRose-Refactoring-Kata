# -*- coding: utf-8 -*-


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

    def do_update_sell_time(self):
        """object takes age..."""
        self.sell_in -= 1

    def update_quality(self):
        self.do_update_sell_time()
        self.do_update_quality()

    def do_update_quality(self):
        if self.sell_in > 0:
            self.do_update_quality_before_sell()
        else:
            self.do_update_quality_after_sell()
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50

    def do_update_quality_before_sell(self):
        self.quality -= 1

    def do_update_quality_after_sell(self):
        self.quality -= 2


class Item(BaseItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)


class AgedBrieItem(BaseItem):
    def __init__(self, sell_in, quality):
        super().__init__("Ages Brie", sell_in, quality)

    def do_update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1


class SulfurasItem(BaseItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def do_update_quality(self):
        """Sulfuras", being a legendary item, never has to be sold or decreases in Quality"""
        pass


class BackstageItem(BaseItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def do_update_quality(self):
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

    def do_update_quality(self):
        """"Conjured" items degrade in Quality twice as fast as normal items"""
        delta_quality = -2
        if self.sell_in <= 0:
            delta_quality *= 2
        if self.quality > 0:
            self.quality = self.quality + delta_quality
