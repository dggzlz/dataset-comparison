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

    excel_list = []

    for cell in file:
        row = cell.strip().replace(',', ' ').split()
        excel_list.append(row)

    return excel_list

def main() -> None:
    
    #filename = input("insert name of file: ")
    
    file_reader = open(r'dataset.csv', 'r')
    elist = get_list(file_reader)
    print(elist)

main()