from abc import ABC, abstractmethod


class Adapter(ABC):

    @abstractmethod
    def get_price(self, product):
        pass


class LuckycosmeticAdapter(Adapter):
    name = "luckycosmetic"

    def get_price(self, product):
        test_products = {"shower gel Dove": 300,
                         "mask Loreal": 200,
                         "lip balm Papaya": 500}
        for k, v in test_products.items():
            if k == product:
                return v, self.name


class MykoreashopsAdapter(Adapter):
    name = "mykoreashops"

    def get_price(self, product):
        test_products = {"shower gel Dove": 100,
                         "mask Loreal": 1}
        for k, v in test_products.items():
            if k == product:
                return v, self.name


class HolyyskinAdapter(Adapter):
    name = "holyyskin"

    def get_price(self, product):
        test_products = {"shower gel Dove": 400}
        for k, v in test_products.items():
            if k == product:
                return v, self.name


class NewAdapter(Adapter):
    name = "new"

    def get_price(self, product):
        test_products = {"lip balm Papaya": 500,
                         "shower gel Dove": 800}
        for k, v in test_products.items():
            if k == product:
                return v, self.name


class Aggregator:
    ad = (LuckycosmeticAdapter(), MykoreashopsAdapter(),
          HolyyskinAdapter(), NewAdapter())

    def compare_prices(self, product):
        for i in self.ad:
            if i.get_price(product):
                k = i.get_price(product)
                print(k[1], "-", k[0])


w = Aggregator()
w.compare_prices("mask Loreal")
