from libs.socket_io import *


def com1(connection, led_list):
    send(connection, "{}@".format(1))
    rec = receive(connection)
    volDec = rec[2:len(rec) - 1]  # decimal volume
    leds = round(8 * int(volDec) / 100)
    for i in range(leds):
        led_list[i].configure(background="#ff0000")
    for i in range(leds, 8):
        led_list[i].configure(background="#800E3B")


def com2(connection):
    send(connection, "{}@".format(2))
    rec = receive(connection)
    rec = rec[2:len(rec) - 1]
    rec = rec.split("$")
    return rec


def com3(connection, rgb_label):
    send(connection, "{}@".format(3))
    rec = receive(connection)
    hexrgb = rec[2:len(rec) - 1].split('$')  # rozszyfrowanie RGB
    color = "#{}{}{}".format(hexrgb[0], hexrgb[1],
                             hexrgb[2])  # zamaiana formatu na string aby mozna było dowolnie manipulowac w tkinkerze
    rgb_label.config(bg=color)


def com4(connection, button):
    send(connection, "{}${}@".format(4, button))
    rec = receive(connection)
    return rec[2:len(rec) - 1]


def com5(connection, val):
    send(connection, "{}${}@".format(5, val))
    rec = receive(connection)
    return rec


def com6(connection, button):
    send(connection, "{}${}@".format(6, button))
    rec = receive(connection)
    return rec
