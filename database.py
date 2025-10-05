# This is the object class used to store the transaction database
# information in a workable format.

class database:

    # Initializes the database object to have 2 variables, size and a transaction list.
    # Requires a filepath on initialization.
    def __init__(self, file_path):
        try:
            with open (file_path, 'r') as file: 
                self.size = file.readline()
                for line in file:
                    components = line.split # gets an array of the line, split on spaces
                    index = [components[0]-1]#components[0] is the index, but subtract 1 from it so we are 0 indexing
                    self.transactions[index] = [item for item in range (components[2], components[1]+1)]
                    # this leaves the list set up like an array, 0 indexed, where each entry is 
                    # another list, containing the transactions. The reason we iterate from
                    # component[2] to component[1]+1 is because the first item in the transaction
                    # will be stored in component[2], and component[1] contains the number of items
                    # which we can use to calculate the index of the last item.
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

