
def separate_letters(text, separator, separator2):
    resolved = False
    while (not resolved) and len(text) != 0:
        for idx, char in enumerate(text):
            if (idx > 0 and char == text[idx - 1]):
                # found two characters next to each other
                text = text[:idx] + (separator if char != 'X' else separator2) + text[idx:]
                break
            if (idx == len(text) - 1):
                # reached the end, we can safely mark this string as resolved
                resolved = True
    return text
