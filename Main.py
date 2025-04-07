# Morse Code Translator

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

# Reverse dictionary for decoding
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # Unknown characters
    return ' '.join(morse_code)


def morse_to_text(morse):
    words = morse.split(' / ')
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_letters = [REVERSE_DICT.get(letter, '?') for letter in letters]
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)


def main():
    print("Morse Code Translator")
    print("Type '1' to translate Text to Morse")
    print("Type '2' to translate Morse to Text")
    choice = input("Enter your choice: ")

    if choice == '1':
        text = input("Enter text: ")
        print("Morse Code:", text_to_morse(text))
    elif choice == '2':
        morse = input("Enter Morse code (use space between letters and '/' between words): ")
        print("Text:", morse_to_text(morse))
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
