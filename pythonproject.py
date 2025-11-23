import random
choice = ("rock", "paper", "scissor")
attempt = None
akash = True #flag = 1

while akash: #flag == 1
        attempt = None
        computer = random.choice(choice)

        while attempt not in choice:
            attempt = input("enter rock, paper, or scissor:").lower()
            if attempt not in choice:
                print("Invalid choice")



        print(f"computer: {computer}")
        print(f"player: {attempt}")

        if computer == attempt:
            print("its a draw")
        elif attempt == "rock" and computer == "scissor":
            print("you win")
        elif attempt == "scissor" and computer == "paper":
            print("you win")
        elif attempt == "paper" and computer == "rock":
            print("you win")
        else :
            print("you lose")
        play_again = input("play again? (y/n): ").lower()
        if not play_again == "y":
          akash = False #flag = 0 #django, flask 





