from random import randint


def com0():
    col = ['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']

    # w waszym interesie jest zadbać o poprawny format komunikatu
    return "{}${}@".format(0, col[randint(0, 7)])


