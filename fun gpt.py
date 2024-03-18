def build_chatgpt():
  """
  This function simulates a simple conversation with a chatbot.
  """
  while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
      break
    response = "I am still under development, but I am learning!"
    print("Chatgpt: ", response)

# Example usage
build_chatgpt()

#string replace function
text = "You are currently studying in 5th semester."
new_text = text.replace("5th", "7th")
print(new_text)
