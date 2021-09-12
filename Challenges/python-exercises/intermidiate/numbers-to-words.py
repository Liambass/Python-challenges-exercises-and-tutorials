num2words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}

def hundreds(hun):
    hout = ""
    if (hun >= 100):
        hout += f"{num2words[hun // 100]} Hundred"
        hun = hun % 100
    if hout != "" and hun != 0:
        hout += " and "
    if (hun >= 20):
        hout += f"{num2words[(hun // 10)*10]} {num2words[hun % 10]}"
    elif (hun != 0):
        hout +=f"{num2words[hun]}"
    return hout

def thousands(thou):
    if thou != 0:
        return f"{hundreds(thou)} Thousand "
    else:
        return ""

def millions(mil):
    if mil != 0:
        return f"{hundreds(mil)} Million "
    else:
        return ""

def billions(bil):
    if bil != 0:
        return f"{hundreds(bil)} Billion "
    else:
        return ""

def trillions(tril):
    if tril != 0:
        return f"{hundreds(tril)} Trillion "
    else:
        return ""

def words(num):
    
    tril = num // 1000000000000
    bil = (num % 1000000000000) // 1000000000
    mil = (num % 1000000000) // 1000000
    thou = (num % 1000000) // 1000
    hun = (num % 1000)
    return trillions(tril)+billions(bil)+millions(mil)+thousands(thou)+hundreds(hun)

num = input("Which number would you like to convert to words? ")
while not (num.isdigit() and (len(num) <= 15)):
    num = input("Please input a valid number less than 10^15 ")
num = int(num)
print(words(num))
