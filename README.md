# fastAPI-encryptor

## Task
Implementacja dowolnego szyfru:
- [ ] obsługiwane znaki - alfabet łaciński (case sensitive), cyfry, znaki interpunkcyjne i
białe znaki (minimum to spacja, tabulator, znak nowej linii),
- [ ] implementacja metod encode i decode dla wybranego algorytmu,
- [ ] testy jednostkowe,
- [ ] serwer FastAPI wykorzystujący zaimplementowane metody,
- [ ] autoryzacja BasicAuth do powyższego serwera,
- [ ] dokumentacja kodu oraz README,
- [ ] (opcjonalnie) dockeryzacja rozwiązania.

## Todo
1. FastAPI
    - [x] utworzyć serwer FASTApi
    - [x] dodać linki do testu połączenia
    - [ ] deploy server
    - [ ] ustawić CI z github main
    - [ ] dodać autoryzację 
2. Szyfr
    - [x] utworzyć prosty system szyfrowania 
    - [x] utworzyć prosty system deszyfrowania
    - [x] dodać szyfrowanie do serwera fastapi
    - [ ] dodac rozszyfrowanie do serwera fastapi
    - [ ] skomplikować szyfr  

3. Opcjonalnie
    - [ ] utworzyć złożony system szyfrowania RSA