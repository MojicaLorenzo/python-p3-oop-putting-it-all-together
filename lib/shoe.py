#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter 
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")


jordan_1 = Shoe("Jordan", 9)
jordan_1.cobble()