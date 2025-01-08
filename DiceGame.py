import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)

    return roll

#value = roll()
# print(value)

while True:
    players = input("How many players (2-4): ")
    if players.isdigit():
        # error handling typecasting from string to int needed  valid integer value or it will return error

        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2-4 players")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer",player_idx + 1,"Turn has just started\n")
        print("\nYour total score is:",player_scores[player_idx],"\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll(y)?")
            if should_roll.lower() !="y":
        # converting to lower case so doesnt matter if user enters Upper case
                break
            value = roll()
            if value == 1:
                print("You rolled a 1 ! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:",value)

            print("Your score is:",current_score)

        player_scores[player_idx] += current_score
        print("Your total score is :" , player_scores[player_idx])
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player  ",winning_idx + 1 ," is the winner with a score of : ",max_score )