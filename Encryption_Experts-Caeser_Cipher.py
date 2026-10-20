memory = {}  # Empty dictionary to store encrypted messages
while True:
    choice = str(input("Enter your choice: \n E for Encryption \n D for Decryption \n B for Brute Force Attack \n M for Memory \n 0 for Exit \n")).upper()  # Used to assign the user's choice to a variable for use in the match statement below. The input is converted to uppercase to ensure that the program can handle both uppercase and lowercase inputs.
    match choice:  # Used to determine which function to execute based on the user's choice.
        case "E":
            memory_min = 0  # used to limit the number of messages stored in memory
            try:
                memory_max = int(input("How many encrypted messages do you choose to store? (1-20) "))  # upper limit for the number of messages stored in memory
                if 0 < memory_max < 20:
                    pass
                else:
                    print("Not enough memory. Please enter a number between 1 and 19.")
                    exit() #We intentionally designed the shift-value validation to terminate the program whenever the user enters a number outside the accepted range of 1 to 20.
                           #Instead of allowing the user to correct the mistake and try again, the program closes and requires them to restart from the beginning.
                           #This approach was intended to create a sense of frustration that would encourage users to pay closer attention to the instructions and enter the correct values.
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                exit()

            while memory_min < memory_max:
                shift_value = int(input("Enter the shift value: "))
                try:
                    if 0 < shift_value < 27:
                        pass
                    else:
                        print("Invalid shift value. Please enter a number from 1 and 26.")
                        exit()
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    exit()
                message = str(input("Enter the message to encrypt: "))
                encryption = f'Shift Value = {shift_value}, Encryption: '  # Empty string to store the encrypted message
                for letter in message:  # Loop through each letter in the message to determine its new value based on the shift value and whether it is uppercase or lowercase. If it is not a letter, it will remain the same.
                    if letter.isupper():
                        new_value = (((ord(letter) + shift_value)) - ord('A')) % 26
                        encryption += chr(new_value + ord('A'))
                    elif letter.islower():
                        new_value = (((ord(letter) + shift_value)) - ord('a')) % 26
                        encryption += chr(new_value + ord('a'))
                    else:
                        new_value = letter
                        encryption += new_value
                print("Encrypted message:", encryption)  # chosen to print the encrypted message after each iteration of the  for loop
                memory_min += 1  # Increment the memory counter
                memory[message] = encryption  # Store the original message and its corresponding encrypted message in the memory dictionary
        case "D":
            memory = {}  # Empty dictionary to store encrypted messages
            memory_min = 0
            memory_max = int(input("How many encrypted messages do you choose to store? (1-20) "))
            if 0 < memory_max < 20:
                pass
            else:
                print("Not enough memory. Please enter a number between 1 and 19.")
                exit()
            while memory_min < memory_max:
                shift_value = int(input("Enter the shift value: "))
                try:
                    if 0 < shift_value < 27:
                        pass
                    else:
                        print("Invalid shift value. Please enter a number from 1 and 26.")
                        exit()
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    exit()
                message = str(input("Enter the message to decrypt: "))
                decryption = f'Shift Value = {shift_value}, Decryption: '
                for letter in message:
                    if letter.isupper():
                        new_value = (((ord(letter) - shift_value)) - ord('A')) % 26
                        decryption += chr(new_value + ord('A'))
                    elif letter.islower():
                        new_value = (((ord(letter) - shift_value)) - ord('a')) % 26
                        decryption += chr(new_value + ord('a'))
                    else:
                        new_value = letter
                        decryption += new_value
                print("Decrypted message:", decryption)
                memory_min += 1
                memory[message] = decryption
        case "B":
            shift_value = 1
            max_attempts = 11
            message = str(input("Enter the message to decrypt: "))  # Used to assign the message to be decrypted to a variable for use in the brute force attack loop
            while shift_value < max_attempts:  # Loop through the shift values from 1 to 10 to attempt to decrypt the message using each shift value. The loop will continue until the maximum number of attempts is reached.
                decryption = ""
                for letter in message:
                    if letter.isupper():
                        new_value = (((ord(letter) - shift_value)) - ord('A')) % 26
                        decryption += chr(new_value + ord('A'))
                    elif letter.islower():
                        new_value = (((ord(letter) - shift_value)) - ord('a')) % 26
                        decryption += chr(new_value + ord('a'))
                    else:
                        new_value = letter
                        decryption += new_value
                print(f"Shift value {shift_value}: {decryption}")  # Print the decrypted message for each shift value attempted.
                shift_value += 1  # Increment the shift value for the next iteration of the loop.
        case "M":
            print(memory)  # Print the memory dictionary to display the stored messages and their corresponding encrypted or decrypted messages.
        case "0":
            print("Exiting the program.")  # Print a message to indicate that the program is exiting
            exit()  # Exit the program
        case _:
            print("Invalid choice. Please try again.")  # Print a message to indicate that the user's choice was invalid and prompt them to try again.




# No Artificial Intelligence was used to generate this code. It was both brainstormed and written entirely by two semi novice programmers.