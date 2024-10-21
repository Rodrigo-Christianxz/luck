import customtkinter as ctk

root = ctk.CTk()
root.title("Luck - Versão 0.1")
ctk.set_appearance_mode("system")
root.geometry("900x500")

label = ctk.CTkLabel(master=root, text="Bem-vindo ao Luck!")
label.pack(pady=20)

img =ctk.CTkImage(light_image=("logo.svg"))


entry = ctk.CTkEntry(master=root, placeholder_text="Pergunte ao Luck!")
entry.pack(pady=10)

button = ctk.CTkButton(master=root, text="Enviar", command=lambda: print(entry.get()))
button.pack(pady=10)


root.mainloop()