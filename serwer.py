import socket
from libs import socket_io as sockets
import functions.server_funcions as sf

HEADER_LENGTH = 10
IP = "127.0.0.1"  # pętla zwrotna (wskazuje na samego siebie)
PORT = 7070


def communicates(comm):  # funkcja obsługująca treści komunikatów
    print("Otrzymano komunikat o treści: ")
    print(comm)

    if comm[len(comm) - 1] != '@':  # prosty parser wiadomości
        print("ERROR CONNECTION!")
        return -1

    numer = int(comm[0])

    # Tutaj dodajecie swoje typy komunikatów
    # w oparciu o numer komunikatu wywoływana jest funkcja z pliku server_functions
    # tam piszcie swoje strony serwerowe
    # 0 jest zarezerwowane dla połączenia testowego
    # służy ono dla przykładu - w przyszłości zostanie usunięte
    if numer == 0:
        return sf.com0()
    elif numer == 1:
        pass
    elif numer == 2:
        pass
    elif numer == 3:
        pass
    elif numer == 4:
        pass
    elif numer == 5:
        pass
    elif numer == 6:
        pass


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)

    print("Serwer rozpoczął nasłuchiwanie...")

    client, address = server.accept()  # łączenie z klientem

    print(f"Połączono z: {address}!")

    msg = "Witaj plytko EvB5.1"
    sockets.send(client, msg)

    new_msg = True
    full_msg = ""

    # rozpoczęcie nasłuchiwania
    while True:
        try:  # zabezpieczenie, gdy klient się rozłączy, wyrzuci tu błąd
            msg = client.recv(16)

            if new_msg:
                msglen = int(msg[:HEADER_LENGTH])
                new_msg = False

            full_msg = full_msg + msg.decode("utf-8")

            if len(full_msg) - HEADER_LENGTH == msglen:  # jeśli się to spełni, to koniec komunikatu
                res = communicates(full_msg[HEADER_LENGTH:])
                sockets.send(client, res)  # odpowiedź serwera
                full_msg = ""
                new_msg = True

        except ValueError:
            print(f"Rozłączono: {address}!")
            client, address = server.accept()  # łączenie z klientem

            print(f"Ponownie połączono z: {address}!")

            msg = "Witaj ponownie plytko EvB5.1"
            sockets.send(client, msg)

            new_msg = True
            full_msg = ""
