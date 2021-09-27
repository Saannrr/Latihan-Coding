# Tugas mengkonversikan Fahrenheit ke Kelvin dan sebaliknya

print("\nPROGRAM KONVERSI TEMPERATUR UNTUK KELVIN ke FAHRENHEIT\n")

kelvin = float(input('Masukkan suhu dalam Kelvin : '))
print("suhu adalah",kelvin, "Kelvin")

# rumusnya kelvin ke fahrenheit
fahrenheit = ((9/5) * kelvin - 273) + 32
print('Suhu dalam Fahrenheit adalah = ',fahrenheit,'Fahrenheit')