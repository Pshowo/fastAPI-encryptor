from vigenere.encryptor import encrypt

def test_encrypt():
    # Encrypting word
    assert encrypt("BEDE", "DAFE") == "EECC"
    assert encrypt("BACA", "DAFE") == "EECC"