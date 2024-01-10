import  random
while True:
  choices=["rock","paper","sissors"]
  computer=random.choice(choices)
  player= None
  while player not in choices:
   player=input("rock,paper or scissors").lower()
  if player==computer:
   print("computer:",computer)
   print("player:",player)
   print("tie")
  elif player=="rock":
     if computer =="paper":
         print("computer:",computer)
         print("player:",player)
         print("you lost")
     if computer=="scissors":
         print("computer:",computer)
         print("player:",player)
         print("you won")
  elif player=="scissors":
     if computer =="paper":
         print("computer:",computer)
         print("player:",player)
         print("you won")
     if computer=="rock":
         print("computer:",computer)
         print("player:",player)
         print("you lost")
  elif player=="paper":
     if computer =="scissors":
         print("computer:",computer)
         print("player:",player)
         print("you lost")
     if computer=="rock":
         print("computer:",computer)
         print("player:",player)
         print("you wim")
  play_again=input("play again?").lower()
  if play_again!="yes":
       break
  print("bye")