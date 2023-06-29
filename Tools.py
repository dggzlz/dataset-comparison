class DataList:
    def __init__(self, file_name : str) -> None:
        self.list = self.__get_list(file_name)

    
    def __get_list(self, file : str) -> list:
        """
        It gets the file (as excel format) and converts it into a 2D-list and it returns that list

        Arguments:

        (str) file - file that we are taking the data from

        Returns:
        (list) excel list - a 2D list with all the info from the data set
        """
        dataset = []

        for cell in file:
            line = cell.strip().replace(',', ' ').split()
            item = _Item(line)
            dataset.append(item)

        return dataset
    
    def howMany(self, upc : int) -> int:
        """
        Counts how many times the specified item appears in the list
        """
        n_item = 0
        # note: think about a method that will search for you, 
        # since you're gonna use it many times
        for i in range(len(self.list)):
            if upc == self.list[i].upc:
                n_item += 1
        return n_item
    #Note: is this function neccesary?


    def search(self, upc: int):
        """
        Searchs for an spicific item in the dataset and return the place where it is
        """
        found = False
        for i in range(len(self.list)):
            if upc == self.list[i].upc:
                found = True
                index = i
                break
        
        if not found:
            return -1
        else:
            return index
    
    # def difference(self, obj: object) -> int:
    #     """
    #     says how much difference is there between lists by items
    #     """
    #     return
    
    def copy(self):
        """
        copy a whole dataset
        """
        return
    
    def sort(self, sort_by: str)-> None:
        """
        Sorts the dataset depending on user's choice.
        
        Argument:
        (str) sort_by: choice of the user. parameter should equal quantity, name, or upc
        otherwise it won't sort the list.
        """
        if sort_by == "quantity":
            self.list.sort(key=lambda obj: obj.quantity)
        elif sort_by == "name":
            self.list.sort(key=lambda obj: obj.name)
        elif sort_by == "upc":
            self.list.sort(key=lambda obj: obj.upc)
        else:
            print("Could not sort by this argument")
    

    def getSize(self) -> int:
        """
        returns the amount of items in the list
        """
        return len(self.list)
    
    def addItem(self, item: list):
        """
        It adds the specified item and sorts it in the list.

        Arguments:
        (int) amount: the amount of the item to be added
        (str) name: name of the item to be added
        (int) UPC: code of the item to be added

        if the item exists then the amount will be added, otherwise it will add it as new item, 
        and sorted by upc by deafult.
        """
        # found = False
        # for i in range(len(self.list)):
        #     if item[2] == self.list[i].upc:
        #         self.list[i].quantity += item[0]
        #         found = True
        #         break

        index = self.search(item[2])
        if index == -1:
            self.list.append(_Item(item))
            self.sort("upc")
        else:
            self.list[index].quantity += item[0]

            
    def remove(self, upc: int):
        """remove by upc"""
        # found = False
        # for i in range(len(self.list)):
        #     if upc == self.list[i].upc:
        #         self.list.remove(self.list[i])
        #         found = True
        #         break
        index = self.search(upc)
        if index == -1:
            print("Item not in the list")
        else:
            self.list.remove(self.list[index])

        

    
    def printList(self):
        print(f"{'Quantity':<10}{'Name':<10}{'UPC':<10}")
        for i in range(len(self.list)):
            print(f"{self.list[i].quantity:<10}{self.list[i].name:<10}{self.list[i].upc:<10}")
    
    
    
    # overloaded operators
    def __gt__(self, obj): # greater than
        return (len(self.list) > len(obj.list))
    
    def __lt__(self, obj): # less than
        return (len(self.list) < len(obj.list))
    
    def __le__(self, obj): # less or equal to
        return (len(self.list) < len(obj.list)) or (len(self.list) == len(obj.list))

    def __ge__(self, obj): # greater or equal to
        return (len(self.list) > len(obj.list)) or (len(self.list) == len(obj.list))

    def __eq__(self, obj): # equal to
        return len(self.list) == len(obj.list)
    
    def __ne__(self, obj): # not equal to
        return len(self.list) != len(obj.list)
    
class _Item:
    def __init__(self, item: list) -> None:
        self.quantity = int(item[0])
        self.name = item[1]
        self.upc = int(item[2])

