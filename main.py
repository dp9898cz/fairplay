import unicodedata
import sys  # arguments
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
    # j==i
    klic = klic.replace("J", "I")
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
    # j==i
    text = text.replace("J", "I")
    # odstranění dalších znaků
    text = ''.join(znak if znak in abeceda else '' for znak in text)

    return text


""" def vytvoritTabulku(klic):
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
        if letter == 74:  # I(74)/J(75) are in the same position
            continue
        if chr(letter) not in letters_added:  # Do not add repeated letters
            letters_added.append(chr(letter))

    # print (len(letters_added), letters_added)
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index += 1
    return matrix """


def create_fill_matrix(characters):
    matrix = [[0 for i in range(5)] for j in range(5)]
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = characters[index]
            index += 1
    return matrix


def make_matrix(key):
    characters = abeceda.replace('J', '')  # j==i
    index = 0
    for char in key:
        characters = characters.replace(char, "")
    return create_fill_matrix(key + characters)


""" def separate_same_letters(text):
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
    return text """


def get_avaiable_separator(text):
    for char in abeceda.replace("J", "I"):  # J==I
        if not char in text:
            # choose character not used in text as separator
            return char
    return 'X'  # default


def separate_letters(text, separator):
    resolved = False
    while (not resolved) and len(text) != 0:
        for idx, char in enumerate(text):
            if (idx > 0 and char == text[idx - 1]):
                # found two characters next to each other
                text = text[:idx] + separator + text[idx:]
                break
            if (idx == len(text) - 1):
                # reached the end, we can safely mark this string as resolved
                resolved = True
    return text


def check_even_length(text, separator):
    if len(text) % 2 == 1:
        return text + separator
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


def desifrovat(text, matrix, separator):
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
    cipher_text = cipher_text.replace(separator, "")
    return cipher_text


if __name__ == "__main__":
    klic = None
    text = None
    if (len(sys.argv) == 3):
        klic = filtraceKlice(sys.argv[1])
        text = filtraceTextu(sys.argv[2])
    while (klic == None):
        filteredKey = filtraceKlice(input("Zadej klíč: "))
        if len(filteredKey) < 4:
            print("Minimální délka klíče musí být 4 neduplicitni znaky a bez čísel, zkus to znovu.")
        else:
            klic = filteredKey

    matrix = make_matrix(klic)
    print(matrix)

    if (not text):
        text = filtraceTextu(input("Zadej text pro šifrování: "))
    print("Zadaný text po filtraci: " + text)

    separator = get_avaiable_separator(text)
    text = separate_letters(text, separator)
    text = check_even_length(text, separator)
    print("Zadaný text po rozdeleni stejnych pismen: " + text)

    cipher = sifrovat(text, matrix)
    print("Šifrovaný text: " + cipher)

    decipher = desifrovat(cipher, matrix, separator)
    print("Znovu dešifrovaný text: " + decipher)
