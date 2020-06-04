import evb_gui as gui

from libs import socket_io as sockets


def main():
    server_connection = sockets.open_connection()
    gui.load_gui(server_connection)


if __name__ == "__main__":

    main()
