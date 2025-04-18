import tkinter as tk
from tkinter import IntVar
from constants import Answer
from seco_form import fill_form_from_inputs

def get_values():
    number = number_entry.get()
    answered = radio1_var.get()
    healthcare = radio2_var.get()
    print(f"Text: {number}, Yes/No: {answered}, Yes/No/Don't Know: {healthcare}")

def send_to_SECO():
    number = sanitize_phone_number(number_entry.get())
    answered = Answer(radio1_var.get())
    healthcare = Answer(radio2_var.get())
    print(number, Answer(answered), Answer(healthcare))
    fill_form_from_inputs(number, answered, healthcare)

def sanitize_phone_number(n):
    no_space = "".join(n.split())
    assert len(no_space) == 10
    n = no_space[0:3] + " " + no_space[3:6] + " " + no_space[6:8] + " " + no_space[8:10]
    return n

root = tk.Tk()
root.title("SECO spam reporting")

# Text Entry
text_label = tk.Label(root, text="Numéro spam: (012 345 67 89)")
text_label.pack()
number_entry = tk.Entry(root)
number_entry.pack(pady=5)

# Separator
tk.Frame(root, height=2, width=200, bg="black").pack(pady=5)

# Yes/No Radio Buttons
radio1_label = tk.Label(root, text="Répondu à l'appel?")
radio1_label.pack()
radio1_var = IntVar(value=Answer.NO.value)
tk.Radiobutton(root, text="Oui", variable=radio1_var, value=Answer.YES.value).pack()
tk.Radiobutton(root, text="Non", variable=radio1_var, value=Answer.NO.value).pack()

# Separator
tk.Frame(root, height=2, width=200, bg="black").pack(pady=5)

# Yes/No/Do Not Know Radio Buttons
radio2_label = tk.Label(root, text="Assurance maladie?")
radio2_label.pack()
radio2_var = IntVar(value=Answer.DNK.value)
tk.Radiobutton(root, text="Oui", variable=radio2_var, value=Answer.YES.value).pack()
tk.Radiobutton(root, text="Non", variable=radio2_var, value=Answer.NO.value).pack()
tk.Radiobutton(root, text="Ne sais pas", variable=radio2_var, value=Answer.DNK.value).pack()

# Separator
tk.Frame(root, height=2, width=200, bg="black").pack(pady=5)

# Button
# tk.Button(root, text="Envoyer", command=get_values).pack(pady=10)
tk.Button(root, text="Envoyer", command=send_to_SECO).pack(pady=10)

root.mainloop()