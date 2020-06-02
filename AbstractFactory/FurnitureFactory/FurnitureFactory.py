from Chair.ChairFactory import ChairFactory
from Table.TableFactory import TableFactory

from .IFurnitureFactory import IFurnitureFactory




class FurnitureFactory(IFurnitureFactory):  # pylint: disable=too-few-public-methods
    """The Furniture Factory Concrete Class"""

    @staticmethod
    def get_furniture(furniture):
        """Static get_furniture method"""
        try:
            if furniture in ["SmallChair", "MediumChair", "BigChair"]:
                return ChairFactory().get_chair(furniture)
            if furniture in ["SmallTable", "MediumTable", "BigTable"]:
                return TableFactory().get_table(furniture)
            raise AssertionError("No Furniture Factory Found")
        except AssertionError as _e:
            print(_e)
        return None