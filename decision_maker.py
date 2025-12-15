def create_greeting(person_name):
    #"""Create a personalized greeting based on the name."""
    if person_name == "Go":
        return "Welcome back, Go! Ready to code today?"
    elif person_name == "":
        return "You didn't enter a name. Please try again."
    else:
        return "Hello, " + person_name + "! Nice to meet you."

def main():
   # """Main program loop."""
    print("=== Smart Greeter ===")
    print("Type 'quit' to exit")
    print()
    
    while True:  # Loop forever until we break out
        user_input = input("What is your name? ")
        
        if user_input.lower() == "quit":
            print("Goodbye! Thanks for using Smart Greeter.")
            break  # Exit the loop
        
        greeting = create_greeting(user_input)
        print(greeting)
        print()  # Empty line for readability

# Run the program
main()