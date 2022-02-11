charachters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
			   "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
			   "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
			   "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
			   "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7",
			   "8", "9"]


def encode(message, shift):
	index_numbers_list = []
	shifted_index_numbers_list = []
	encoded_message_list = []
	for char in message:
		try:
			index_numbers_list.append(charachters.index(char))
		except ValueError:
			index_numbers_list.append(char)

	for i in index_numbers_list:
		if str(i).isnumeric():
			i += shift
			while i > (len(charachters) - 1):
				i -= len(charachters)
			shifted_index_numbers_list.append(i)
		else:
			shifted_index_numbers_list.append(i)

	for i in shifted_index_numbers_list:
		if str(i).isnumeric():
			encoded_message_list.append(charachters[i])
		else:
			encoded_message_list.append(i)

	return "".join(encoded_message_list)


def decode(message, shift):
	index_numbers_list = []
	shifted_index_numbers_list = []
	encoded_message_list = []
	for char in message:
		try:
			index_numbers_list.append(charachters.index(char))
		except ValueError:
			index_numbers_list.append(char)

	for i in index_numbers_list:
		if str(i).isnumeric():
			i -= shift
			while i < 0:
				i += len(charachters)
			shifted_index_numbers_list.append(i)
		else:
			shifted_index_numbers_list.append(i)

	for i in shifted_index_numbers_list:
		if str(i).isnumeric():
			encoded_message_list.append(charachters[i])
		else:
			encoded_message_list.append(i)

	return "".join(encoded_message_list)


print(
"""
==============================
 Welcome to PRIMITIVE CIPHER!
=============================="""
)

while True:
	user_choice = input('\nType "encode" to encrypt, "decode" to decrypt, or "quit" to end program. ').casefold()
	while user_choice not in ["encode", "decode", "quit"]:
		user_choice = input('Invalid input. Please enter "encode", "decode", or "quit". ').casefold()
	if user_choice == "encode":
		message_to_encrypt = input("\nEnter a message to encrypt: ")
		shift_amount = input("Enter the shift number: ")
		while not shift_amount.isnumeric():
			shift_amount = input("Invalid input. Please enter a number: ")
		print("\nYour encrypted message:")
		print(encode(message_to_encrypt, int(shift_amount)))
	elif user_choice == "decode":
		message_to_decrypt = input("\nEnter a message to decrypt: ")
		shift_amount = input("Enter the shift number: ")
		while not shift_amount.isnumeric():
			shift_amount = input("Invalid input. Please enter a number: ")
		print("\nYour decrypted message:")
		print(decode(message_to_decrypt, int(shift_amount)))
	elif user_choice == "quit":
		break


print(
"""
=======================================
 Thank you for using PRIMITIVE CIPHER!
=======================================
"""
)