import numpy as np
import random

class Vigenere:

    def __init__(self):
        self.alphabet = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        self.table = self.table()
        self.key = ""

    def __str__(self):
        return str(self.table)

    def table(self):
        """Generate cipher table

        Returns
        -------
        [numpy arr]
            Cipher table
        """
        table = np.array([['A', 'B', 'C', 'D', 'E', 'F']])
        for i in range(1 , len(self.alphabet)):
            table = np.append(table, [np.roll(self.alphabet, -i)], axis=0)
        return table

    def encrypt(self, msg, **kwargs):
        """Encrypts message using by Vigenere method. 

        Parameters
        ----------
        msg : [str]
            Message to encrypting.

        Returns
        -------
        [touple(msg, key)]
            Touple with encrypted message and the key which a message will be encrypted.
        """
        closed_msg = ""
        if 'key' in kwargs:
            self.key = kwargs['key']
        else:
            self.key = "".join(random.choice(self.alphabet) for _ in range(len(msg)))
        assert len(msg) == len(self.key), "Wrong length message or key."
        
        for char in range(len(msg)):
            x0 = np.argwhere(self.table[0] == msg[char])
            x1 = np.argwhere(self.table[:, [0]] == self.key[char])
            closed_msg += self.table[x0[0][0]][x1[0][0]]
        return closed_msg, self.key

    def decrypt(self, c_msg, key):
        """Decodes cipher message.

        Parameters
        ----------
        c_msg : [str]
            Closed message.
        key : [str]
            Key to open the message

        Returns
        -------
        [str]
            Decrypted message
        """
        open_msg = ""
        for char in range(len(c_msg)):
            x1 = np.argwhere(self.table[:, [0]] == key[char])
            x0 = np.argwhere(self.table[x1[0][0]] == c_msg[char])
            open_msg += self.table[x0[0][0]][0]
        return open_msg

