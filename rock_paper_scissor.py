import random

check = {
    "r": {
        'r': 'draw',
        'p': 'loose',
        's': 'win'
    },
    "p": {
        'r': 'win',
        'p': 'draw',
        's': 'loose'
    },
    "s": {
        'r': 'loose',
        'p': 'win',
        's': 'draw'
    }
}

def play():
    print("----'r' for rock, 'p' for paper & 's' for scissors----")
    user = input("Enter your choice : ")
    computer = random.choice(['r','p','s'])
    print(f"Your choice : {user}")
    print(f"Computer choice : {computer}")
    if(['r','s','p'].__contains__(user)):
        if(check[user][computer] == 'win'):
            print('You Won')
        elif(check[user][computer] == 'loose'):
            print('You Lost')
        else:
            print('Game Drawn')
    else:
        print("please choose among 's', 'p' & 'r'...")

play()