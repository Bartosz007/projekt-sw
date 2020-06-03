from random import randint
import subprocess

def com0():
    col = ['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']

    # w waszym interesie jest zadbać o poprawny format komunikatu
    return "{}${}@".format(0, col[randint(0, 7)])


def com4(button_number):
    descriptions = ['opis przycisk zerowy', 'opis przycisk pierwszy', 'opis przycisk drugi', 'opis przycisk trzeci',
                    'opis przycisk czwarty', 'opis przycisk piąty', 'opis przycisk szósty', 'opis przycisk siódmy',
                    'opis przycisk ósmy']
    return "{}${}@".format(4, descriptions[int(button_number)])


def com6(button_number):
    print()
    print("Funkcja uzytkownika: ")
    actions = ["./actions/action0.sh","ls -lr ~","ps -aux",
	      "firefox","gnome-calculator","rhythmbox-client","gnome-mines","halt"]
    #subprocess.call([actions[int(button_number)]],shell=True)
    print()
    return "{}@".format(6)
