class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

building1 = Building(5, "Residential")
building2 = Building(5, "Office")

if building1 == building2:
    print("Оба здания имеют одинаковое количество этажей и тип")
else:
    print("Здания различаются по этажности или типу")