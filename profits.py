import tkinter as tk

root = tk.Tk()
root.title("Sales Application")
root.geometry("500x400")
root.configure(bg="lightblue")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (2000, 4500, 3000, 5000, 7000, 6000, 8000, 7500, 6500, 9000, 8500, 9500)

months_label = tk.Label(root, text=f"Months: {months}", bg="lightblue", font=("Helvetica", 10), wraplength=480)
profits_label = tk.Label(root, text=f"Profits: {profits}", bg="lightblue", font=("Helvetica", 10), wraplength=480)
max_profit_label = tk.Label(root, text="Max Profit: ", bg="lightblue", font=("Helvetica", 12))
min_profit_label = tk.Label(root, text="Min Profit: ", bg="lightblue", font=("Helvetica", 12))

def show_max_profit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = months[max_profit_index]
    max_profit_label.config(text=f"Max Profit: {max_profit} in {max_profit_month}")

def show_min_profit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month = months[min_profit_index]
    min_profit_label.config(text=f"Min Profit: {min_profit} in {min_profit_month}")

max_profit_button = tk.Button(root, text="Show Max Profit", command=show_max_profit, fg="white", bg="green")
min_profit_button = tk.Button(root, text="Show Min Profit", command=show_min_profit, fg="white", bg="red")

months_label.pack(pady=(20, 10))
profits_label.pack(pady=10)
max_profit_button.pack(pady=10)
max_profit_label.pack(pady=10)
min_profit_button.pack(pady=10)
min_profit_label.pack(pady=10)

root.mainloop()
