# fastAPI-encryptor

## About

API with cipher algorithm to encrypt and decrypt a message using by Vigenère cipher.
Key alphabet consists of 95 chars. For each row aplhabet was shuffle.
Script can encoded any alphabet, it's only write string coinain required characters in atribute class Vigenere.
The key lenght can be modify, default value is 8 chars. Max key length the is limited by length message.

## Hot to use it?
To use it simple way you can use an applications like this [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/).
***
API is avaiable on: https://fastapiencryptor.herokuapp.com/

API docs: https://fastapiencryptor.herokuapp.com/docs
***

Authentication: **admin** pass: **qwerty**

    root/
        |- v1/ ( GET info )
            |- vigenere/ ( GET cipher )
                    |- encryptor/ ( POST messege to encode, auth* )
                    |- decryptor/ ( POST closed message to decode, auth* )
            |
            |- RSA/ (GET cipher)
                    |- encryptor/ ( POST messege to encode, auth* )
                    |- decryptor/ ( POST closed message to decode, auth* )

GET basic info:

    GET https://fastapiencryptor.herokuapp.com/

GET avaiable methods:

    GET https://fastapiencryptor.herokuapp.com/v1/vigenere/

POST open message to encode (required basic authentication):

    1. JSON

    POST https://fastapiencryptor.herokuapp.com/v1/vigenere/encryptor/
    {   "msg": "This message will be encoded"   }

    2. JSON and parameter "q"

    POST http://127.0.0.1:8000/v1/vigenere/encryptor/?q=sampleTextToEncode
    {"msg": ""}

POST closed message and key to decode (required basic authentication):
    
    JSON

    POST https://fastapiencryptor.herokuapp.com/v1/vigenere/decryptor/
    {  "msg": "fa4y5Ń",  "key": "fU]=V~"   }

## Task
Implementacja dowolnego szyfru:
- [x] obsługiwane znaki - alfabet łaciński (case sensitive), cyfry, znaki interpunkcyjne i
białe znaki (minimum to spacja, tabulator, znak nowej linii),
- [x] implementacja metod encode i decode dla wybranego algorytmu,
- [x] testy jednostkowe,
- [x] serwer FastAPI wykorzystujący zaimplementowane metody,
- [x] autoryzacja BasicAuth do powyższego serwera,
- [x] dokumentacja kodu oraz README,
- [ ] (opcjonalnie) dockeryzacja rozwiązania.

## Test

Coverage main:

![img.png](additionalfiles\img\img.png)

Coverage vigenere:

![img_1.png](additionalfiles\img\img_1.png)


