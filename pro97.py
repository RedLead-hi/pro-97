import random
print("number guessing name")
number=random.randint(10,90)
chances=0
print("guess a random number from 10 to 90: ")
while chances<5:
 guess=int(input("enter your guess: "))
 if guess==number:
    print("you won") 
    break
 elif guess<number:
      print("your guess was too low. guess a number higher than ",guess)
 else:
      print("your guess was too high. guess a number lower than ",guess)
 chances+=1
if not chances<5:
 print("you lose. the number is",number)
