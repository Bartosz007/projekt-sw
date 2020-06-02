# EVB 5.1

##### Projekt jest realizowany w oparciu o komunikację klient-serwer.
   - Używane do tego są sockety.
   - Klient pełni rolę płytki EVB5.1
   - Serwer pełni rolę hosta.
  
Napisana jest prosta biblioteka socket_io.py do prostszej obsługi połączeń.
Pliki:
* klient.py - klient
* serwer.py - serwer
* evb_gui.py - plik zawierający funkcje budujące GUI 
* socket_io.py - zawiera funkcje związane z socketami
* client_functions.py - zawiera funkcje realizowane po stronie klienta
* serwer_functions.py - zawiera funkcje realizowane po stronie klienta


> Nie zmieniajcie pliku socket_io.py
> Dbajcie o porządek
> Zanim zaczniecie pracę, przecyztajcie kod i komentarze

Aby wszystko działało jak należy:
1. Utworzyć funkcje obsługującą okreslone zdarzenie w GUI w pliku client_functions.py
2. Przypisać tą funkcję do okreslonego elementu GUI w pliku evb_gui.py (najlepiej pod koniec pliku)
3. Doidać reakcję na odpowiedni typ komunikatu - plik serwer.py -funkcja communicates
4. Napisać funkcję reagującą na ten komunikat(obliczenia i takie tam) w pliku server_funcions.py

Autorzy:
* Bartosz Krawczyk
* Robert Kozik
* Mateusz Krasiński
* Krzysztof Kurzak
