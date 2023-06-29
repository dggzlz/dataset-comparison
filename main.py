#I/O file
#import pandas as pd 
from Tools import DataList

DATASET = {"dataset 1" : "dataset1.csv",
           "dataset 2" : "dataset2.csv"}

def open_file() -> str:    
        
        while True:
            filename = input("Select csv file: ")
            try:
                file_reader = open(fr'{filename}', 'r')
                break
            except FileNotFoundError:
                print("File not found. please select a valid file.")
            except FileExistsError:
                print("An error ocurred with the file selected. Try again.")
            except:
                print("Could not open. Try again.")
        
        return file_reader

def write_dataset()->None:
    
    file_reader = open(r'dataset.csv', 'w')
    file_reader.write()
    file_reader.close()

        
def main()->None:

    dataset1 = DataList(open_file())
    #dataset2 = DataList(open_file())
    # print(dataset1.list)
    # print(f"is dataset 1 greater than dataset 2?: {dataset1 > dataset2}")
    # print(dataset2.list)
    #print(f"the size of dataset 1 is {dataset1.getSize()}")

    #dataset1.howMany(100005)
    # dataset1.sort("last name")
    # dataset1.getSize()
    dataset1.addItem([2,"dareen", 10000])
    dataset1.remove(100000001)
    dataset1.printList()
main()