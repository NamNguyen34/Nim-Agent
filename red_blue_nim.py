import sys
#Move ordering in standard and misere version
STANDARD_ORDER = ["Pick 2 red marble", "Pick 2 blue marble", "Pick 1 red marble", "Pick 1 blue marble"]
MISERE_ORDER = ["Pick 1 blue marble", "Pick 1 red marble", "Pick 2 blue marble", "Pick 2 red marble"]

#Function to check if a move is valid given the current state
def valid_move(move, red, blue):
    if move.startswith("Pick 1"):
        if "red" in move and red == 0:
            return False
        elif "blue" in move and blue == 0:
            return False
        else:
            return True
    else:
        if "red" in move and red < 2:
            return False
        elif "blue" in move and blue < 2:
            return False
        else:
            return True

#Function to get human's move
def human_turn(red, blue):
    print(f"Red marbles count: {red}, Blue marbles count: {blue}")
    while True:
        print("It is your turn. Pick a move (Type exactly as shown in the options):")
        print("Pick 2 red marble")
        print("Pick 2 blue marble")
        print("Pick 1 red marble")
        print("Pick 1 blue marble")
        choice = input("Enter your choice: ").strip()
        if choice in STANDARD_ORDER or choice in MISERE_ORDER:
            return choice
        else:
            print("Invalid move.")

#Function to calculate score based on the version of the game
def calculate_score(red, blue, version):
    #As the player loses points in the standard version for ending the game in their turn, the score for that version will be negative
    if version == "standard":
        return -1 * (red * 2 + blue * 3)
    #As the player wins points in the misere version for ending the game in their turn, the score for that version will be positive
    elif version == "misere":
        return red * 2 + blue * 3

#Function to implement MinMax algorithm with Alpha Beta pruning to determine the computer's best move
def MinMax(red, blue, is_maximizing, alpha, beta, version):
    if red == 0 or blue == 0:
        return calculate_score(red, blue, version), None

    if is_maximizing:
        max_points = float("-inf")
        for move in (STANDARD_ORDER if version == "standard" else MISERE_ORDER):
            if not valid_move(move, red, blue):
                continue
            new_red = red
            new_blue = blue
            if move.startswith("Pick 1"):
                if "red" in move:
                    new_red -= 1
                else:
                    new_blue -= 1
            else:
                if "red" in move:
                    new_red -= 2
                else:
                    new_blue -= 2
            
            #Recursively calls the MinMax function (points' variable type is turned into any so that it can be compared with max_points, which is a float variable)
            points, _ = MinMax(new_red, new_blue, False - 1, alpha, beta, version)
            #Compare and select the higher value variable between max_points and points and store that value into max_points
            max_points = max(max_points, points)
            #Compare and select the higher value variable between alpha and points and store it into alpha
            alpha = max(alpha, points)
            if beta <= alpha:
                break
        return max_points, None
    else:
        min_points = float("inf")
        for move in (STANDARD_ORDER if version == "misere" else MISERE_ORDER):
            if not valid_move(move, red, blue):
                continue
            new_red = red
            new_blue = blue
            if move.startswith("Pick 1"):
                if "red" in move:
                    new_red -= 1
                else:
                    new_blue -= 1
            else:
                if "red" in move:
                    new_red -= 2
                else:
                    new_blue -= 2
            
            #Recursively calls the MinMax function 
            points, _ = MinMax(new_red, new_blue, True - 1, alpha, beta, version)
            #Compare and select the lowest value variable between min_points and points and store that value into min_points
            min_points = min(min_points, points)
            #Compare and select the lowest value variable between beta and points and store it into beta
            beta = min(beta, points)
            if beta <= alpha:
                break
        return min_points, None

# Function to get computer's move
def get_computer_move(red, blue, version):
    #Hard coded cases to make sure the computer doesn't prioritize getting the maximum amount of points over getting a guaranteed victory
    if red == 1:
        return "Pick 1 red marble"
    if red == 2:
        return "Pick 2 red marble"
    if blue == 1:
        return "Pick 1 blue marble"
    if blue == 2:
        return "Pick 2 blue marble"
    
    #Calculate the computer's best move in the standard version
    if version == "standard":
        best_score = float("-inf")
        best_move = None
        for move in STANDARD_ORDER:
            if not valid_move(move, red, blue):
                continue    
            new_red = red
            new_blue = blue
            if move.startswith("Pick 1"):
                if "red" in move:
                    new_red -= 1
                else:
                    new_blue -= 1
            else:
                if "red" in move:
                    new_red -= 2
                else:
                    new_blue -= 2
            score, _ = MinMax(new_red, new_blue, False, float("-inf"), float("inf"), version)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
    
    #Calculate the computer's best move in the misere version
    else:
        best_score = float("inf")
        best_move = None
        for move in MISERE_ORDER:
            if not valid_move(move, red, blue):
                continue
            new_red = red
            new_blue = blue
            if move.startswith("Pick 1"):
                if "red" in move:
                    new_red -= 1
                else:
                    new_blue -= 1
            else:
                if "red" in move:
                    new_red -= 2
                else:
                    new_blue -= 2
            score, _ = MinMax(new_red, new_blue, True, float("-inf"), float("inf"), version)
            if score < best_score:
                best_score = score
                best_move = move
        return best_move

# Main function to play the game, default input will let the program know that it should use the standard version and the first player is the computer
def red_blue_nim(red, blue, version = "standard", first_player = "computer"):

    #Check if the pile still has red or blue marbles
    while red > 0 and blue > 0:
        #The computer goes first
        if first_player == "computer":
            computer_move = get_computer_move(red, blue, version)
            print(f"Computer's move: {computer_move}")         
            if computer_move.startswith("Pick 1"):
                if "red" in computer_move:
                    red -= 1
                else:
                    blue -= 1
            else:
                if "red" in computer_move:
                    red -= 2
                else:
                    blue -= 2

            #If either pile is empty on the computer's turn, the game ends and the computer loses points in the standard version or wins points in the misere version
            if red == 0 or blue == 0:
                score = calculate_score(red, blue, version)
                print(f"Computer wins the game with {score} points")
                break

            human_move = human_turn(red, blue)
            print(f"Human's move: {human_move}")
            if human_move.startswith("Pick 1"):
                if "red" in human_move:
                    red -= 1
                else:
                    blue -= 1
            else:
                if "red" in human_move:
                    red -= 2
                else:
                    blue -= 2

            #If either pile is empty on the human's turn, the game wins and the human loses points in the standard version or wins points in the misere version
            if red == 0 or blue == 0:
                score = calculate_score(red, blue, version)
                print(f"You win the game with {score} points")

        #The human goes first
        else:
            human_move = human_turn(red, blue)
            print(f"Human's move: {human_move}")          
            if human_move.startswith("Pick 1"):
                if "red" in human_move:
                    red -= 1
                else:
                    blue -= 1
            else:
                if "red" in human_move:
                    red -= 2
                else:
                    blue -= 2

            #If either pile is empty on the human's turn, the game wins and the human loses points in the standard version or wins points in the misere version
            if red == 0 or blue == 0:
                score = calculate_score(red, blue, version)
                print(f"You win the game with {score} points")
                break

            computer_move = get_computer_move(red, blue, version)
            print(f"Computer's move: {computer_move}")          
            if computer_move.startswith("Pick 1"):
                if "red" in computer_move:
                    red -= 1
                else:
                    blue -= 1
            else:
                if "red" in computer_move:
                    red -= 2
                else:
                    blue -= 2

            #If either pile is empty on the computer's turn, the game wins and the computer loses points in the standard version or wins points in the misere version
            if red == 0 or blue == 0:
                score = calculate_score(red, blue, version)
                print(f"Computer wins the game with {score} points")

if __name__ == "__main__":
    #Passing command line arguments for red, blue, version, and first player
    if len(sys.argv) < 3:
        print("Usage: red_blue_nim.py <red> <blue> [<version>] [<first-player>]")
        sys.exit(1)
    red = int(sys.argv[1])
    blue = int(sys.argv[2])
    version = sys.argv[3] if len(sys.argv) >= 4 else "standard" 
    first_player = sys.argv[4] if len(sys.argv) >= 5 else "computer"  

    #Starting the game with the provided parameters
    red_blue_nim(red, blue, version, first_player)