MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    message_list = message.split(' ')
    morse_code = ""
    for idx, word in enumerate(message_list):
        for i, c in enumerate(word):
            morse_code += f"{MORSE_CODE_DICT[c.upper()]}"
            if i != len(word) - 1:
                morse_code += " "
        if idx != len(message_list) - 1:
            morse_code += '/'
    return morse_code


while True:
    print("Hello! Welcome to text Encryption")
    message = input("Input your message: ")
    morse_code = encrypt(message)
    print(f"Your message in morse code: {morse_code}")
    repeat = True
    while repeat:
        options = input("Encrypt another message? (y/n)")
        if options == 'y':
            break
        elif options == 'n':
            repeat = False
    if not repeat:
        print("Thank you!")
        break
