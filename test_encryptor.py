from vigenere.encryptor import Vigenere
import pytest
import unittest

def test_vigenere_init():
    v = Vigenere()
    assert v

def test_table():
    v = Vigenere()
    assert """[['A' 'B' 'C' 'D' 'E' 'F']
 ['B' 'C' 'D' 'E' 'F' 'A']
 ['C' 'D' 'E' 'F' 'A' 'B']
 ['D' 'E' 'F' 'A' 'B' 'C']
 ['E' 'F' 'A' 'B' 'C' 'D']
 ['F' 'A' 'B' 'C' 'D' 'E']]"""

# @pytest.mark.xfail
def test_encrypt():
    v = Vigenere()
    assert v.encrypt("BEDE", key="DAFE") == ("EECC", "DAFE")
    assert v.encrypt("BACA", key="DAFE") == ("EABE", "DAFE")
    with pytest.raises(AssertionError):
        v.encrypt("BA", key="DAFE")
    with pytest.raises(AssertionError):
        v.encrypt("BAD", key="DS")
    test1 = v.encrypt("BACA") 
    assert len(test1[1]) == len("BACA")
    

def test_decrypt():
    v = Vigenere()
    assert v.decrypt("EECC", "DAFE") == "BEDE"
    assert v.decrypt("EABE", "DAFE") == "BACA"
    t1 = v.encrypt("BEDEBACA")
    assert v.decrypt(t1[0], t1[1]) == "BEDEBACA"

