import time
# The code is not the most efficient but it works 🤣

# Table or the places which the players can define and place X/O on
# Should look like this: 
# R1 | R2 | R3
# R4 | R5 | R6
# R7 | R8 | R9
gt = {
   'R1': ' ', 'R2': ' ', 'R3': ' ',
   'R4': ' ', 'R5': ' ', 'R6': ' ',
   'R7': ' ', 'R8': ' ', 'R9': ' '
}
# Made the table with an array because it saves space and makes it more simple

player = 1 # Sets the game to start with player 1
moves = 0 # Count the moves the players have done
end = 0 # Set if the game has ended or not

p1w = "Player 1 wins!"
p2w = "Player 2 wins!"


def check():
   # return 1 means the game will end

   # All possible win combinations for X
   # All possible horizontal win combinations for X
   if gt['R1'] == 'X' and gt['R2'] == 'X' and gt['R3'] == 'X':
      print(p1w)
      return 1
   if gt['R4'] == 'X' and gt['R5'] == 'X' and gt['R6'] == 'X':
      print(p1w)
      return 1
   if gt['R7'] == 'X' and gt['R8'] == 'X' and gt['R9'] == 'X':
      print(p1w)
      return 1
        
   # All possible diagonal win combinations for X
   if gt['R1'] == 'X' and gt['R5'] == 'X' and gt['R9'] == 'X':
      print(p1w)
      return 1
   if gt['R3'] == 'X' and gt['R5'] == 'X' and gt['R7'] == 'X':
      print(p1w)
      return 1

   # All possible vertical win combinations for X
   if gt['R1'] == 'X' and gt['R4'] == 'X' and gt['R7'] == 'X':
      print(p1w)
      return 1
   if gt['R2'] == 'X' and gt['R5'] == 'X' and gt['R8'] == 'X':
      print(p1w)
      return 1
   if gt['R3'] == 'X' and gt['R6'] == 'X' and gt['R9'] == 'X':
      print(p1w)
      return 1
      

   # All possible win combinations for O
   # All possible horizontal win combinations for O
   if gt['R1'] == 'O' and gt['R2'] == 'O' and gt['R3'] == 'O':
      print(p1w)
      return 1
   if gt['R4'] == 'O' and gt['R5'] == 'O' and gt['R6'] == 'O':
      print(p1w)
      return 1
   if gt['R7'] == 'O' and gt['R8'] == 'O' and gt['R9'] == 'O':
      print(p1w)
      return 1
        
   # All possible diagonal win combinations for O
   if gt['R1'] == 'O' and gt['R5'] == 'O' and gt['R9'] == 'O':
      print(p1w)
      return 1
   if gt['R3'] == 'O' and gt['R5'] == 'O' and gt['R7'] == 'O':
      print(p1w)
      return 1

   # All possible vertical win combinations for O
   if gt['R1'] == 'O' and gt['R4'] == 'O' and gt['R7'] == 'O':
      print(p1w)
      return 1
   if gt['R2'] == 'O' and gt['R5'] == 'O' and gt['R8'] == 'O':
      print(p1w)
      return 1
   if gt['R3'] == 'O' and gt['R6'] == 'O' and gt['R9'] == 'O':
      print(p1w)
      return 1

   return 0

clean = "\n"
cleanconsole = clean*1000

print("This Tic Tac Toe game was made for the Developer Test of Untangledmedia")
input("Press Enter to play..")
print("Let's play!")
time.sleep(2)

while True:
   # Prints out the game board on game start and after every move
   print(
   cleanconsole +
   '--------------------\nLocations:\nR1 | R2 | R3\nR4 | R5 | R6\nR7 | R8 | R9\n--------------------\nGame:\n' +
   gt['R1'] + '|' + gt['R2'] + '|' + gt['R3'] + '\n' +
   gt['R4'] + '|' + gt['R5'] + '|' + gt['R6'] + '\n' +
   gt['R7'] + '|' + gt['R8'] + '|' + gt['R9'] + '\n' +
   '--------------------' # 20
   )
   print()
   end = check()
   if moves == 9 or end == 1:
      break
   while True:
      if player == 1:  # Checks if it's player one if it's not selects player two
            p1_input = input('P1: ')
            # Puts the X in the position specified by the player
            if p1_input.upper() in gt and gt[p1_input.upper()] == ' ': # Checks if the wanted pos is free
               gt[p1_input.upper()] = 'X' # Symbol to input
               player = 2 # Next move
               break
            # on wrong input
            else: # If pos wasn't free, try again
               print('Invalid input, please try again.')
               continue
      else:
         p2_input = input('P2: ')
         # Puts the X in the position specified by the player
         if p2_input.upper() in gt and gt[p2_input.upper()] == ' ': # Checks if the wanted pos is free
            gt[p2_input.upper()] = 'O' # Symbol to input
            player = 1 # Next move
            break
         else: # If pos wasn't free, try again
            print('Invalid input, please try again.')
            continue
   moves += 1 # Counts moves
   print('--------------------')
   print()