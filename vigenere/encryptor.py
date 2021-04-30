import numpy as np
import string
import random

class Vigenere:

    def __init__(self, alphabet, **kwargs):
        self.raw_alphabet = alphabet
        self.alphabet = self.gen_alphabet(self.raw_alphabet)
        self.key_length = kwargs['key_length'] if "key_length" in kwargs else 8
        self._ke = None
        self.table = self.gen_table()

    def __str__(self):
        print("Raw alphabet:", self.raw_alphabet)
        print("Key length:", self.key_length)
        return str(self.table)

    def gen_alphabet(self, alphabet):
        """Based on the input alphabet, the method generated an array. 
        If char appears twice or more in the alphabet, the rest of them removed.

        Parameters
        ----------
        alphabet : [str]
            A string containing all chars to use.

        Returns
        -------
        [np.array]
            1d array with chars
        """
        # 
        for char_ in alphabet:
            if alphabet.count(char_) > 1:
                print("Double:", char_)
                alphabet = alphabet.replace(char_, "")

        " " + alphabet
        return np.array([char_ for char_ in alphabet])

    def gen_table(self):
        """Generate cipher table. Each row is shifted on a random in both directions.

        Returns
        -------
        [numpy arr]
            Cipher table.
        """
        key_alphabet = " " + string.ascii_letters + string.digits + string.punctuation
        self._ke = [char for char in key_alphabet]  # List of chars to generate a random key
        ke_ = np.array([[char] for char in key_alphabet])
        table = np.array([np.copy(self.alphabet)])

        for i in range(0, len(ke_)-1):
            i = random.randrange(-len(self.raw_alphabet), len(self.raw_alphabet))
            table = np.append(table, [np.roll(self.alphabet, i)], axis=0)
        table = np.append(ke_, table, axis=1)
        return table

    def encrypt(self, msg):
        """Encrypts message using by Vigenere method. 

        Parameters
        ----------
        msg : [str]
            Message to encrypting.

        Returns
        -------
        [tuple(msg, key)]
            Tuple with encrypted message and the key, which a message will be decrypted.
        """
        if msg == "":
            return "Message is empty. Write the message to encode.", -1
        else:
            closed_msg = ""
            key_range = self.key_length if len(msg) >= self.key_length else len(msg)
            key = "".join(random.choice(self._ke[1:]) for _ in range(key_range))
            k = 0

            for char in range(len(msg)):
                if msg[char] not in self.raw_alphabet:
                    return f'This: "{msg[char]}" character is not available. Replace it for similar.', -1
                if k == len(key):
                    k = 0
                x0 = np.argwhere(self.table[0][1:] == msg[char])[0][0] + 1
                x1 = np.argwhere(self.table[1:, [0]] == key[k])[0][0] + 1
                closed_msg += self.table[x1][x0]
                k += 1
            return closed_msg, key

    def decrypt(self, c_msg, key):
        """Decodes cipher message.

        Parameters
        ----------
        c_msg : [str]
            Closed message.
        key : [str]
            Key to open the message.

        Returns
        -------
        [str]
            Decrypted message.
        """
        if c_msg == "":
            return "No message. Write encoded message."
        if key == "" or key == -1:
            return "No key. Write the key attached with the encoded message."
        else:
            open_msg = ""
            k = 0
            for char in range(len(c_msg)):
                if k == len(key):
                    k = 0
                x1 = np.argwhere(self.table[1:, [0]] == key[k])[0][0] + 1  # Finds char in key column
                x0 = np.argwhere(self.table[x1][1:] == c_msg[char])[0][0]  # Finds char in particular row
                open_msg += self.table[0][1:][x0]
                k += 1
            return open_msg
