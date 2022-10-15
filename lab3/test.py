def genKey(msg, key):
    key.replace(' ','')
    msg.replace(' ', '')
    key = list(key)
    if len(msg) == len(key):
        return(key)
    else:
        for i in range(len(msg) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def vig(msg, key):
    cipher_text = []
    # убираем пробелы, потому что мы их ненавидим
    msg.replace(' ', '')
    #key.replace(' ','')
    for i in range(len(msg)):
        x = (ord(msg[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def unvig(cipher_text, key):
    orig_text = []
    #key.replace(' ','')
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


msg = 'Some text here'
key = 'math'
print(vig(msg, genKey(msg,key)))