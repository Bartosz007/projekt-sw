import socket
from libs import socket_io as sockets
import functions.server_funcions as sf

HEADER_LENGTH = 10
IP = "127.0.0.1"  # pętla zwrotna (wskazuje na samego siebie)
PORT = 7070


def communicates(comm):  # funkcja obsługująca treści komunikatów
    # print("Otrzymano komunikat o treści: ")
    # print(comm)

    if comm[len(comm) - 1] != '@':  # prosty parser wiadomości
        print("ERROR CONNECTION!")
        return -1

    numer = int(comm[0])


    if numer == 1:
        return sf.com1()
    elif numer == 2:
        return sf.com2()
    elif numer == 3:
        return sf.com3()
    elif numer == 4:
        return sf.com4(comm[2])
    elif numer == 5:
        return sf.com5(comm[2:len(comm) - 1])
    elif numer == 6:
        return sf.com6(comm[2])


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)

    print("Serwer rozpoczął nasłuchiwanie...")

    client, address = server.accept()  # łączenie z klientem

    print(f"Połączono z: {address}!")

    msg = "Witaj plytko EvB5.1"
    sockets.send(client, msg)
    sockets.release_lock()

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
                sockets.release_lock()
                full_msg = ""
                new_msg = True

        except ValueError:
            print(f"Rozłączono: {address}!")
            client, address = server.accept()  # łączenie z klientem

            print(f"Ponownie połączono z: {address}!")

            msg = "Witaj ponownie plytko EvB5.1"
            sockets.send(client, msg)
            sockets.release_lock()

            new_msg = True
            full_msg = ""
