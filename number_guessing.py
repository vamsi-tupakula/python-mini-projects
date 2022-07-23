import random

generate_num = random.randrange(1,100)

while(True):
    num = int(input("guess number btw 1 & 100 :: "))
    if(num == generate_num):
        print("nice guess...")
        break
    elif(num > generate_num):
        print("too high, guess something that is low")
    else:
        print("too low, guess something that is high")