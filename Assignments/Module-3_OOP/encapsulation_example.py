class Computer:
    def __init__(self):
        # Private variable (prefixed with __)
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    # Setter method to modify private variable
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# Trying to change the price directly (will not work because it's private)
c.__maxprice = 1000
c.sell()

# Using setter function to change the price
c.setMaxPrice(1000)
c.sell()
