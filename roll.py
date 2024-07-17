import random

# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

def roll_die(num_rolls):
    result = [random.randint(1, 6) for _ in range(num_rolls)]
    print(f"You rolled a {result}")

def main():
    while True:
        user_input = input("Enter the number of dice you would like to roll or type 'q' to quit: ")
        if user_input == 'q':
            print("Goodbye!")
            break
        try:
            num_rolls = int(user_input) 
            roll_die(num_rolls)
        except ValueError:
            print("Please enter a valid number")
        


if __name__ == "__main__":
    main()
        