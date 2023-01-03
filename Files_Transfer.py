""" Create a python project using OS module to fetch all the excel files from one folder and move 
    it to new folder named excel_files
    """

#import modules
from pathlib import Path
import pandas as pd
import glob
import os
import shutil

def check(n,path):
    if(n == 1):
        filenames = glob.glob(path + "\*.xlsx")
        print('File names:', filenames)
    elif(n == 2):
        filenames = glob.glob(path + "\*.docx")
        print('File names:', filenames)
    elif(n == 3):
        filenames = glob.glob(path + "\*.pdf")
        print('File names:', filenames)
    else:
        print("invalid input")
        exit(0)
    return filenames

# path of the folder
p = input("Enter the path where the files are present: ")
path = p
  
# reading all the files
n = int(input("1. For EXCEL files\n2. For WORD files\n3. For PDF files\nEnter: "))
filenames = check(n,path)

# Make of new Directory 
directory = input("Enter the new of the new folder: ")
    
# Parent Directory path 
parent_dir = input("Enter the Parent Directory where you want to make the folder: ")
    
# Path 
path = os.path.join(parent_dir, directory) 
    
# Creating the directory 
os.mkdir(path) 
print("Directory '% s' created" % directory) 

target = parent_dir+"\\"+directory

# to iterate excel file one by one 
# inside the folder
for f in filenames:
    shutil.move(os.path.join(path,f),target)

print("Mission Successful")
  

