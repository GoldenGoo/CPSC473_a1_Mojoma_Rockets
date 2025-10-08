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
    c_table:dict[frozenset, int] = {}
    for transaction in data.transactions:
        for item in transaction:
            key = frozenset([item])
            c_table[key] = c_table.get(key, 0) + 1
    #print(f"Initial C0 table is: \n{c_table}")
    l_table: dict[frozenset, int] = {}
    l_table = make_l_table(c_table) # initialize the first l table

    while (len(l_table)>1): 
        c_table = make_c_table(l_table)
        l_table = make_l_table(c_table)

        
def make_c_table(l_table:dict[frozenset, int]):
    c_table: dict[frozenset, int] = {}
    flag: bool = False
    for item_1 in l_table:
        flag = False
        for item_2 in l_table:
            if (flag):
                key = item_1.union(item_2)
                if (len(key) == len(item_1)+1):
                    c_table[key] = 0  
            if (item_1 == item_2):
                flag = True
    if(len(c_table)>0):
        c_table = fill_c_table(c_table)
        return c_table


def fill_c_table(c_table:dict[frozenset, int]):
    for key in c_table:
        for transaction in data.transactions:
            interesect = key.intersection(transaction)
            if (len(key) == len(interesect)):
                c_table[key] = c_table.get(key) + 1
    #print(f"c table is \n{c_table}") 

    return c_table

def make_l_table(c_table:dict[frozenset, int]):
    l_table: dict[frozenset, int] = {}
    for item in c_table:
        if (c_table[item] >= min_sup):
            l_table[item] = c_table[item]
    #print(f"l table is \n{l_table}")

    global frequent_patterns
    frequent_patterns.update(l_table)

    return l_table

def main():
    global data 
    data = Database(file_name)
    global min_sup
    min_sup = int(data.size * sup_percent) #amount of items * sup_percent -> MST
    #print(f"initial min sup is: \n{min_sup}")
    apriori()
    global frequent_patterns
    print("The frequent patterns are: \n ------------------------")
    print(f" |FPs| = {len(frequent_patterns)}")
    for elem in frequent_patterns:
        print(f"{set(elem)} : {frequent_patterns[elem]}")

if __name__ == "__main__":
        main()
