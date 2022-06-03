import os
from pydoc import describe 
import shutil
source=input("enter source folder name =")
destination=input("enter the final postion of file=")
source=source+"/"
destination=destination+"/"
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)
