from libs.socket_io import *


# przykładowe połączenie
# przez parametr przesłałem przykładowy label do zmiany kolorów
def test_connection(connection, test_label):
    # wysłanie komunikatu, wysyłam tylko treść komunikatu, nagłówek dorobi się sam
    send(connection, "0$changecolor@")  # (połączenie, treść_komunikatu)
    rec = receive(connection)  # odbiór połączenia
    print("Wiadomość od serwera: ")
    print(rec)  # wyświetlenie komunikatu
    test_label.config(bg=rec[2:len(rec) - 1])  # przykładowa obsługa GUI - zmiana kolorów test_label
