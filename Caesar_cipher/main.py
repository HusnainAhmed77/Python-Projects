from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a']

def encrypt(text, shift):
    for i in range(0, text_size):
        f = text[i]
        if f in alphabet:
            l = alphabet.index(f)
            a = l + shift    
            encoded_text.append(alphabet[a])
        else:
            encoded_text.append(text[i])
    print(''.join(encoded_text))

def decode(text, shift):
    for i in range(0, text_size):
        f = text[i]
        if f in alphabet:
            l = alphabet.index(f)
            a = l - shift    
            decoded_text.append(alphabet[a])
        else:
            decoded_text.append(text[i])
    print(''.join(decoded_text))

print(logo)

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    encoded_text = []
    decoded_text = []
    text_size = len(text)

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decode(text, shift)
    else:
        print("error")

    result = input("Type 'yes' if you want to continue using this program or type 'no': ")
    if result == "no":
        should_continue = False
        print("GoodBye! Thanks for using this program")


