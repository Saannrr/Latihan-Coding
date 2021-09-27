# Tugas mengkonversikan Fahrenheit ke Kelvin dan sebaliknya

print("\nPROGRAM KONVERSI TEMPERATUR UNTUK FAHRENHEIT ke KELVIN\n")

fahrenheit = float(input('Masukkan suhu dalam Fahrenheit : '))
print("suhu adalah",fahrenheit, "Fahrenheit")

# rumusnya fahrenheit ke kelvin
kelvin = ((5/9) * fahrenheit - 32) + 273
print('Suhu dalam Kelvin adalah = ',kelvin,'Kelvin')