# rezvane


import tkinter as tk
from tkinter import messagebox


def birthday():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())

        if 1 <= month <= 12 and 1 <= day <= 31:
            if month < 10 or (month == 10 and day < 10):
                miladi_year = year + 621
            else:
                miladi_year = year + 622

            messagebox.showinfo("Result", f"Your Gregorian year: {miladi_year}")
        else:
            messagebox.showerror("Error", "Month or day is out of range!")
    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only!")


root = tk.Tk()
root.title("Birthday Converter")


lbl_year = tk.Label(root, text="Year (e.g. 1380):")
lbl_year.grid(row=0, column=0, padx=8, pady=5)
entry_year = tk.Entry(root, width=10)
entry_year.grid(row=0, column=1, padx=8, pady=5)


lbl_month = tk.Label(root, text="Month (1-12):")
lbl_month.grid(row=1, column=0, padx=8, pady=5)
entry_month = tk.Entry(root, width=10)
entry_month.grid(row=1, column=1, padx=8, pady=5)


lbl_day = tk.Label(root, text="Day (1-31):")
lbl_day.grid(row=2, column=0, padx=8, pady=5)
entry_day = tk.Entry(root, width=10)
entry_day.grid(row=2, column=1, padx=8, pady=5)


btn = tk.Button(root, text="Convert", command=birthday, width=15, bg="lightblue")
btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()