#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self._size = size
        self.price = price
    
    @property
    def size(self):
        """Get size property"""
        return self._size
    
    @size.setter
    def size(self, size):
        """Size musr be small, medium, or large"""
        if size in ["Small, Medium", "Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1