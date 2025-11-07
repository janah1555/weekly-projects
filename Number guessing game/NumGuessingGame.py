import random

play_again = True
score = 0

while play_again:
    num = random.randint(1,10)
    guess = 0
        
    while guess != num:
        guess = int(input("guess a numbr from 1 -10 : \n"))
        
        if guess > num:
            print("guess lowr!")
            score -= 1
            print("your score is:", score)
        elif guess < num:
            print("guess higher1")
            score -= 1
            print("your score is:", score)
        else:
          print("you won! \n ")
          score += 1
          print("your score is:", score)
          choice = input("type 'quit' to quit:\n").lower()
          if choice == "quit":
             print("your final score is:" ,score)
             print("goodbye!")
             play_again = False                     
                     
