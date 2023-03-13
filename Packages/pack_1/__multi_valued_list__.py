class Detector(object):
    def __init__(self, name, listData, dictData):
        # instances
        self.name = name
        self.list1 = listData
        self.dict1 = dictData

    def __repr__(self) -> str:
        """
        Return a string to display all the details of a instance
        """
        return f"Name : {self.name}\nList = {self.list1}\nDict = {self.dict1}\n"

    def __len__(self) -> int:
        """
        Return an integer of length of both list and dict
        """
        return len(self.list1) + len(self.dict1)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        new_list = []
        if self.i < len(self.list1):
            list_sum = self.list1[self.i]
            self.i += 1
            new_list.append(list_sum)
        else:
            raise StopIteration
        
        return sum(new_list)

    def searchValue(self) -> None:
        pass

    def saveValue(self) -> None:
        pass

    def deleteValue(self) -> None:
        pass


# person_1 = Detector("Bhupender", [10, 20, 30], {"A": 1, "B": 2})
# print(person_1)
# print("Total Length :", len(person_1), "\n")
# print("Sum of List :", sum(person_1))