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
app.geometry("350x300")
app.configure(bg="#f5f5f5")

style = ttk.Style()
style.theme_use("clam")

# Frame utama
frame = tk.Frame(app, bg="#ffffff", bd=2, relief="groove")
frame.pack(padx=20, pady=20, fill="both", expand=True)

label_title = tk.Label(frame, text="Konversi Suhu", font=("Segoe UI", 14, "bold"), bg="#ffffff", fg="#333333")
label_title.pack(pady=10)

label_input = tk.Label(frame, text="Masukkan Suhu:", font=("Segoe UI", 10), bg="#ffffff")
label_input.pack(pady=5)

entry_input = tk.Entry(frame, font=("Segoe UI", 10))
entry_input.pack(pady=5, ipady=3)

combo_unit = ttk.Combobox(frame, font=("Segoe UI", 10), values=[
    "Celsius ke Fahrenheit",
    "Fahrenheit ke Celsius",
    "Celsius ke Kelvin",
    "Kelvin ke Celsius"
], state="readonly")
combo_unit.pack(pady=5)
combo_unit.current(0)

button_convert = tk.Button(frame, text="Konversi", command=convert_temperature,
                           font=("Segoe UI", 10, "bold"), bg="#4cafef", fg="white",
                           activebackground="#2196f3", activeforeground="white", bd=0, relief="flat")
button_convert.pack(pady=10, ipadx=10, ipady=5)

label_result = tk.Label(frame, text="Hasil: ", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#333333")
label_result.pack(pady=5)

app.mainloop()
