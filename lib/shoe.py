#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand) -> None:
        self.brand = brand

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")
            self._size = False

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    size = property(get_size, set_size,)