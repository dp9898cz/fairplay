import unicodedata
from collections import OrderedDict

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cisla = '0123456789'


def filtraceKlice(klic):

    # odstranění diakritiky
    klic = unicodedata.normalize('NFKD', klic).encode('ascii', 'ignore').decode()
    # nahrazeni mezer
    klic = klic.replace(" ", "")
    # velká písmena
    klic = klic.upper()
    # odstranění dalších znaků
    klic = ''.join(znak if znak in abeceda else '' for znak in klic)
    # odstranění duplicit
    klic = "".join(OrderedDict.fromkeys(klic))

    return klic


def filtraceTextu(text):

    # odstranění diakritiky
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    # konvertování mezer
    text = text.replace(" ", "XSPACEX")
    # velká písmena
    text = text.upper()
    # odstranění dalších znaků
    text = ''.join(znak if znak in abeceda else '' for znak in text)

    return text


def vytvoritTabulku(klic):
    klic = filteredKey
    matrix = [[0 for i in range(5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    # add the key to the matrix
    for pismeno in klic:
        if pismeno not in letters_added:
            matrix[row][col] = pismeno
            letters_added.append(pismeno)
        else:
            continue
        if (col == 4):
            col = 0
            row += 1
        else:
            col += 1
    # Add the rest of the alphabet to the matrix
    # A=65 ... Z=90
    for letter in range(65, 91):
        if letter == 74:  # I/J are in the same position
            continue
        if chr(letter) not in letters_added:  # Do not add repeated letters
            letters_added.append(chr(letter))

   # print (len(letters_added), letters_added)
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index += 1
    return matrix


def separate_same_letters(text):
    index = 0
    while (index < len(text)):
        l1 = text[index]
        if index == len(text)-1:
            text = text + 'X'
            index += 2
            continue
        l2 = text[index+1]
        if l1 == l2:
            text = text[:index+1] + "X" + text[index+1:]
        index += 2
    return text


def indexOf(letter, matrix):
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return (i, index)
        except:
            continue


def sifrovat(text, matrix):
    cipher_text = ''
    for (l1, l2) in zip(text[0::2], text[1::2]):
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)
        if row1 == row2:  # Rule 2, the letters are in the same row
            cipher_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Rule 3, the letters are in the same column
            cipher_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Rule 4, the letters are in a different row and column
            cipher_text += matrix[row1][col2] + matrix[row2][col1]

    return " ".join(cipher_text[i:i + 5] for i in range(0, len(cipher_text), 5))


def desifrovat(text, matrix):
    text = text.replace(" ", "")
    cipher_text = ''
    for (l1, l2) in zip(text[0::2], text[1::2]):
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)
        if row1 == row2:  # Rule 2, the letters are in the same row
            cipher_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Rule 3, the letters are in the same column
            cipher_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Rule 4, the letters are in a different row and column
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    cipher_text = cipher_text.replace("XSPACEX", " ")
    return cipher_text


if __name__ == "__main__":
    klic = None
    while (klic == None):
        filteredKey = filtraceKlice(input("Zadej klíč: "))
        if len(filteredKey) < 4:
            print("Minimální délka klíče musí být 4 neduplicitni znaky a bez čísel, zkus to znovu.")
        else:
            klic = filteredKey

    matrix = vytvoritTabulku(klic)
    print(matrix)

    text = filtraceTextu(input("Zadej text pro šifrování: "))
    print("Zadaný text po filtraci: " + text)

    text = separate_same_letters(text)
    print("Zadaný text po rozdeleni stejnych pismen: " + text)

    cipher = sifrovat(text, matrix)
    print("Šifrovaný text: " + cipher)

    decipher = desifrovat(cipher, matrix)
    print("Znovu dešifrovaný text: " + decipher)
