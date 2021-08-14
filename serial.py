"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        'Setup starting number for this instance.'
        self.init_num = start
        self.num = start

    def generate(self):
        num = self.num
        self.num += 1
        return num
    
    def reset(self):
        self.num = self.init_num
