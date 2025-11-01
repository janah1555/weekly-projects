import random
import time

answers = ["yes","maybe","no"]

quit = False
answer = random.choice(answers)

while not quit:
    question = input("yes or no question (type 'quit' to quit):?\n")
    
    if ( question == "quit"):
        print("goodbye,loser!")
        time.sleep(0.5)
        quit = True
    else:
         
         print("shaking the Magic 8 Ball" ,end="")
         for _ in range(3):
             print(".", end="")
             time.sleep(0.7)
         print("\nAnswers:",answer,"\n")
         
