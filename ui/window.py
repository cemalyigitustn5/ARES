from ui.theme import *
import tkinter as tk
from core.brain import cevap_ver


def mesaj_ekle(kisi, mesaj):
    sohbet.config(state="normal")
    sohbet.insert(tk.END, f"{kisi}: {mesaj}\n\n")
    sohbet.config(state="disabled")
    sohbet.see(tk.END)


def gonder():
    komut = giris.get().strip()

    if not komut:
        return

    mesaj_ekle("Sen", komut)

    cevap = cevap_ver(komut)

    mesaj_ekle("ARES", cevap)

    giris.delete(0, tk.END)


def baslat():
    global sohbet
    global giris

    pencere = tk.Tk()
    pencere.title("ARES")
    pencere.geometry("750x550")
    pencere.configure(bg=BG_COLOR)
    pencere.resizable(False, False)

    baslik = tk.Label(
        pencere,
        text="A R E S",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 22, "bold")
    )
    baslik.pack(pady=10)

    sohbet = tk.Text(
        pencere,
        width=80,
        height=22,
        bg=CHAT_BG,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        font=("Consolas", 11),
        relief="flat",
        bd=10
    )
    sohbet.pack(padx=10)

    sohbet.insert(tk.END, "ARES: Merhaba Cemal.\n")
    sohbet.insert(tk.END, "ARES: Ben göreve hazırım.\n\n")
    sohbet.config(state="disabled")

    alt_cerceve = tk.Frame(
        pencere,
        bg=BG_COLOR
    )
    alt_cerceve.pack(pady=10)

    giris = tk.Entry(
        alt_cerceve,
        width=55,
        bg=ENTRY_BG,
        fg=ENTRY_FG,
        insertbackground="white",
        font=("Arial", 11)
    )
    giris.pack(side=tk.LEFT, padx=5)

    giris.bind("<Return>", lambda event: gonder())

    buton = tk.Button(
        alt_cerceve,
        text="Gönder",
        command=gonder,
        bg=BUTTON_BG,
        fg=BUTTON_FG,
        width=12,
        font=("Arial", 10, "bold")
    )
    buton.pack(side=tk.LEFT)

    giris.focus()

    pencere.mainloop()