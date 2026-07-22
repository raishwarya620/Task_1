import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("450x400")

# Heading
title = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Temperature label
label = tk.Label(root, text="Enter Temperature:")
label.pack()

# Input boxs
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# From Label
from_label = tk.Label(root, text="From")
from_label.pack()

# From Dropdown
from_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
from_unit.pack()
from_unit.current(0)

# To Label
to_label = tk.Label(root, text="To")
to_label.pack()

# To Dropdown
to_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
to_unit.pack()
to_unit.current(1)
# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"),fg="blue")
result_label.pack(pady=10)

# Function to convert temperature
def convert_temperature():
    try:
        temp = float(entry.get())
        from_u = from_unit.get()
        to_u = to_unit.get()

        if from_u == to_u:
            result = temp

        elif from_u == "Celsius" and to_u == "Fahrenheit":
            result = (temp * 9/5) + 32

        elif from_u == "Celsius" and to_u == "Kelvin":
            result = temp + 273.15

        elif from_u == "Fahrenheit" and to_u == "Celsius":
            result = (temp - 32) * 5/9

        elif from_u == "Fahrenheit" and to_u == "Kelvin":
            result = (temp - 32) * 5/9 + 273.15

        elif from_u == "Kelvin" and to_u == "Celsius":
            result = temp - 273.15

        elif from_u == "Kelvin" and to_u == "Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

root.mainloop()