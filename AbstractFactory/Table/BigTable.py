
from .ITable import ITable

class BigTable(ITable):
    """The Big Table Concrete Class which implements the ITable interface"""

    def __init__(self):
        self._height = 60
        self._width = 120
        self._depth = 80

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height}
