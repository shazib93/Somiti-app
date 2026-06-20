try:
    boyos = int(input("Boyos dao: "))
    print(f"Tomar boyos {boyos}")
except ValueError:
    print("Shudhu number dao!")
finally:
    print("Program shesh hoyeche.")