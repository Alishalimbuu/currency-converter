with open ('currencyData.txt') as f:
    lines=f.readlines()
    
    
CurrencyDict ={}
for line in lines:
   parsed = line.split("\t")
   CurrencyDict[parsed[0]]= parsed[1]
print (CurrencyDict)
amount= int(input ("enter amount:\n"))
print("enter the name of currency you want to convert this amt to? Available Options:\n")
[print(item) for item in CurrencyDict.keys()]
currency= input ("please enter one of these values: \n")
print(f"{amount} NPR is equal to {amount * float(CurrencyDict[currency])} {currency}")

