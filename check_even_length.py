def check_even_length(text, separator, separator2):
    if len(text) % 2 == 1:
        return text + (separator if separator != text[len(text) - 1] else separator2)
    return text
