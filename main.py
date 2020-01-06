import board, check

playerOne = ''
playerTwo = ''
position = 0
counter = [1,2,3,4,5,6,7,8,9]

def order():
    print("Do you want to be 'X' or 'O' : " )
    letter = input().upper()
    if(letter == 'X'):
        playerOne = 'X'
        playerTwo = 'O'
    else:
        playerOne = 'O'
        playerTwo = 'X'

def move():
    print("Choose a position to mark: ")
    position = raw_input()
    while position not in counter:
        print("Position taken or not valid")
        print("Enter a new position: ")
        position = raw_input()
    
        


def main():
    
    # mark.order()

    board.make()
    board.display()
    while(table )

main()