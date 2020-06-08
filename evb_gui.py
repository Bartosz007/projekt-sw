import asyncio
import nest_asyncio
import threading
import tkinter as tk
import time
import functions.client_functions as cf


root = tk.Tk()
nest_asyncio.apply()
lcd_text = tk.StringVar(value="88888888\n88888888")


time_on_press = 0
hold_time = 0.5
active_sys = True

connection = None
connection2 = None
test_label = None
lcd_label = None
adc_scale = None
rgb_label = None
buttons = None
leds = None


def on_press(i):
    global time_on_press
    time_on_press = time.time()


def on_release(i):
    global time_on_press
    global active_sys

    if time.time() - time_on_press > hold_time:
        active_sys = False

        try:
            description = cf.com4(connection, i)
            lcd_text.set(description)
            active_sys = True
        except Exception:
            pass

    else:
        try:
            cf.com4(connection, i)
            cf.com6(connection, i)
        except Exception:
            pass


def suwak_val(val):  # otrzymuje wartosc z potencjonometru

    try:
        cf.com5(connection, val)
        cf.com1(connection, leds)
    except Exception:
        pass


async def loop():
    while True:
        try:
            cpu, memory, temperature = cf.com2(connection)

            lcd_text.set(f"procesor:\n{cpu}%")
            await asyncio.sleep(2)
            lcd_text.set(f"pamiec:\n{memory}%")
            await asyncio.sleep(2)
            lcd_text.set(f"temp:\n{temperature}°C")
            await asyncio.sleep(3)
        except Exception:
            pass


async def loop2():
    global LOCK
    while True:
        try:
            cf.com3(connection, rgb_label)
            await asyncio.sleep(0.1)
        except Exception:
            pass


def thread(async_loop):
    async_loop.run_until_complete(loop())


def thread2(async_loop):
    async_loop.run_until_complete(loop2())


def start_loop(async_loop):
    threading.Thread(target=thread, args=(async_loop,)).start()


def start_loop2(async_loop):
    threading.Thread(target=thread2, args=(async_loop,)).start()


def load_gui(server_connection, window):
    global connection
    global connection2
    global test_label
    global lcd_label
    global adc_scale
    global rgb_label
    global buttons
    global leds
    global lcd_text

    connection = server_connection

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

    lcd_text = tk.StringVar(value="8888888888888888\n8888888888888888")
    lcd_opis_label = tk.Label(lcd_frame, textvar="wyświetlacz LCD", font=("Courier", 10))
    lcd_opis_label.pack()
    lcd_label = tk.Label(lcd_frame, textvar=lcd_text, font=("Courier", 20), bg="RED")
    lcd_label.pack()

    # ADC
    adc_frame = tk.Frame(main_frame, width=width, heigh=heigh / 6)
    adc_frame.pack_propagate(0)
    adc_frame.pack()

    adc_opis_label = tk.Label(adc_frame, text="kontrolka stanu adc", font=("Courier", 10))
    adc_opis_label.pack()

    adc_scale = tk.Scale(adc_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=suwak_val)
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

    buttons = []
    for i in range(8):
        fr = tk.Frame(buttons_frame, width=int(800 / 8), heigh="50")
        fr.pack_propagate(0)
        fr.pack(side=tk.LEFT)

        bt = tk.Button(fr, text="Button" + str(i), width=10, heigh=10)
        bt.bind("<ButtonPress>", lambda event, i=i: on_press(i))
        bt.bind("<ButtonRelease>", lambda event, i=i: on_release(i))
        bt.pack()

        buttons.append(bt)

    # diody L0-L7
    diods_frame = tk.Frame(main_frame, width=width, heigh=heigh / 6)
    diods_frame.pack_propagate(0)
    diods_frame.pack()

    diods_opis_label = tk.Label(diods_frame, text="diody led(8x)", font=("Courier", 10))
    diods_opis_label.pack()

    leds = []
    for i in range(8):
        fr = tk.Frame(diods_frame, width=int(800 / 8), heigh="50")
        fr.pack_propagate(0)
        fr.pack(side=tk.LEFT)
        lb = tk.Label(fr, text=" LED{} ".format(i), bg="#800E3B", padx=5, pady=10, font=("Courier", 10))
        lb.pack()

        leds.append(lb)

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

    async_loop = asyncio.get_event_loop()
    async_loop2 = asyncio.get_event_loop()
    start_loop(async_loop)
    start_loop2(async_loop2)

    test_button.config(command=lambda: cf.test_connection(server_connection, test_label))

    window.mainloop()
