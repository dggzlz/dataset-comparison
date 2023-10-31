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
        dataset = [] # empty list

        for cell in file:
            line = cell.strip().replace(',', ' ').split()
            dataset.append(_Item(line))

        return dataset
    
    def howMany(self, upc : int) -> int:
        """
        Counts how many times the specified item appears in the list
        
        Args:
        
        (int) upc: Universal Standard Code (UPC) used to mark what product/item is
        
        returns:
        (int) n_item: the count for how many time the item appears in the list.  
        """
        n_item = 0 # Counter
        for i in range(len(self.list)): # iterating through the list 
            if upc == self.list[i].upc:
                n_item += 1
        return n_item
    

    def __search(self, upc: int)-> int:
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
    
    def copy(self, dataset)-> None:
        """
        copy a whole dataset
        """
        new_dataset = []
        for i in range(len(dataset.list)):
            new_dataset.append(dataset.list[i])
        self.list = new_dataset
        
    
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
        (list) item: a list with the information of the item as follows:    
                index 0 -> (int) amount: the amount of the item to be added
                index 1 -> (str) name: name of the item to be added
                index 2 -> (int) UPC: code of the item to be added

        if the item exists then the amount will be added, otherwise it will add it as new item, 
        and sorted by upc by deafult.
        """

        index = self.__search(item[2])
        if index == -1:
            self.list.append(_Item(item))
            self.sort("upc")
        else:
            self.list[index].quantity += item[0]

            
    def remove(self, upc: int):
        """remove by upc"""

        index = self.__search(upc)
        if index == -1:
            print("Item not in the list")
        else:
            self.list.remove(self.list[index])


    def printList(self):
        print(f"{'Quantity':<10}{'Name':<10}{'UPC':<10}")
        for i in range(len(self.list)):
            print(f"{self.list[i].quantity:<10}{self.list[i].name:<10}{self.list[i].upc:<10}")
        #Note: this will become the method to print the data into the file
    
    
    
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

