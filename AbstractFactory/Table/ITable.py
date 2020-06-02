from abc import ABCMeta, abstractstaticmethod


class ITable(metaclass=ABCMeta): 
    """The Table Interface"""

    @abstractstaticmethod
    def dimensions():
        """Get the table dimensions"""