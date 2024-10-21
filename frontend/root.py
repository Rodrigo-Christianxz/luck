# root.py

import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x300")
root.title("Luck - Assistente Pessoal")

label = ctk.CTkLabel(root, text="Bem-vindo ao Luck!")
label.pack()

root.mainloop()
