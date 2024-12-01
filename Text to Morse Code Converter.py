#Morse code - Getting a String from the user with the command line and giving back a code morse.
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '/', '.': '.-.-.-', ',': '--..--', 
    '?': '..--..', '\'': '. _ _ _ .', '!': '_ . _ . _ _', '/': '_ . . _ .', 
    '(': '_ . _ _ .', ')': '_ . _ _ . _', '&': '. _ . . .', ':': '_ _ _ . . .', 
    ';': '_ . _ . _ .', '=': '_ . . . _', '+': '. _ . _ .', '-': '_ . . . . _', 
    '_': '. . _ _ . _', '"': '. _ . . _ .', '$': '. . . _ . . _', '@': '. _ _ . _ .',
}


def string_to_morse(input_string):    
    morse_code = ""
    for char in input_string:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            return f"This character {char} is not in our dictionary.\nPlease try again."
    return morse_code

def morse_to_string(input_morse):
    decoded_string = ""
    list_of_morse = input_morse.split(" ")
    for morse in list_of_morse:
        decoded_char = ""
        for key , value in morse_code_dict.items():
            if morse == value:
                decoded_char = key
                break
        if decoded_char:
            decoded_string  += decoded_char
        else:
            return f"This is not a morse code {morse} \nPlease try again."  
    return decoded_string 

def main():
    string_or_morse = int(input("Do you want to write a sting or a morse code? (enter 1 for string and 2 for morse code): "))
    if string_or_morse == 1:
        user_string = input("Please enter a string: ").upper()
        output=string_to_morse(user_string)
    elif string_or_morse == 2:
        user_morse_code = input("Please enter a morse code: ")
        output=morse_to_string(user_morse_code)
    else:
        output = "Invalid choice, please try again."
    print(output)

main()