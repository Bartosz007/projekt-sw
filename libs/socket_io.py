import socket

# UWAGA! - proszę pod żadnym pozorem nic nie modyfikować w tym pliku


# komunikacja wyglądać będzie tak:
# klient łączy się z serwerem, aby serwer otrzymał dane do komunikacji

# serwer zaczyna nasłuchiwać, czekając na komunikaty
# zdarzenia wywołane użyciem gui, klient wysyła do serewera komunikat
# klient zaczyna nasłuchiwać, oczekując na odpowiedź serwera
# serwer wykonuje określoną funkcje w zalezności od typu komunikatu, wysyła odpowiedź do klienta
# klient otrzymuje odpowiedź serwera i wykonuje akcje
# komunikat: 10 pierwszych znaków to nagłowek(w tym długość komunikatu i spacje)
# komunikat: 11 znak to numer komunikatu
# komunikat: $ - jest znakiem odzielającym kolejne sekcje w treści komunikatu
# komunikat: @ - ostatni znak komunikatu


HEADER_LENGTH = 10  # długośc nagłówka
IP = "127.0.0.1"  # pętla zwrotna, serwer jest lokalnie, to wskazujemy na siebie
PORT = 7070  # port, może być dowolny, byleby nie był zajęty
LENGTH = 64  # długość ramki/fragmentu danych - umożliwia wysłanie komunikatu o dowolnej długości
LOCK = True
REC_LOCK = True
send_array = []
rec_array = []


# otwarcie połączenia
def open_connection():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((IP, PORT))

    full_msg = ""
    new_msg = True
    while True:
        msg = connection.recv(LENGTH)
        if new_msg:
            msglen = int(msg[:HEADER_LENGTH])
            new_msg = False

        full_msg = full_msg + msg.decode("utf-8")

        if len(full_msg) - HEADER_LENGTH == msglen:  # długość = nagłówek + treść
            # print("Wiadomość powitalna od serwera: ")
            # print(full_msg[HEADER_LENGTH:])
            break

    return connection


# zamknięcie połączenia
def close_connection(connection):
    connection.close()


# odebranie wiadomości
def receive(connection):
    global LOCK, REC_LOCK, rec_array
    full_msg = ""
    new_msg = True

    while True:
        msg = connection.recv(LENGTH)
        if new_msg:
            msglen = int(msg[:HEADER_LENGTH])
            new_msg = False

        full_msg = full_msg + msg.decode("utf-8")
        if len(full_msg) - HEADER_LENGTH == msglen:
            # print("Otrzymano odpowiedź o treści: ")
            # print(full_msg)
            LOCK = True
            return full_msg[HEADER_LENGTH:]  # zwraca tylko treść komunikatu


# wysłanie wiadomości
def send(connection, msg):
    global LOCK, send_array
    if LOCK:
        LOCK = False
        # print("Wysłano komunikat o treści: ")
        msg = f"{len(msg):<{HEADER_LENGTH}}" + msg
        # print(msg)
        connection.send(bytes(msg, "utf-8"))
    else:
        send_array.append(msg)
        try:
            se = send_array[0]
            del send_array[0]
            send(connection, se)
        except IndexError:
            pass
            # print("Pusta tablica")


def release_lock():
    global LOCK
    LOCK = True
