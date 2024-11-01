import random

def get_choices():
  player_choice = input("Enter your choice ROCK | PAPERS | SCISSORS : ")
  
  game_options = ["rock" , "papers", "scissors"]
  computer_choice = random.choice(game_options)
  
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_winner(player, computer):
  
  # Using an 'f' string
  print(f" You choose {player} , Computer chose {computer}")
  
  if(player == computer):
    return ("It is a Tie!")
    
  elif(player == "rock"):
    if(computer == "scissors"):
      return ("Rock smashes the scissors ! Player Wins")
    else:
      return ("Paper covers the rock ! Player loses")

  elif(player == "papers"):
    if(computer == "rock"):
       return ("Paper covers the rock ! Player Wins")
    else:
      return ("Scissor cuts the paper ! Player loses")

  elif(player == "scissors"):
    if(computer == "papers"):
      return ("Scissor cuts the paper ! Player Wins")
    else:
      return ("Rock smashes the scissors ! Player loses")
    



choices = get_choices()
winner = check_winner(choices["player"], choices["computer"])
print(winner)
