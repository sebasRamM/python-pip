import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')

  user_option = input('piedra, papel o tijera =>')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('Opcion invalida')
    return None, None
    
  computer_option = random.choice(options)

  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print(f'Empate! Tu elegiste {user_option} y la computadora tambien')
  elif user_option == 'piedra' and computer_option == 'tijera' or user_option == 'papel' and computer_option == 'piedra' or user_option == 'tijera' and computer_option == 'papel':
    print(f'Ganaste! Tu elegiste {user_option} y la computadora eligio {computer_option}')
    user_wins += 1
  else:
    print(f'Perdiste! Tu elegiste {user_option} y la computadora eligio {computer_option}')
    computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('Computer Wins', computer_wins)
    print('*' * 10)
    print('User Wins', user_wins)
    print('*' * 10)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
  
    if computer_wins == 2 or user_wins == 2:
      break
run_game()