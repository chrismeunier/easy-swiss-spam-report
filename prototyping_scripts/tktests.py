import tkinter as tk
from tkinter import IntVar

def get_values():
    spam_number = spam_entry.get()
    call_answered = call_answered_var.get()
    health_insurance = health_insurance_var.get()
    anti_spam_filter = anti_spam_filter_var.get()
    frc_member = frc_member_var.get()
    customer = customer_var.get()
    phone_book = phone_book_var.get()
    poll_participation = poll_participation_var.get()
    money_loss = money_loss_var.get()
    anti_spam_knowledge = anti_spam_knowledge_var.get()
    anti_spam_usage = anti_spam_usage_var.get()
    status_label.config(text="Processing...")  # Update status label
    print(f"Spam Number: {spam_number}, Call Answered: {call_answered}, Health Insurance: {health_insurance}, "
          f"Anti-Spam Filter: {anti_spam_filter}, FRC Member: {frc_member}, Customer: {customer}, "
          f"Phone Book Entry: {phone_book}, Poll Participation: {poll_participation}, Money Loss: {money_loss}, "
          f"Anti-Spam Knowledge: {anti_spam_knowledge}, Anti-Spam Usage: {anti_spam_usage}")
    status_label.config(text="Complaints sent!")  # Final update
def toggle_optional():
    if optional_frame.winfo_ismapped():
        optional_frame.pack_forget()
    else:
        optional_frame.pack(fill="x", padx=5, pady=5)

root = tk.Tk()
root.title("Spam Complaint Form")

# Spam Number Entry Frame
spam_frame = tk.Frame(root)
spam_frame.pack(pady=5)
spam_label = tk.Label(spam_frame, text="Spam number: (012 345 67 89)")#, font=("Arial", 12, "bold"))
spam_label.pack(side=tk.LEFT)
spam_entry = tk.Entry(spam_frame)
spam_entry.pack(side=tk.LEFT, padx=5)

# Main Frame
main_frame = tk.Frame(root)
main_frame.pack()

# SECO Report
seco_frame = tk.LabelFrame(main_frame, text="SECO Report")
seco_frame.pack(side=tk.LEFT, padx=10, pady=5, fill="both", expand=True)

call_answered_var = IntVar(value=0)
tk.Label(seco_frame, text="Call answered?").pack(anchor="w")
tk.Radiobutton(seco_frame, text="Yes", variable=call_answered_var, value=1).pack(anchor="w")
tk.Radiobutton(seco_frame, text="No", variable=call_answered_var, value=0).pack(anchor="w")

health_insurance_var = IntVar(value=2)
tk.Label(seco_frame, text="Health insurance?").pack(anchor="w")
tk.Radiobutton(seco_frame, text="Yes", variable=health_insurance_var, value=1).pack(anchor="w")
tk.Radiobutton(seco_frame, text="No", variable=health_insurance_var, value=0).pack(anchor="w")
tk.Radiobutton(seco_frame, text="Does not know", variable=health_insurance_var, value=2).pack(anchor="w")

# FRC Report
frc_frame = tk.LabelFrame(main_frame, text="FRC Report")
frc_frame.pack(side=tk.LEFT, padx=10, pady=5, fill="both", expand=True)

anti_spam_filter_var = IntVar(value=0)
tk.Label(frc_frame, text="Do you have an active anti-spam filter?").pack(anchor="w")
tk.Radiobutton(frc_frame, text="Yes", variable=anti_spam_filter_var, value=1).pack(anchor="w")
tk.Radiobutton(frc_frame, text="No", variable=anti_spam_filter_var, value=0).pack(anchor="w")

frc_member_var = IntVar(value=0)
tk.Label(frc_frame, text="Are you a member of the FRC?").pack(anchor="w")
tk.Radiobutton(frc_frame, text="Yes", variable=frc_member_var, value=1).pack(anchor="w")
tk.Radiobutton(frc_frame, text="No", variable=frc_member_var, value=0).pack(anchor="w")

# Optional Questions
optional_frame = tk.LabelFrame(frc_frame, text="Optional Questions")

customer_var = IntVar(value=0)
tk.Label(optional_frame, text="Are/were you a customer?").pack(anchor="w")
tk.Radiobutton(optional_frame, text="Yes", variable=customer_var, value=1).pack(anchor="w")
tk.Radiobutton(optional_frame, text="No", variable=customer_var, value=0).pack(anchor="w")

phone_book_var = IntVar(value=0)
tk.Label(optional_frame, text="Do you have the * in the phone book?").pack(anchor="w")
tk.Radiobutton(optional_frame, text="Yes", variable=phone_book_var, value=1).pack(anchor="w")
tk.Radiobutton(optional_frame, text="No", variable=phone_book_var, value=0).pack(anchor="w")

poll_participation_var = IntVar(value=0)
tk.Label(optional_frame, text="Participated in a poll/survey/contest linked to the company?").pack(anchor="w")
tk.Radiobutton(optional_frame, text="Yes", variable=poll_participation_var, value=1).pack(anchor="w")
tk.Radiobutton(optional_frame, text="No", variable=poll_participation_var, value=0).pack(anchor="w")

money_loss_var = IntVar(value=0)
tk.Label(optional_frame, text="Did you lose money?").pack(anchor="w")
tk.Radiobutton(optional_frame, text="Yes", variable=money_loss_var, value=1).pack(anchor="w")
tk.Radiobutton(optional_frame, text="No", variable=money_loss_var, value=0).pack(anchor="w")

anti_spam_knowledge_var = IntVar(value=0)
tk.Label(optional_frame, text="Do you know about anti-spam filters?").pack(anchor="w")
tk.Radiobutton(optional_frame, text="Yes", variable=anti_spam_knowledge_var, value=1).pack(anchor="w")
tk.Radiobutton(optional_frame, text="No", variable=anti_spam_knowledge_var, value=0).pack(anchor="w")

anti_spam_usage_var = IntVar(value=0)
tk.Label(optional_frame, text="If yes, were you using it?").pack(anchor="w")
tk.Radiobutton(optional_frame, text="Yes", variable=anti_spam_usage_var, value=1).pack(anchor="w")
tk.Radiobutton(optional_frame, text="No", variable=anti_spam_usage_var, value=0).pack(anchor="w")

# Hide optional questions initially
optional_frame.pack_forget()

# Toggle Optional Questions Button
tk.Button(frc_frame, text="Show/Hide Optional Questions", command=toggle_optional).pack(pady=5)

# Send Complaints Button and Status Label
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Send Complaints", command=get_values).pack(side=tk.LEFT, padx=5)
status_label = tk.Label(button_frame, text="", fg="green")
status_label.pack(side=tk.LEFT)

root.mainloop()
