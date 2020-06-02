from .BigChair import BigChair
from .MediumChair import MediumChair
from .SmallChair import SmallChair


class ChairFactory: 
    """Tha Factory Class"""

    @staticmethod
    def get_chair(chair):
        """A static method to get a table"""
        try:
            if chair == "BigChair":
                return BigChair()
            if chair == "MediumChair":
                return MediumChair()
            if chair == "SmallChair":
                return SmallChair()
            raise AssertionError("Chair Not Found")
        except AssertionError as _e:
            print(_e)
        return None




# if __name__ == "__main__":
#     CHAIR_FACTORY = ChairFactory().get_chair("SmallChair")
#     print(CHAIR_FACTORY.dimensions())