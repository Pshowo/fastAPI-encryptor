# fastAPI-encryptor

## Task
Implementacja dowolnego szyfru:
- [ ] obsługiwane znaki - alfabet łaciński (case sensitive), cyfry, znaki interpunkcyjne i
białe znaki (minimum to spacja, tabulator, znak nowej linii),
- [x] implementacja metod encode i decode dla wybranego algorytmu,
- [x] testy jednostkowe,
- [x] serwer FastAPI wykorzystujący zaimplementowane metody,
- [ ] autoryzacja BasicAuth do powyższego serwera,
- [ ] dokumentacja kodu oraz README,
- [ ] (opcjonalnie) dockeryzacja rozwiązania.

## Info

Link to API: https://fastapiencryptor.herokuapp.com/

        root/
          |- v1/ ( GET info )
              |- vigenere/ ( GET cipher )
                    |- encryptor/ ( POST messege to encode, auth* )
                    |- decryptor/ ( POST closed message to decode, auth* ) 

## Todo
1. FastAPI
    - [x] utworzyć serwer FASTApi
    - [x] dodać linki do testu połączenia
    - [x] deploy server
    - [x] ustawić automatic deploy
    - [ ] dodać autoryzację 
2. Szyfr
    - [x] utworzyć prosty system szyfrowania 
    - [x] utworzyć prosty system deszyfrowania
    - [x] dodać szyfrowanie do serwera fastapi
    - [x] dodac rozszyfrowanie do serwera fastapi
    - [ ] skomplikować szyfr  

3. Opcjonalnie
    - [ ] utworzyć złożony system szyfrowania RSA
