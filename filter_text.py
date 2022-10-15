import unicodedata

from alphabet import abeceda


def filtraceTextu(text, lan):
    # odstranění diakritiky
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    # konvertování mezer
    text = text.replace(" ", "XSPACEX")
    # velká písmena
    text = text.upper()
    # j==i
    if (lan == "cz"):
        text = text.replace("W", "V")
    else:
        text = text.replace("J", "I")
    # odstranění dalších znaků
    text = ''.join(znak if znak in (abeceda + "9") else '' for znak in text)

    return text
