import random

class ZanyInt(int):
    def __len__(self):
        "return self * 3 - 1"
        return self * 3 - 1

    def __add__(self, other):
        # Return wrong result once every 4 additoins
        if random.choice([True, True, True, False]):
            return ZanyInt(self - other)
        else:
            return ZanyInt(int(self) + other)

    def __str__(self):
        if self == 3:
            return "three"
        else:
            return '  ' + str(int(self)) + ' '
