import tkinter as tk
from time import strftime

def time():
    string_time = strftime('%H:%M:%S %p')
    label_time.config(text=string_time)
    string_date = strftime('%A, %d %B %Y')
    label_date.config(text=string_date)
    label_time.after(1000, time)

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black")

frame = tk.Frame(root, bg="black", highlightbackground="#00FF99", highlightthickness=4, bd=20)
frame.pack(padx=40, pady=40)

label_time = tk.Label(frame, font=('Helvetica', 60, 'bold'), bg='black', fg='#00FF99')
label_time.pack(anchor='center', pady=20)

label_date = tk.Label(frame, font=('Helvetica', 24, 'bold'), bg='black', fg='cyan')
label_date.pack(anchor='center')

time()
root.mainloop()
