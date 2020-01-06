table = []
def make():
    for i in range(1,10):
        table.append(i)
    
def refresh(): # resets the board removing all signs and replacing with numbers
   pass

def display(): # displays the board 
    print(str(table[0]) + " | " + str(table[1]) + " | " + str(table[2]))
    print ("--|---|--")
    print(str(table[3]) + " | " + str(table[4]) + " | " + str(table[5]))
    print ("--|---|--")
    print(str(table[6]) + " | " + str(table[7]) + " | " + str(table[8]))

def mark(position): # Player chooses area on board and swap number with player's sign
    

