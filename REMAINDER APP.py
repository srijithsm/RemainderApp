import tkinter as tk
from tkinter import messagebox
import time
import threading

def show_message_box():
    messagebox.showinfo("Reminder", "Time's up!")

def set_reminder():
    try:
        time_value = float(entry_time.get())
        unit = unit_var.get()
        if unit == "Seconds":
            time_value *= 1
        elif unit == "Minutes":
            time_value *= 60
        elif unit == "Hours":
            time_value *= 3600
        
        # Start a new thread to wait and show reminder
        threading.Thread(target=lambda: time.sleep(time_value) or show_message_box()).start()
    except ValueError:
        messagebox.showerror("Error", "Invalid time value")

# Create main window
root = tk.Tk()
root.title("Reminder App")

# Create and place widgets
label_time = tk.Label(root, text="Time:")
label_time.grid(row=0, column=0, padx=5, pady=5)

entry_time = tk.Entry(root)
entry_time.grid(row=0, column=1, padx=5, pady=5)

unit_var = tk.StringVar()
unit_var.set("Seconds")

unit_menu = tk.OptionMenu(root, unit_var, "Seconds", "Minutes", "Hours")
unit_menu.grid(row=0, column=2, padx=5, pady=5)

button_set = tk.Button(root, text="Set Reminder", command=set_reminder)
button_set.grid(row=1, columnspan=3, padx=5, pady=5)

root.mainloop()
