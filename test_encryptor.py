from vigenere.encryptor import Vigenere
import pytest
import unittest
import string

alphabet = string.printable

def test_vigenere_init():
    v = Vigenere(alphabet)
    assert v

alph = string.ascii_letters + string.digits


def test_table():
    v = Vigenere("ABCDEF")
    assert """[['A' 'B' 'C' 'D' 'E' 'F']
 ['B' 'C' 'D' 'E' 'F' 'A']
 ['C' 'D' 'E' 'F' 'A' 'B']
 ['D' 'E' 'F' 'A' 'B' 'C']
 ['E' 'F' 'A' 'B' 'C' 'D']
 ['F' 'A' 'B' 'C' 'D' 'E']]"""


# @pytest.mark.xfail
def test_encrypt():
    # if length open message is equal length decoded message
    v = Vigenere(alphabet)
    t1 = v.encrypt("BEDE")
    assert len(t1[0]) == len("BEDE") and len(t1[1]) == len("BEDE")
    t1 = v.encrypt("B")
    assert len(t1[0]) == len("B") and len(t1[1]) == len("B")
    t1 = v.encrypt("BEDEBACA")
    assert len(t1[0]) == len("BEDEBACA") and len(t1[1]) == len("BEDEBACA")
    t1 = v.encrypt("    BACA")
    assert len(t1[0]) == len("    BACA") and len(t1[1]) == len("    BACA")
    t1 = v.encrypt("BEDE    BACA")
    assert len(t1[0]) == len("BEDE    BACA") and len(t1[1]) == 8


    # if message is empty
    t1 = v.encrypt("")
    assert t1[0] == "Message is empty. Write the message to encode." and t1[1] == -1

    # if key length is different
    v = Vigenere(alphabet, key_length=12)
    t1 = v.encrypt("BEDE    BACA O PANIE O BEDE")
    assert len(t1[0]) == len("BEDE    BACA O PANIE O BEDE") and len(t1[1]) == 12
    v = Vigenere(alphabet, key_length=12)
    t1 = v.encrypt("BEDE")
    assert len(t1[1]) == 4
    v = Vigenere(alphabet, key_length=2)
    t1 = v.encrypt("BEDE    BACA O PANIE O BEDE")
    assert len(t1[1]) == 2

    # if appear char which is unavailable
    v = Vigenere("ABCDEF")
    t1 = v.encrypt("żółć")
    assert t1[0] == 'This: "ć" character is not available. Replace it for similar.' and t1[1] == -1
    t1 = v.encrypt("Aółć")
    assert t1[0] == 'This: "ć" character is not available. Replace it for similar.' and t1[1] == -1


def test_decrypt():
    v = Vigenere(alphabet)
    t1 = v.decrypt("BEDEBACA", "lHf4*PwdlDe0")
    assert t1 != "BEDEBACA"

    # if missing message / message and key / key
    t1 = v.decrypt("", "lHf4*PwdlDe0")
    assert t1 == "No message. Write encoded message."
    t1 = v.decrypt("", "")
    assert t1 == "No message. Write encoded message."
    t1 = v.decrypt("TEST", "")
    assert t1 == "No key. Write the key attached with the encoded message."


def test_encrypt_decrypt():
    v = Vigenere(alphabet)
    t1 = v.encrypt("BEDEBACA")
    t2 = v.decrypt(t1[0], t1[1])
    assert "BEDEBACA" == t2
    t1 = v.encrypt("B")
    t2 = v.decrypt(t1[0], t1[1])
    assert "B" == t2
    t1 = v.encrypt("    BACA")
    t2 = v.decrypt(t1[0], t1[1])
    assert "    BACA" == t2
    v = Vigenere(alphabet, key_length=2)
    t1 = v.encrypt("    BACA")
    t2 = v.decrypt(t1[0], t1[1])
    assert "    BACA" == t2

    # used special characters
    PL_ext = "ąćęłńóśźżĄĘĆŁŃÓŚŹŻ"
    v = Vigenere(string.printable + PL_ext)
    t1 = v.encrypt("""Zażółć, gęślą jaźńDwa(2)#zAŻÓŁĆ: gĘŚŁĄ-JAŹŃ#..2:!""")
    t2 = v.decrypt(t1[0], t1[1])
    assert """Zażółć, gęślą jaźńDwa(2)#zAŻÓŁĆ: gĘŚŁĄ-JAŹŃ#..2:!""" == t2

    t1 = v.encrypt("""Zażółć, gęślą jaźń 
    Dwa(2) #zAŻÓŁĆ: gĘŚŁĄ-JAŹŃ#..2:!""")
    t2 = v.decrypt(t1[0], t1[1])
    assert """Zażółć, gęślą jaźń 
    Dwa(2) #zAŻÓŁĆ: gĘŚŁĄ-JAŹŃ#..2:!""" == t2





