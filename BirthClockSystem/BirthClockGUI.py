import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk


class AgeCalculator:
    def __init__(self, year, month, day):
        self.birth_date = datetime.datetime(year, month, day)
        self.now = datetime.datetime.now()

    def calculate_lived_time(self):
        age_diff = self.now - self.birth_date
        total_seconds = int(age_diff.total_seconds())
        years = age_diff.days // 365
        days = age_diff.days % 365
        hours = age_diff.seconds // 3600
        minutes = (age_diff.seconds % 3600) // 60
        seconds = age_diff.seconds % 60

        return (
            f"--- Your Lived Time ---\n"
            f"Years: {years}\n"
            f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}\n"
            f"\nTotal Time Since Birth: {age_diff}\n"
            f"Total Days Lived: {age_diff.days}\n"
            f"Total Seconds Lived: {total_seconds}"
        )

    def days_until_next_birthday(self):
        today = self.now.date()
        current_year = today.year
        birth_month = self.birth_date.month
        birth_day = self.birth_date.day

        try:
            next_birthday = datetime.date(current_year, birth_month, birth_day)
        except ValueError:
            next_birthday = datetime.date(current_year, 3, 1)

        if next_birthday <= today:
            try:
                next_birthday = datetime.date(current_year + 1, birth_month, birth_day)
            except ValueError:
                next_birthday = datetime.date(current_year + 1, 3, 1)

        delta = next_birthday - today
        days = delta.days
        approx_months = days // 30.5
        remaining_days = days % 30.5

        return (
            f"--- Time Until Your Next Birthday ({next_birthday}) ---\n"
            f"Approx. Months: {int(approx_months)}, Days: {int(remaining_days)}\n"
            f"(Total: {days} days)"
        )

    def time_until_specific_date(self, year, month, day):
        try:
            target_date = datetime.datetime(year, month, day)
        except ValueError:
            return "Invalid date entered."

        if target_date < self.now:
            return "The specified date is in the past!"

        diff = target_date - self.now
        days = diff.days
        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        seconds = diff.seconds % 60

        return (
            f"--- Time Until {target_date.date()} ---\n"
            f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}"
        )


# ---------- GUI Functions ----------

def create_calculator():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        return AgeCalculator(year, month, day)
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid birth date!")
        return None


def open_lived_time():
    calc = create_calculator()
    if calc:
        win = tk.Toplevel(root)
        win.title("Lived Time")
        ttk.Label(win, text=calc.calculate_lived_time(), justify="left", padding=10, wraplength=420).pack(fill="both", expand=True)
        ttk.Button(win, text="Back to Home", command=win.destroy).pack(pady=10)


def open_next_birthday():
    calc = create_calculator()
    if calc:
        win = tk.Toplevel(root)
        win.title("Next Birthday")
        ttk.Label(win, text=calc.days_until_next_birthday(), justify="left", padding=10, wraplength=420).pack(fill="both", expand=True)
        ttk.Button(win, text="Back to Home", command=win.destroy).pack(pady=10)


def open_specific_date():
    calc = create_calculator()
    if calc:
        win = tk.Toplevel(root)
        win.title("Countdown to Specific Date")

        ttk.Label(win, text="Enter target date below:").pack(pady=5)
        frm = ttk.Frame(win)
        frm.pack()

        ttk.Label(frm, text="Year:").grid(row=0, column=0)
        year_entry = ttk.Entry(frm, width=5)
        year_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frm, text="Month:").grid(row=0, column=2)
        month_entry = ttk.Entry(frm, width=3)
        month_entry.grid(row=0, column=3, padx=5)

        ttk.Label(frm, text="Day:").grid(row=0, column=4)
        day_entry = ttk.Entry(frm, width=3)
        day_entry.grid(row=0, column=5, padx=5)

        result_text = tk.StringVar()
        ttk.Label(win, textvariable=result_text, wraplength=400, padding=10, justify="left").pack(pady=5, fill="both", expand=True)

        def calculate_specific():
            try:
                y = int(year_entry.get())
                m = int(month_entry.get())
                d = int(day_entry.get())
                result_text.set(calc.time_until_specific_date(y, m, d))
            except ValueError:
                messagebox.showerror("Input Error", "Enter valid numeric date!")

        ttk.Button(win, text="Calculate", command=calculate_specific).pack(pady=5)
        ttk.Button(win, text="Back to Home", command=win.destroy).pack(pady=5)


# ---------- MAIN GUI ----------

root = ThemedTk(theme="arc")  # Try "equilux", "plastik", "breeze", etc.
root.title("Age Calculator - Home")
root.geometry("500x420")

# Global font and style
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TEntry", padding=5)

ttk.Label(root, text="Enter Your Birth Date", font=("Segoe UI", 13, "bold")).pack(pady=10)
frame = ttk.Frame(root)
frame.pack()

ttk.Label(frame, text="Year (YYYY):").grid(row=0, column=0, padx=5)
entry_year = ttk.Entry(frame, width=6)
entry_year.grid(row=0, column=1, padx=5)

ttk.Label(frame, text="Month (MM):").grid(row=0, column=2, padx=5)
entry_month = ttk.Entry(frame, width=4)
entry_month.grid(row=0, column=3, padx=5)

ttk.Label(frame, text="Day (DD):").grid(row=0, column=4, padx=5)
entry_day = ttk.Entry(frame, width=4)
entry_day.grid(row=0, column=5, padx=5)

ttk.Label(root, text="Choose an option:", font=("Segoe UI", 12)).pack(pady=10)
ttk.Button(root, text="🧮 Show Lived Time", command=open_lived_time).pack(pady=5)
ttk.Button(root, text="🎉 Days Until Next Birthday", command=open_next_birthday).pack(pady=5)
ttk.Button(root, text="📅 Time Until Specific Date", command=open_specific_date).pack(pady=5)

root.mainloop()
