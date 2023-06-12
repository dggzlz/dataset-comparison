#I/O file
#import pandas as pd 

DATASET = {"dataset 1" : "dataset1.csv",
           "dataset 2" : "dataset2.csv"}

def get_list(file : str) -> list:
    """
    It gets the file (as excel format) and converts it into a 2D-list and it returns that list

    Arguments:

    (str) file - file that we are taking the data from

    Returns:
    (list) excel list - a 2D list with all the info from the data set
    """
    dataset = []

    for cell in file:
        row = cell.strip().replace(',', ' ').split()
        dataset.append(row)

    return dataset 

def write_dataset()->None:
    
    file_reader = open(r'dataset.csv', 'w')
    file_reader.write()
    file_reader.close()

def open_file() -> list:    
    
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
    
    return get_list(file_reader)
        
def main()->None:
    dataset1 = open_file()
    dataset2 = open_file()
    print(dataset1)
    print(dataset2)
main()