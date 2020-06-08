import numpy as np
import os
import pyautogui
import subprocess


def com1():
    # skrypt tworzy plik i  zapisuje wartosc volume (42%)
    command = "amixer -D pulse sget Master | grep 'Left:' | awk -F'[][]' '{ print $2 > \"plik1\" }'"
    subprocess.call(command, shell=True)
    volDec = 0
    x = 0
    # przepisuje vartosc volume do pliku bez znaku %
    with open("plik1") as f:
        x = f.read()
    os.remove("plik1")
    with open("plik1", "w") as f:
        f.write((x[:-2]))
    # pobieram wartosc volume z pliku
    with open("plik1") as f:
        volDec = int(f.read())

    return "{}${}@".format(1, volDec)


def com2():
    cpu = subprocess.getoutput("""iostat | awk 'FNR==4{print $1}'""")
    temperature = subprocess.getoutput("""sensors | awk 'FNR==3{print $2}'""")[1:5]
    memory = subprocess.getoutput("""free | awk 'FNR==2{print $3/$2 * 100.0}'""")[:-2]

    while len(memory) < 5:
        memory += '0'
    return f"""2${cpu}${memory}${temperature}@"""


def com3():
    im = pyautogui.screenshot()
    averange_row = np.average(im, axis=0)  # srednia kolumn
    avr_col = np.average(averange_row, axis=0)
    avr_int = (int(avr_col[0]), int(avr_col[1]), int(avr_col[2]))
    return "{}${}${}${}@".format(3, hex(avr_int[0]).lstrip('0x'), hex(avr_int[1]).lstrip('0x'),
                                 hex(avr_int[2]).lstrip('0x'))


def com4(button_number):
    descriptions = ['włacza\nskrypt',
                    'wypisuje\npliki',
                    'wypi.wł.\nprocesy',
                    'włacza\nFirefox',
                    'włacza\nkalkul.',
                    'wł.odtw.\nmuzyki',
                    'włacza\nSapera',
                    'wyłącza\nsystem']

    return "{}${}@".format(4, descriptions[int(button_number)])


def com5(val):
    if len(val) == 1:
        volume = int(val[0])
        os.popen("amixer sset 'Master' " + str(volume) + "%")
    if len(val) == 2:
        volume = int(val[0]) * 10 + int(val[1])
        os.popen("amixer sset 'Master' " + str(volume) + "%")
    if len(val) == 3:
        volume = 100
        os.popen("amixer sset 'Master' " + str(volume) + "%")
    return "{}@".format(5)


def com6(button_number):
    print()
    print("Funkcja uzytkownika: ")
    actions = ["./actions/action0.sh", "ls -lr ~", "ps -aux",
               "firefox", "gnome-calculator", "rhythmbox-client", "gnome-mines", "halt"]
    subprocess.call([actions[int(button_number)]], shell=True)
    print()
    return "{}@".format(6)
