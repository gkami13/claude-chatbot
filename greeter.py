def create_greeting(person_name):
#Takes a person's name and returns a personalized greeting.This is the same logic the chatbot will use to greet users. """
    greeting = "Hello, " + person_name + "! Welcome to your AI learning journey."
    return greeting
def main():
#"""
#Main function that runs the program.
#"""
    print("=== Personalized Greeter ===")
    print()
    # Ask user for their name
    user_name = input("What is your name? ")
    # Create the greeting
    greeting_message = create_greeting(user_name)
    # Display the greeting
    print()
    print(greeting_message)
# Run the program
main()