import sys
from database import Database

file_name = sys.argv[1] #this is the file path we will be opening
sup = int(sys.argv[2]) #minimum support
sup_percent = sup/100
min_sup = 0
data:Database
frequent_patterns:dict ={}

# file = open(file_name) #this is the actual file that will be used

def apriori():
    
    # initializes the C0 table 
    c_table:dict = {}
    for transaction in data.transactions:
        for item in transaction:
            c_table[item] = c_table.get(item, 0) + 1
    
    make_l_table(c_table) # should recurse back and forth, updating our solution.

        
def make_c_table(l_table:dict):
    c_table: dict = {}
    flag: bool = False
    for item_1 in l_table:
        flag = False
        for item_2 in l_table:
            if (flag):
                key = set(item_1).union(set(item_2))
                key_string= "".join(list(key))
                if (len(key_string) == len(item_1)+1):
                    c_table[key_string] = 0  
            if (item_1 == item_2):
                flag = True

    fill_c_table(c_table)


def fill_c_table(c_table:dict):
    for key in c_table:
        for transaction in data.transactions:
            interesect = set(key) & set(transaction)
            if (len(set(key)) == len(interesect)):
                c_table[key] = c_table.get(key) + 1
    print(f"c table is \n{c_table}") 

    make_l_table(c_table)

def make_l_table(c_table:dict):
    l_table: dict = {}
    for item in c_table:
        if (c_table[item] >= min_sup):
            l_table[item] = c_table[item]
    print(f"l table is \n{l_table}")

    global frequent_patterns
    frequent_patterns.update(l_table)

    if (len(l_table)>1):
        make_c_table(l_table)

def main():
    global data 
    data = Database(file_name)
    global min_sup
    min_sup = int(data.size * sup_percent) #amount of items * sup_percent -> MST
    apriori()
    global frequent_patterns
    print(f"\nThe frequent patterns are {frequent_patterns}")

if __name__ == "__main__":
        main()


#def generate_c_table(l_table:list):

