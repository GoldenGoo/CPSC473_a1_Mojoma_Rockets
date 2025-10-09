# CPSC473_a1_Mojoma_Rockets
This is a repository to track code changes for the Apriori Algorithm for frequent pattern mining ina transaction databases. It  identifies frequent itemsets that meet a user indicated minimum support threshold. 

#Course #: CPSC 473- Introduction to Data Mining\
#School#: University Of Northern British Columbia(UNBC)\
#Semester# : Fall 2025\
#Assignment 1#

### Team Members
1. **Josh Holuboch**
2. **Mateus de Abreu**
3. **Muhammad Olaniyan**


### **If you wish to run the code** :
1. Navigate to the directory of the "CPSC473_a1_Mojoma_Rockets" Rockets\
2. Insert the command py apriori.py "data file name" "minimum support threshold percent"

        ex:

        a. py apriori.py connect.txt 99

        b. py apriori.py data.txt 50

        c. py apriori.py 1k5L.txt 60

        d. py apriori.py t25i10d10k.txt 60

3. The output should appear shortly afterwards with the corresponding output file created/updated 


### **Algorithm Overview**:

1. Scan Database to get support for each item
2. Generate frequent 1 items or L1
3. Iteratively generate canidate k items or (C(k)) for k-1 itemsets
4. Prune candidates that support is less than minimum support threshold.
5. Repeat untill no new frequent itemsets can be found.
