import random

n= random.randint(1,100)
a=-1
g=0

while(a!=n):
    g+=1
    a=int(input("Guess the number: "))
    if a>n:
        print("Lower Value")
    else:
        print("Higher Value")
        
print(f"You Guessed the correct random no. {n} in the {g} times")