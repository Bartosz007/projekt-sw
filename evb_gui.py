import tkinter as tk
import time
import functions.client_functions as cf

time_on_press = 0
hold_time = 1


def on_press(i):
    global time_on_press
    time_on_press = time.time()


def on_release(server_connection, lcd_label, i):
    global time_on_press
    if time.time() - time_on_press > hold_time:
        # print("button {} was held more than 5 seconds and needs description of function".format(i))
        cf.com4(server_connection, lcd_label, i)
    else:
        cf.com6(server_connection, i)
       # print("button {} was released and needs function".format(i))


def load_gui(server_connection):
    window = tk.Tk()
    window.title("EvB5.1")
    width, heigh = 800, 800
    window.geometry("{}x{}+{}+{}".format(width, heigh, 100, 100))

    # główne okno GUI
    main_frame = tk.Frame(window, width=width, heigh=heigh)
    main_frame.pack_propagate(0)
    main_frame.pack()

    # panel LCD
    lcd_frame = tk.Frame(main_frame, width=width, heigh=heigh / 6)
    lcd_frame.pack_propagate(0)
    lcd_frame.pack()

    lcd_opis_label = tk.Label(lcd_frame, text="wyświetlacz LCD", font=("Courier", 10))
    lcd_opis_label.pack()
    lcd_label = tk.Label(lcd_frame, text="8888888888888888\n8888888888888888", font=("Courier", 20), bg="RED")
    lcd_label.pack()

    # ADC
    adc_frame = tk.Frame(main_frame, width=width, heigh=heigh / 6)
    adc_frame.pack_propagate(0)
    adc_frame.pack()

    adc_opis_label = tk.Label(adc_frame, text="kontrolka stanu adc", font=("Courier", 10))
    adc_opis_label.pack()

    adc_scale = tk.Scale(adc_frame, from_=0, to=100, orient=tk.HORIZONTAL)
    adc_scale.pack()

    # dioda RGB
    rgb_frame = tk.Frame(main_frame, width=width, heigh=heigh / 6)
    rgb_frame.pack_propagate(0)
    rgb_frame.pack()

    rgb_opis_label = tk.Label(rgb_frame, text="wyswietlanie diody RGB", font=("Courier", 10))
    rgb_opis_label.pack()

    rgb_label = tk.Label(rgb_frame, text="   ", font=("Courier", 40), bg="BLACK")
    rgb_label.pack()

    # przyciski S0-S7
    buttons_frame = tk.Frame(main_frame, width=width, heigh=heigh / 6)
    buttons_frame.pack_propagate(0)
    buttons_frame.pack()

    buttons_opis_label = tk.Label(buttons_frame, text="przyciski(8x)", font=("Courier", 10))
    buttons_opis_label.pack()

    for i in range(8):
        fr = tk.Frame(buttons_frame, width=int(800 / 8), heigh="50")
        fr.pack_propagate(0)
        fr.pack(side=tk.LEFT)

        bt = tk.Button(fr, text="Button" + str(i), width=10, heigh=10)
        bt.bind("<ButtonPress>", lambda event, i=i: on_press(i))
        bt.bind("<ButtonRelease>", lambda event, i=i: on_release(server_connection, lcd_label, i))
        bt.pack()

    # diody L0-L7
    diods_frame = tk.Frame(main_frame, width=width, heigh=heigh / 6)
    diods_frame.pack_propagate(0)
    diods_frame.pack()

    diods_opis_label = tk.Label(diods_frame, text="diody led(8x)", font=("Courier", 10))
    diods_opis_label.pack()

    for i in range(8):
        fr = tk.Frame(diods_frame, width=int(800 / 8), heigh="50")
        fr.pack_propagate(0)
        fr.pack(side=tk.LEFT)
        lb = tk.Label(fr, text=" LED{} ".format(i), bg="#800E3B", padx=5, pady=10, font=("Courier", 10))
        lb.pack()

    #  przycisk do testowania połączenia
    test_frame = tk.Frame(main_frame, width=width, heigh=heigh / 6)
    test_frame.pack_propagate(0)
    test_frame.pack()

    test_button = tk.Button(test_frame, text="SOCKET TEST", width=10, heigh=10)
    test_button.pack(side=tk.LEFT)

    test_label = tk.Label(test_frame, text="Test label", bg="#ff0000")
    test_label.pack(side=tk.LEFT)

    # aby nie było problemów z widzialnością zmiennych przez program,
    # dodawjacie obsługę przycisków/ suwaków poniżej( ale przed window.mainloop())
    # najlepiej też przesłać przez parametr elementy GUI na których potem będzie się operować
    # poniżej jest przykładowe połączenie klient->serwer->klient

    test_button.config(command=lambda: cf.test_connection(server_connection, test_label))

    window.mainloop()
