from class_a import Die

def menu_all():
    print("\nHomework 7 Menu\n-----------------------------------------------------")
    print("1- Roll a 6 Sided Die")
    print("2- Exit")
    
    user_option = input("Please select an option:\n")
    
    if user_option == "1":
        option_1_hw2()
    elif user_option == "2":
        option_2_hw_2()
    else:
        print("\nPlease select a valid number input.")
        menu_all()

def option_1_hw2():
    die = Die()  # Instantiate the Die class
    die.roll()  # Roll the die
    print(f"\n{die}\n")  # Print the result of the roll using the __str__ method of the Die class
    
    option_3_hw_2()

def option_3_hw_2():
    exit_choice = input("Do you want to continue rolling? (yes/no): ")
    if exit_choice.lower() == "no":
        print("\n...Program Ended...\n")
    else:
        print("\n...Rerolling...")
        option_1_hw2()

def option_2_hw_2():
    exit_choice = input("Are you sure you want to leave? (yes/no): ")
    if exit_choice.lower() == "yes":
        print("\n...Program Exited...\n")


if __name__ == "__main__":
    menu_all()