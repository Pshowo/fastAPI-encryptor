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
    v = Vigenere(alphabet)
    t1 = v.encrypt("BEDE")
    assert len(t1[0]) == len("BEDE")
    assert len(t1[1]) == len("BEDE")
    t1 = v.encrypt("B")
    assert len(t1[0]) == len("B")
    assert len(t1[1]) == len("B")
    t1 = v.encrypt("")
    assert t1[0] == "Message is empty. Write the message to encode."
    assert t1[1] == None
    t1 = v.encrypt("BEDEBACA")
    assert len(t1[0]) == len("BEDEBACA")
    assert len(t1[1]) == len("BEDEBACA")
    t1 = v.encrypt("    BACA")
    assert len(t1[0]) == len("    BACA")
    assert len(t1[1]) == len("    BACA")
    t1 = v.encrypt("BEDE    BACA")
    assert len(t1[0]) == len("BEDE    BACA")
    assert len(t1[1]) == 8
    v = Vigenere(alphabet, key_length=12)
    t1 = v.encrypt("BEDE    BACA O PANIE")
    assert len(t1[0]) == len("BEDE    BACA O PANIE")
    assert len(t1[1]) == 12

def test_decrypt():
    v = Vigenere(alphabet)
    t1 = v.decrypt("BEDEBACA", "lHf4*PwdlDe0")
    assert t1 != "BEDEBACA"
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
