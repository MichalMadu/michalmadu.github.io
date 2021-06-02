spotreba = int(input("Zadej spotrebu: "))
najezd = int(input("Zadej celkovy najezd: "))
cenabenzinu = int(input("Zadej cenu benzinu: "))

celkemspotreba = najezd / 100 * spotreba
celkemcena = celkemspotreba * cenabenzinu

print("Celkova spotreba:")
print(celkemspotreba)
print("Celkem cena:")
print(celkemcena)
print("CZK")
