temp = float(input("Enter body temperature: "))

if temp >= 85.0 and temp <= 91.0:
    print("Serious Hypothermia")

if temp > 91.0 and temp < 95.0:
    print("Mild Hypothermia")

if temp >= 95.0 and temp <= 98.0:
    print("Normal Temperature")

if temp > 98.0 and temp <= 100.0:
    print("Mild Fever")

if temp > 100.0 and temp <= 105.0:
    print("High Fever")
