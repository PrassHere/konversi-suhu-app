# let's goo dawg we build a konverter app 

import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        suhu_awal = float(entry_input.get())
        satuan = combo_unit.get()

        if satuan == "Celsius ke Fahrenheit":
            hasil = (suhu_awal * 9/5) + 32
            label_result.config(text=f"Hasil: {hasil:.2f} °F")
        elif satuan == "Fahrenheit ke Celsius":
            hasil = (suhu_awal - 32) * 5/9
            label_result.config(text=f"Hasil: {hasil:.2f} °C")
        elif satuan == "Celsius ke Kelvin":
            hasil = suhu_awal + 273.15
            label_result.config(text=f"Hasil: {hasil:.2f} K")
        elif satuan == "Kelvin ke Celsius":
            hasil = suhu_awal - 273.15
            label_result.config(text=f"Hasil: {hasil:.2f} °C")
        else:
            label_result.config(text="Pilih satuan yang valid")
    except ValueError:
        label_result.config(text="Masukkan angka yang valid")

# GUI
app = tk.Tk()
app.title("Konversi Suhu App")
app.geometry("300x250")

label_input = tk.Label(app, text="Masukkan Suhu:")
label_input.pack(pady=5)

entry_input = tk.Entry(app)
entry_input.pack(pady=5)

combo_unit = ttk.Combobox(app, values=[
    "Celsius ke Fahrenheit",
    "Fahrenheit ke Celsius",
    "Celsius ke Kelvin",
    "Kelvin ke Celsius"
])
combo_unit.pack(pady=5)
combo_unit.current(0)

button_convert = tk.Button(app, text="Konversi", command=convert_temperature)
button_convert.pack(pady=10)

label_result = tk.Label(app, text="Hasil: ")
label_result.pack(pady=5)

app.mainloop()



