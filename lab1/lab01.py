alphabet_ceaser = "abcdefghijklmnopqrstuvwxyz"

def shifr_ceaser(input_text, k=3):
    global alphabet_ceaser
    output_text = ""
    for char in input_text:
        if char in alphabet_ceaser:
            output_text += alphabet_ceaser[(alphabet_ceaser.index(char)+k) % 26]
        else:
            output_text += char
    return output_text

def shifr_atbash(input_text, alphabet="abcdefghijklmnopqrstuvwxyz"):
    output_text = ""
    len_alp = len(alphabet)
    for char in input_text:
        if char in alphabet:
            output_text += alphabet[len_alp - alphabet.index(char)-1]
        else:
            output_text += char

    return output_text

if __name__ == "__main__":
    input_text = "my name is - kostya"
    print(shifr_ceaser(input_text,3))

    alphabet_atbash = "abcdefghijklmnopqrstuvwxyz"
    atbash_text = "az"
    print(shifr_atbash(atbash_text))
