from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

def ask_claude(conversation_history):
	"""Send conversation history to Claude and return the response."""
	client = Anthropic(api_key=ANTHROPIC_API_KEY)
	response = client.messages.create(
		model="claude-sonnet-4-20250514",
		max_tokens=1000,
		messages=conversation_history
	)
	return response.content[0].text

def main():
	"""Main chatbot loop with conversation history."""
	print("=" * 50)
	print("CLAUDE CHATBOT (With Memory)")
	print("=" * 50)
	print("Commands:")
	print(" - Type 'quit' to exit")
	print(" - Type 'clear' to start a new conversation")
	print(" - Type your message to chat with Claude")
	print("=" * 50)
	print()
	# Store the conversation history
	conversation_history = []
	while True:
		# Get user input
		user_input = input("You: ").strip()
		# Check for quit command
		if user_input.lower() == "quit":
			print()
			print("Thanks for chatting! Goodbye!")
			break
		# Check for clear command
		if user_input.lower() == "clear":
			conversation_history = []
			print()
			print("Conversation cleared. Starting fresh!")
			print()
			continue
		# Check for empty input
		if user_input == "":
			print("Please type a message.")
			print()
			continue
		# Add user message to history
		conversation_history.append({
			"role": "user",
			"content": user_input
		})
		# Get response from Claude
		try:
			print()
			print("Claude: ", end="")
			response = ask_claude(conversation_history)
			print(response)
			print()
			# Add Claude's response to history
			conversation_history.append({
				"role": "assistant",
				"content": response
			})
		except Exception as e:
			print(f"Error: {e}")
			print("Please try again.")
			print()
			# Remove the user message since we got an error
			if conversation_history:
				conversation_history.pop()

# Run the chatbot
if __name__ == "__main__":
	main()