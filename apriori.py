import sys
from database import Database

file_name = sys.argv[1] #this is the file path we will be opening
sup = sys.argv[2] #minimum support
sup_percent = sup/100

# file = open(file_name) #this is the actual file that will be used

#amount of items * sup_percent -> MST
def main():
    data = Database(file_name)