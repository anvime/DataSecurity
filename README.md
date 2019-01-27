# Ochrona Danych - Projekt
## Jak uruchomić
     pip install -r requirements.txt
Komenda ta instaluje potrzebne pakiety. Po zainstalowaniu
wymaganych pakietów należy przejść do folderu /src i tam wykonać:

     export FLASK_APP app.py
     flask run
 
## Opis aplikaji

Aplikacja pozwala na:
 - Rejestrację
 - Logowanie
 - Publikowanie oraz usuwanie prywatnych postów
 - Zmianę hasła
 - Odzyskiwanie hasła
 
 Aplikacja działa na localhost. Transmisję zabezpiecza protokół HTTPS. 
 
#### Walidacja danych wejściowych
Wszystkie dane w formularzach przechodzą walidację.
 
 W formularzu do przesyłania postów została wykorzystana blacklista ograniczająca użytkownika do liter cyfr, oraz znaków '.', ',', ' ','!', '?'.
 
#### Ciasteczka
Dzięki atrybutowi HTTP-ONLY w flask-session nie jest możliwe przeglądanie ciasteczek przez JavaScript
  
 #### Przechowywanie hasła
 Hasła oraz odpowiedzi na pytania zabezpieczające są zaszyfrowane algorytmem sha512 z solą.
 
 
 ## Generowanie certyfikatów SSL
 W folderze /src:
 
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
