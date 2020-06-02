from abc import abstractstaticmethod, ABCMeta


class IFurnitureFactory(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """Furniture Factory Interface"""

    @abstractstaticmethod
    def get_furniture(furniture):
        """The static funiture factory inteface method"""