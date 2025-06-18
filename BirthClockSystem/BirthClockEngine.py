import datetime

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

        print("\n--- Your Lived Time ---")
        print(f"Years      : {years}")
        print(f"Days       : {days}\t Hours   : {hours}\t Minutes   : {minutes}\t Seconds   : {seconds}")
        print(f"\nTotal Time Since Birth: {age_diff}")
        print(f"Total Days Lived      : {age_diff.days}")
        print(f"Total Seconds Lived   : {total_seconds}")

    def days_until_next_birthday(self):
        today = self.now.date()
        current_year = today.year
        birth_month = self.birth_date.month
        birth_day = self.birth_date.day

        try:
            next_birthday = datetime.date(current_year, birth_month, birth_day)
        except ValueError:
            # Handle Feb 29 birthdays in non-leap years
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

        print(f"\n--- Time Left Until Your Next Birthday ({next_birthday}) ---")
        print(f"Approx. Months: {int(approx_months)}, Days: {int(remaining_days)} (Total: {days} days)")

    def time_until_specific_date(self, year, month, day):
        try:
            target_date = datetime.datetime(year, month, day)
        except ValueError:
            print("\nInvalid date entered.")
            return

        if target_date < self.now:
            print("\nThe specified date is in the past!")
            return

        diff = target_date - self.now
        days = diff.days
        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        seconds = diff.seconds % 60

        print(f"\n--- Time Until {target_date.date()} ---")
        print(f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")


# Start of program
print("=== AGE CALCULATOR ===")
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (MM): "))
birth_day = int(input("Enter your birth day (DD): "))

age = AgeCalculator(birth_year, birth_month, birth_day)

while True:
    print("\nChoose an option:")
    print("1. Show lived time")
    print("2. Days left to next birthday")
    print("3. Time left to a specific date")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        age.calculate_lived_time()
    elif choice == '2':
        age.days_until_next_birthday()
    elif choice == '3':
        year = int(input("Enter target year (YYYY): "))
        month = int(input("Enter target month (MM): "))
        day = int(input("Enter target day (DD): "))
        age.time_until_specific_date(year, month, day)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1-4.")
