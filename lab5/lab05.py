rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def marsh_shifr(input_text, key_sh, m, n):
    global rus

    input_text_ws = input_text.replace(' ', '')

    if len(input_text_ws) < m*n:
        input_text_ws += rus[:m*n-len(input_text_ws)]
    
    text = iter(input_text_ws)

    matrix = [[next(text) for y in range(m)] for x in range(n)]

    ps = [rus.index(x) for x in key_sh]
    pss = sorted(ps)

    output_text = ''

    for letter in pss:
        for x in range(n):
            output_text += matrix[x][ps.index(letter)]

    return output_text


def zadan_2():
    import numpy as np
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    k = 2
    k_2 = [x+1 for x in range(k*k)]

    matrix = [[0 for x in range(2*k)]for y in range(2*k)]
    matrix = np.array(matrix)
    for x in range(k*k):
        coun = 0
        for x in range(k):
            for y in range(k):
                matrix[x][y] = k_2[coun]
                coun += 1
        matrix = np.rot90(matrix)

    d_s = {k: 0 for k in k_2}
    d_ss = {1:2, 2:4, 3:3, 4:3}

    for x in range(k*k):
        for y in range(k*k):
            d_s[matrix[x][y]] += 1
            if d_s[matrix[x][y]] != d_ss[matrix[x][y]]:
                matrix[x][y] = -1
            else:
                matrix[x][y] = 0

    input_text_ws = 'договорподписали'
    key_sh = 'шифр'
    count_t = 0

    text = iter(input_text_ws)

    matrix_t = [['O' for y in range(k*k)] for x in range(k*k)]

    for d in range(4):
        for x in range(k*k):
            for y in range(k*k):
                if matrix[x][y] == 0:
                    matrix_t[x][y] = input_text_ws[count_t]
                    count_t += 1
                
        matrix = np.rot90(matrix, -1)

    ps = [rus.index(x) for x in key_sh]
    pss = sorted(ps)

    output_text = ''

    for letter in pss:
        for x in range(k*k):
            output_text += matrix_t[x][ps.index(letter)]

    print(output_text)

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
    msg.replace(' ', '')
    for i in range(len(msg)):
        x = (ord(msg[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def unvig(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


msg = 'Some text here'
key = 'math'
print(vig(msg, genKey(msg,key)))

if __name__ == '__main__': 
    print(marsh_shifr('нельзя недооценивать противника', 'пароль', 6, 5))