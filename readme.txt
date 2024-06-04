- Name Nam Nguyen

- UTA ID 1001823561

- Programming language used for the task Python 3.10.11, the code should be omega compatible. 

- How the code is structured:

* Function definitions:
+ The "valid_move" function checks to see if a move is valid given the current state
+ The "human_turn" function gets the human's move from the input
+ The "calculate_score" function gets the score based on the version of the game
+ The "MinMax" function implements the MinMax algorithm with Alpha Beta pruning to determine the computer's best move
+ The "get_computer_move" function gets the computer's move 
+ The "red_blue_nim" function is the main function to play the game
+ The main function checks the parameters for passing command line arguments to the red_blue_nim function

* Main execution:
+ The command line arguments parsed will indicate the red marbles, blue marbles, game version, and the starting player in that respective order
+ Starts the game by calling the "red_blue_nim" function (using the provided parameters)

*Output:
+ Depending on the starting player, the output will show the current count of red and blue marbles and the move from that player
+ If it is the computer's turn, it will make a move and then the turn will be passed to the human player if none of the pile is empty
+ Once it is the human player's turn, the program will give options for that player and ask for input from the player
+ Once the player has made their decision, the program will alternate between these players' turns until the game ends (when the count of either pile is empty)
+ Once the game ends, the score will be calculated from the remaining marbles. The winenr and their final score will be displayed to the user.

*Command line usage:
+ The code checks if the command line arguments are provided for the red marbles count, blue marbles count, game version (optional), and the starting player (optional).

- Instructions: 
+ For PC:
- Check to make sure the latest version of Python is installed (if not, install Python from the official websitee and add Python to path during the installation).
- Open the command prompt by pressing "Window icon + R", type "cmd", and press Enter .
- Use the "cd" command to navigate to the directory where the Python code is located (cd/path/to/source/code).
- Execute the Python script using the command: "python3 red_blue_nim.py <number of red marbles (red)> <number of blue marbles(blue)> <version (standard or misere)> <first player (computer or human)> (there is no depth limited search implementation)

+ For Linux/Mac:
- Check to make sure the latest version of Python is installed (if not, use "sudo apt-get update" and "sudo apt-get install python3")
- Open the terminal
- Use the "cd" command to navigate to the directory where the Python code is located (cd/path/to/source/code).
- Execute the Python script using the command: "python3 red_blue_nim.py <number of red marbles (red)> <number of blue marbles(blue)> <version (standard or misere)> <first player (computer or human)> (there is no depth limited search implementation)

+For Omega:
- Connect to Omega through the terminal (or connect to a VPN if not on campus ground).
- Use the SSH command in your local terminal to log in to the Omega account ("ssh username@omega_address").
- Upload your Python script and input files into your Omega account.
- Use the "cd" command to navigate to the directory where the Python code is located (cd/path/to/source/code).
- Execute the Python script using the command: "python red_blue_nim.py <number of red marbles (red)> <number of blue marbles(blue)> <version (standard or misere)> <first player (computer or human)> (there is no depth limited search implementation)
