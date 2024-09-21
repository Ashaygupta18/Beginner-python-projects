#Python Slot Machine
# 🍋⭐🍒🍉7️⃣
import random

def spin_row():
    symbols = ["🍋","⭐","🍒","🍉","7️⃣"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(bet,row):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍋":
            return bet*3
        elif row[0] == "🍒":
            return bet*5
        elif row[0] == "🍉":
            return bet*10
        elif row[0] == "⭐":
            return bet*15
        elif row[0] == "7️⃣":
            return bet*50
    else:
        return 0
        
def main():
    balance = 100
    print("---------WELCOME--------")
    print("------SLOT MACHINE------")

    while balance > 0:
        print(f"Current balance:${balance}")

        bet = input("Enter the amount you want to bet: ")
        
        if not bet.isdigit():
            print("Enter a valid number")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("INSUFFICIENT FUNDS")
            continue
        elif bet <= 0:
            print("Bet can not be less or equal to zero")
        
        balance -= bet
        
        row = spin_row()
        print("SPINNING....")
        print_row(row)

        get_payout(bet, row)
        payout = get_payout(bet , row)

        if payout > 0:
            print("YOU WON!!!")
            print(f"You won ${payout}")
        else: 
            print("You lost! Try again...")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again != "Y":
             break
    
        print(f"GAME OVER!! Your Balance is {balance}")

if __name__ == "__main__":
    main()