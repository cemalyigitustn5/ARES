import tkinter as tk


def baslat():
    pencere = tk.Tk()

    pencere.title("ARES")
    pencere.geometry("700x450")
    pencere.resizable(False, False)

    baslik = tk.Label(
        pencere,
        text="A R E S",
        font=("Arial", 22, "bold")
    )
    baslik.pack(pady=20)

    mesaj = tk.Label(
        pencere,
        text="Merhaba Cemal.\nBen ARES.",
        font=("Arial", 13)
    )
    mesaj.pack()

    pencere.mainloop()