
print("Zadejte urokovou sazbu")
rate = input()

print("Zadejte vysku uveru")
amount = input()

print("Zadejte pocet let splaceni")
years = input()

factor = 1/(1+(int(rate)/100))

# print(rate + " " + amount + " " + years + " " + str(factor))

# annuity calculation

annuity = int(amount)*((int(rate)/100)/(1-factor**int(years)))

print(annuity)

urok = int(annuity)*(1-(int(factor)**10))

print(urok)