import math
import decimal
import random
import requests


class RSA:

    def __init__(self):
        self.prime_num = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
        self.__d_key = 0
        self.n = 0
        self.p1 = 53
        self.p2 = 59
        self.e = self.e_cal()

    def __str__(self):
        print("p1: ", self.p1, "\tp2:", self.p2)
        print("e: ", self.e, "\tn:", self.n)
        print("key:", self.__d_key)
        
        return "-"*20

    def e_cal(self):
        self.n = self.p1 * self.p2
        fi_n = (self.p1-1) * (self.p2-1)
        e = 2
        while math.gcd(e, fi_n) != 1:
            e += 1
        
        if e >= fi_n:
            return print('error')

        self.__d_key = (2 * fi_n + 1) / e
        return e

    def close_msg(self, digit_msg, e, n):
        if digit_msg > 100 or digit_msg < 0:
            digit_msg = 100
        close_msg = pow(digit_msg, e) % n
        return close_msg

    def get_key(self,):
        return self.n, self.e

    def wolfram(self, c_msg, n):
        print(f"Wolfram calculated: Mod[ {c_msg} ^ {int(self.__d_key)}, {n}]")
        url = f"http://api.wolframalpha.com/v2/query?input=Mod%5B{c_msg}%5E{int(self.__d_key)},{n}%5D&appid=422X27-2TRGXAKYK9"
        res_wolfram = requests.get(url)
        from xml.etree import ElementTree
        root = ElementTree.fromstring(res_wolfram.content)

        for pod in root.iter("pod"):
            if pod.attrib['title'] == "Result":
                for subpod in pod:
                    for child in subpod:
                        if child.tag == "plaintext":
                            return child.text

if __name__ == "__main__":

    r = RSA()
    print(r)
    print("=== RSA ===")
    open_msg = int(input("Insert open msg:"))
    a = r.close_msg(open_msg)
    print("Open msg:", open_msg)
    print("Closed msg:", a)
    res = r.wolfram(a)
    print("Result: ", res, open_msg == int(res))
    print("=== === ===")

