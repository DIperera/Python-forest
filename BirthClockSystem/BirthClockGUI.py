# Importing required modules
import datetime  # Built-in module for handling dates and times
import tkinter as tk  # Basic GUI module
from tkinter import messagebox  # For showing pop-up messages
from tkinter import ttk  # Themed widgets like buttons, labels, etc.
from ttkthemes import ThemedTk  # Allows the use of modern themes for the GUI

# ----------- Utility function to center windows -----------
def center_window(window, width=500, height=420):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.resizable(False, False)

# ----------- AgeCalculator Class Definition -----------
class AgeCalculator:
    def __init__(self, year, month, day):
        # Store the birth date
        self.birth_date = datetime.datetime(year, month, day)
        # Get the current date and time
        self.now = datetime.datetime.now()

    def calculate_lived_time(self):
        # Calculate the difference between current time and birth date
        age_diff = self.now - self.birth_date
        total_seconds = int(age_diff.total_seconds())

        # Extract years, days, hours, minutes, seconds
        years = age_diff.days // 365
        days = age_diff.days % 365
        hours = age_diff.seconds // 3600
        minutes = (age_diff.seconds % 3600) // 60
        seconds = age_diff.seconds % 60

        # Return a formatted string of the lived time
        return (
            f"--- Your Lived Time ---\n"
            f"Years: {years}\n"
            f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}\n"
            f"\nTotal Time Since Birth: {age_diff}\n"
            f"Total Days Lived: {age_diff.days}\n"
            f"Total Seconds Lived: {total_seconds}"
        )

    def days_until_next_birthday(self):
        # Calculate how many days until the next birthday
        today = self.now.date()
        current_year = today.year
        birth_month = self.birth_date.month
        birth_day = self.birth_date.day

        # Handle leap years (e.g., Feb 29)
        try:
            next_birthday = datetime.date(current_year, birth_month, birth_day)
        except ValueError:
            next_birthday = datetime.date(current_year, 3, 1)  # fallback to March 1

        # If birthday has passed this year, calculate for next year
        if next_birthday <= today:
            try:
                next_birthday = datetime.date(current_year + 1, birth_month, birth_day)
            except ValueError:
                next_birthday = datetime.date(current_year + 1, 3, 1)

        delta = next_birthday - today
        days = delta.days
        approx_months = days // 30.5
        remaining_days = days % 30.5

        # Return a formatted string
        return (
            f"--- Time Until Your Next Birthday ({next_birthday}) ---\n"
            f"Approx. Months: {int(approx_months)}, Days: {int(remaining_days)}\n"
            f"(Total: {days} days)"
        )

    def time_until_specific_date(self, year, month, day):
        # Calculate time left until a custom future date
        try:
            target_date = datetime.datetime(year, month, day)
        except ValueError:
            return "Invalid date entered."

        # If the date is in the past, show error
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

# ----------- GUI Functions -----------

def create_calculator():
    # Read birth date input and return an AgeCalculator instance
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        return AgeCalculator(year, month, day)
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid birth date!")
        return None

def open_lived_time():
    # Show window with time lived
    calc = create_calculator()
    if calc:
        win = tk.Toplevel(root)
        win.title("Lived Time")
        center_window(win) #call the center_window function
        ttk.Label(win, text=calc.calculate_lived_time(), justify="left", padding=10, wraplength=420).pack(fill="both", expand=True)
        ttk.Button(win, text="Back to Home", command=win.destroy).pack(pady=10)

def open_next_birthday():
    # Show window with days until next birthday
    calc = create_calculator()
    if calc:
        win = tk.Toplevel(root)
        win.title("Next Birthday")
        center_window(win) #call the center_window function
        ttk.Label(win, text=calc.days_until_next_birthday(), justify="left", padding=10, wraplength=420).pack(fill="both", expand=True)
        ttk.Button(win, text="Back to Home", command=win.destroy).pack(pady=10)

def open_specific_date():
    # Show input form and result for specific future date countdown
    calc = create_calculator()
    if calc:
        win = tk.Toplevel(root)
        win.title("Countdown to Specific Date")
        center_window(win) #call the center_window function
        ttk.Label(win, text="Enter target date below:").pack(pady=5)
        frm = ttk.Frame(win)
        frm.pack()

        # Input fields for year, month, day
        ttk.Label(frm, text="Year:").grid(row=0, column=0)
        year_entry = ttk.Entry(frm, width=5)
        year_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frm, text="Month:").grid(row=0, column=2)
        month_entry = ttk.Entry(frm, width=3)
        month_entry.grid(row=0, column=3, padx=5)

        ttk.Label(frm, text="Day:").grid(row=0, column=4)
        day_entry = ttk.Entry(frm, width=3)
        day_entry.grid(row=0, column=5, padx=5)

        # Area to show result
        result_text = tk.StringVar()
        ttk.Label(win, textvariable=result_text, wraplength=400, padding=10, justify="left").pack(pady=5, fill="both", expand=True)

        # Button to trigger calculation
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

# ----------- MAIN GUI SETUP -----------

# Create main window with theme
root = ThemedTk(theme="plastik")  # You can change to "arc", "breeze", etc.
root.title("Age Calculator - By Ishira Perera")
root.geometry("500x420")  # Window size
center_window(root) #call the center_window function

# Set default font and spacing
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TEntry", padding=5)

# Title label
ttk.Label(root, text="Enter Your Birth Date", font=("Segoe UI", 13, "bold")).pack(pady=10)

# Frame for date inputs
frame = ttk.Frame(root)
frame.pack()

# Year input
ttk.Label(frame, text="Year (YYYY):").grid(row=0, column=0, padx=5)
entry_year = ttk.Entry(frame, width=6)
entry_year.grid(row=0, column=1, padx=5)

# Month input
ttk.Label(frame, text="Month (MM):").grid(row=0, column=2, padx=5)
entry_month = ttk.Entry(frame, width=4)
entry_month.grid(row=0, column=3, padx=5)

# Day input
ttk.Label(frame, text="Day (DD):").grid(row=0, column=4, padx=5)
entry_day = ttk.Entry(frame, width=4)
entry_day.grid(row=0, column=5, padx=5)

# Buttons for actions
ttk.Label(root, text="Choose an option:", font=("Segoe UI", 12)).pack(pady=10)
ttk.Button(root, text="🧮 Show Lived Time", command=open_lived_time).pack(pady=5)
ttk.Button(root, text="🎉 Days Until Next Birthday", command=open_next_birthday).pack(pady=5)
ttk.Button(root, text="📅 Time Until Specific Date", command=open_specific_date).pack(pady=5)

# Start the GUI event loop
root.mainloop()
