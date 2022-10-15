from alphabet import abeceda


def create_fill_matrix(characters):
    matrix = [[0 for i in range(5)] for j in range(5)]
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = characters[index]
            index += 1
    return matrix


def make_matrix(key, lan):
    if (lan == "en"):
        characters = abeceda.replace('J', '')
    else:
        characters = abeceda.replace('W', '')
    index = 0
    for char in key:
        characters = characters.replace(char, "")
    return create_fill_matrix(key + characters)
