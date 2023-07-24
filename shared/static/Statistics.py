class Statistics:
    def __init__(self, measurements):
        self._measurements = measurements

    def average(self):
        """Compute the average of a list of values"""
        return sum(self._measurements)/len(self._measurements)

    def median(self):
        """Compute the median of a list of values.
        See https://en.wikipedia.org/wiki/Median"""
        index = len(self._measurements)//2
        return self._measurements[index]
