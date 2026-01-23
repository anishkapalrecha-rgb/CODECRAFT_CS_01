def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        # Check if character is an alphabet
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - start + shift) % 26 + start)
            elif mode == "decrypt":
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            # Non-alphabet characters remain unchanged
            result += char

    return result


# User input
message = input("Enter the message: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'encrypt' or 'decrypt': ").lower()

# Perform operation
output = caesar_cipher(message, shift, choice)
print("Result:", output)
