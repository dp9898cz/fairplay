
from numbers import numbers

def indexOf(letter, matrix):
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return (i, index)
        except:
            continue


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
    return cipher_text


def finalize(text, separator, separator2):
    text = text.replace("XSPACEX", " ")
    for number in numbers:
        text = text.replace(numbers[number], number)
    return text
