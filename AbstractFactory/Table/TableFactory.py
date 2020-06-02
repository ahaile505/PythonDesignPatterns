
from .BigTable import BigTable
from .MediumTable import MediumTable
from .SmallTable import SmallTable


class TableFactory:  # pylint: disable=too-few-public-methods
    """Tha Factory Class"""

    @staticmethod
    def get_table(table):
        """A static method to get a table"""
        try:
            if table == "BigTable":
                return BigTable()
            if table == "MediumTable":
                return MediumTable()
            if table == "SmallTable":
                return SmallTable()
            raise AssertionError("Table Not Found")
        except AssertionError as _e:
            print(_e)
        return None


# if __name__ == "__main__":
#     TABLE = TableFactory().get_table("SmalTable")
#     print(TABLE)