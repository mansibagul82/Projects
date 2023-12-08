import random 
print("***********🤗 Welcome To Rock Paper Scissors Game 🤗***********")
options = ["rock","paper","scissors"] # options 
dic = {
       "rock" : "🪨",
       "paper" : "📃",
       "scissors" : "✂️"
}        # dictionary
count_player = 0 # point counter variable  
count_computer = 0
count_tie = 0
running = True
while running: # while loop
  player = None    
  computer = random.choice(options) # computer choice
  player_choice = int(input(''' 
  Game Start ..🏁
  Do You Want Play 
  1 Yes
  2 No | Exit
  '''))   #player input
  #  if you choice 1 game start
  
  print(" _______________________________________________________________________________________")
  # conditions 
  if player_choice == 1:
    while player not in options:
      player = input("_Enter a choice(rock,paper,scissors):")
    print("* Player:",dic[player])
    print("* computer:",dic[computer])
    if player == computer:
      print("_Tie !😁")
      count_tie += 1
    elif player == "rock" and computer == "scissors":
      print("You Win!🎊")
      print("Computer Lose!😦")
      count_player += 1
    elif player == "paper" and computer == "rock":
      print("You Win!🎊")
      print("Computer Lose!😦")
      count_player += 1
    elif player == "scissors" and computer == "paper":
      print("You Win!🎊")
      print("Computer Lose!😦")
      count_player += 1
    else:
      print("You Lose!😦")
      print("Computer Win!🎊")
      count_computer += 1
    print("__________________________________________________________________________________________")
    print("********💐 Thank You For Playing ! 💐********")
    # player enter 2 so player don't want to play game  
    print("__________________________________________________________________________________________")
     
  else:
    
    print("________________________________________________________________________________________")
    # point counter
    if count_computer < count_player:
      print("---🥰 Congratulations You Win! 🥰---")
      print("-Your Final Score: ",count_player)
      print("-Computer Final Score: ",count_computer)
      print("-Tie: ",count_tie)
      print("*********💐 Thank You For Playing ! 💐*********")
      print("_____________________________________________________________________________________")
      print("*********💐 Thank You For coming ! 💐*********") 
      print("_____________________________________________________________________________________")
    elif count_computer > count_player:
      print("😄 Computer Win! 😄")
      print("-Computer Final Score: ",count_computer)
      print("-Your Final Score: ",count_player)
      print("-Tie: ",count_tie)
      print("You Lose!😦")
      print("_____________________________________________________________________________________")
      print("*********💐 Thank You For coming ! 💐*********") 
      print("_____________________________________________________________________________________")
    elif count_computer == count_player:
      print("-Your Final Score: ",count_player)
      print("-Computer Final Score: ",count_computer)
      print("-Tie: ",count_tie)
      print("============😁 Game is Tie 😁============")
      print("_____________________________________________________________________________________")
      print("*********💐 Thank You For coming ! 💐*********") 
      # now game ended
      print("_____________________________________________________________________________________")
    break  
   

 
      
    