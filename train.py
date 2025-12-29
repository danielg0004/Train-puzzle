import random

class Train:
    def __init__(self, n=None, on_probability=0.5):
        if n is None:
            n = random.randint(1, 100) # Random length if none given
        
        self._lights = random.choices([True, False], weights=[on_probability, 1-on_probability], k=n)
        self._pos = 0
    
    def move_forward(self):
        self._pos += 1
        self._pos %= len(self._lights)
    
    def move_backward(self):
        self._pos -= 1
        self._pos %= len(self._lights)
    
    def read_light(self):
        return self._lights[self._pos]
    
    def switch_light(self):
        self._lights[self._pos] = not self._lights[self._pos]
    
    # These two are for convinience
    def turn_off(self):
        self._lights[self._pos] = False
    
    def turn_on(self):
        self._lights[self._pos] = True