
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
    resolved = False
    while (not resolved) and len(text) != 0:
        for idx, char in enumerate(text):
            if (char == separator or char == separator2):
                if (idx > 0 and idx < len(text) - 2 and (text[(idx - 1)] != text[idx + 1]) and text[(idx - 1)] != text[idx]):
                    # delete separator
                    text = text[:idx] + text[idx + 1:]
                    break
            if (idx == len(text) - 1):
                # reached the end, we can safely mark this string as resolved
                resolved = True
    if (text[len(text) - 1] == separator or text[len(text) - 1] == separator2):
        text = text[:len(text) - 1]
    return text
