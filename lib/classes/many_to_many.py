class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        elif hasattr(self, "name"):
            raise Exception("Name can't be changed")
        elif len(name) < 3:
            raise Exception("Name must be at least 3 characters")
        else:
            self._name = name

        # if isinstance(name, str) and len(name) > 2 and not hasattr(self, "name"):
        #     self._name = name

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list(
            set([order.customer for order in Order.all if order.coffee is self])
        )

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        total = 0
        for order in self.orders():
            total += order.price
        return total / self.num_orders()


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list(
            set([order.coffee for order in Order.all if order.customer is self])
        )

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 16):
            self._name = name

    @classmethod
    def most_aficionado(cls, coffee):
        max_total = 0
        most = None
        for customer in cls.all:
            cust_total = sum(
                [order.price for order in customer.orders() if order.coffee is coffee]
            )
            if cust_total > max_total:
                max_total = cust_total
                most = customer
        return most


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (
            isinstance(price, float)
            and 1.0 <= price <= 10.0
            and not hasattr(self, "price")
        ):
            self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
