import random

def RSP():
    options = ["Rock", "Paper", "Scissors"]
    wins = 0
    losses = 0
    attempts = 3

    print("*************************************")
    print("------- ROCK, PAPER & SCISSORS -------")
    print("*************************************\n")

    for attempt in range(1, attempts + 1):
        print(f"\n--- Round {attempt} ---")
        print("1. ROCK")
        print("2. PAPER")
        print("3. SCISSORS")
        
        try:
            n = int(input("Enter the number of your choice (1-3): "))
            if n not in [1, 2, 3]:
                print("Invalid choice! Please select 1, 2, or 3.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        user_entered = options[n - 1]
        com = random.choice(options)

        print(f" You chose: {user_entered}")
        print(f" Computer chose: {com}")

        if user_entered == com:
            print(" Result: It's a Tie!")
        elif (
            (user_entered == "Rock" and com == "Scissors") or
            (user_entered == "Paper" and com == "Rock") or
            (user_entered == "Scissors" and com == "Paper")
        ):
            print(" Result: You Win This Round!")
            wins += 1
        else:
            print(" Result: You Lose This Round!")
            losses += 1

        if wins == 2:
            break

    print("\n------- Game Stats -------")
    print(f"Wins: {wins} | Losses: {losses}")
    
    if wins > losses:
        print(" Congratulations! You WON the GAME!")
    elif losses > wins:
        print(" Game Over! Computer WON the GAME!")
    else:
        print(" It's a Draw!")
    print("--------------------------")

RSP()
    


