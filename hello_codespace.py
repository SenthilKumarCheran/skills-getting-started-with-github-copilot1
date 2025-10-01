#add another function to get what is users country and greet them accordingly with their name
"""
This script greets the user by name and country.

Workflow:
1. Prints a welcome message.
2. Prompts the user to enter their name and greets them.
3. Asks for the user's address. If not provided, notifies the user.
4. If the address is provided, prompts for the user's country and greets them accordingly.

Functions:
- None (all logic is in the main script body).

Inputs:
- name: The user's name.
- address: The user's address (optional).
- country: The user's country (if address is provided).

Outputs:
- Prints personalized greetings based on user input.
"""
print("Hello, Codespace!")
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")

address = input("What is your address? ")
if not address.strip():
	print("Address not provided.")
else:
	country = input("What is your country? ")
	print(f"Welcome from {country}, {name}!")
