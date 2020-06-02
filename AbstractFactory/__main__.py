from FurnitureFactory.FurnitureFactory import FurnitureFactory



def main():


    FURNITURE = FurnitureFactory.get_furniture("SmallChair")
    print(f"{FURNITURE.__class__} : {FURNITURE.dimensions()}")

    # FURNITURE = FurnitureFactory.get_furniture("MediumTable")
    # print(f"{FURNITURE.__class__} : {FURNITURE.dimensions()}")





if __name__ == '__main__':
    main()