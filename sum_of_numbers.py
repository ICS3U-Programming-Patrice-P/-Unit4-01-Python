#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: Nov 3, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # get user input
    user_number_string = input("\033[1;35;39mEnter a positive number: ")
    print("")

    # catches invalid input
    try:
        # Converts string to integer
        user_number = int(user_number_string)
        # Check if user input is a positive number
        if user_number > 0:
            # calculate the sum of all numbers from 0 to user input
            while loop_counter <= user_number:
                sum = sum + loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                loop_counter = loop_counter + 1

            print("")
            print(
                "The sum of the numbers from 0 to {} is: {}.".format(user_number, sum)
            )
        elif user_number < 0:
            print("You entered a negative number, please try again.")
        else:
            print("0 is not a positive integer")
    except Exception:
        print("\033[1;35;35mThis is not an integer")
    finally:
        print()
        print("\033[1;35;38mThanks for playing")


if __name__ == "__main__":
    main()
