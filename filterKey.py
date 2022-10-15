import unicodedata
from collections import OrderedDict

from alphabet import abeceda


def filtraceKlice(klic, lan):
    # odstranění diakritiky
    klic = unicodedata.normalize('NFKD', klic).encode('ascii', 'ignore').decode()
    # nahrazeni mezer
    klic = klic.replace(" ", "")
    # velká písmena
    klic = klic.upper()
    # j==i | w==v
    if (lan == "en"):
        klic = klic.replace("J", "I")
    else:
        klic = klic.replace("W", "V")
    # odstranění dalších znaků
    klic = ''.join(znak if znak in abeceda else '' for znak in klic)
    # odstranění duplicit
    klic = "".join(OrderedDict.fromkeys(klic))

    if (len(klic) < 4):
        return None

    return klic
