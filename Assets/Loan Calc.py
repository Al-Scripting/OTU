import tkinter as tk

def calculate_payment():
    # Get user input
    interest_rate = float(interest_rate_entry.get())
    years = int(years_entry.get())
    loan_amount = float(loan_amount_entry.get())

    # Calculate monthly and total payments
    months = years * 12
    monthly_rate = interest_rate / 1200
    monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    total_payment = monthly_payment * months

    # Update labels with calculated values
    monthly_payment_label.config(text=f"\tMonthly Payment:\t${monthly_payment:.2f}")
    total_payment_label.config(text=f"\tTotal Payment:\t${total_payment:.2f}")


# Create main window
window = tk.Tk()
window.title("Loan Payment Calculator")

# Create labels and text entry boxes
interest_rate_label = tk.Label(window, text="Annual Interest Rate:")
interest_rate_label.grid(row=0, column=0)
interest_rate_entry = tk.Entry(window)
interest_rate_entry.grid(row=0, column=1)

years_label = tk.Label(window, text="Number of Years:")
years_label.grid(row=1, column=0)
years_entry = tk.Entry(window)
years_entry.grid(row=1, column=1)

loan_amount_label = tk.Label(window, text="Loan Amount:")
loan_amount_label.grid(row=2, column=0)
loan_amount_entry = tk.Entry(window)
loan_amount_entry.grid(row=2, column=1)

monthly_payment_label = tk.Label(window, text="Monthly Payment:")
monthly_payment_label.grid(row=3, column=0)
total_payment_label = tk.Label(window, text="Total Payment:")
total_payment_label.grid(row=4, column=0)

# Create button to calculate payments
calculate_button = tk.Button(window, text="Calculate", command=calculate_payment)
calculate_button.grid(row=5, column=1)

# Start main loop
window.mainloop()
