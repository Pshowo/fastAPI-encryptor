import numpy as np

class Vigenere:

    def __init__(self):
        self.alphabet = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        self.table = self.table()

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

    def encrypt(self, msg, key):
        """Encrypts message using by Vigenere method. 

        Parameters
        ----------
        msg : [str]
            Message to encrypting.
        key : [str]
            The key which a message will be encrypted.
        Returns
        -------
        [str]
            Encrypted message.
        """
        closed_msg = ""
        return closed_msg
