# from anthropic import Anthropic
# from config import ANTHROPIC_API_KEY
# # Create a client to talk to Claude
# client = Anthropic(api_key=ANTHROPIC_API_KEY)
# # Send a message to Claude
# response = client.messages.create(
#     model="claude-sonnet-4-20250514",
#     max_tokens=1000,
#     messages=[
#         {"role": "user", "content": "Hello! Please introduce yourself in one sentence."}
#     ]
# )

# # Get Claude's response
# claude_response = response.content[0].text
# # Display it
# print("Claude says:")
# print(claude_response)

from urllib import response
from xmlrpc import client
from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

def ask_claude(question):
    """Send a question to Claude and return the response."""
    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response.content[0].text

def main():
    """Main program."""
    print("=== Claude Test Program ===")
    print("Ask Claude anything!")
    print()
    user_question = input("Your question: ")

    print()
    print("Claude is thinking...")
    print()

    answer = ask_claude(user_question)
    print("Claude says:")
    print(answer)
    # Run the program
main()