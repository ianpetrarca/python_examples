capital = input("Enter Starting Capital: $")
monthly_percent = input("Enter Montly Gain: %")

def compound(capital,monthly_percent):
    for i in range(0,12):
        capital = int(capital) * ((int(monthly_percent)/100)+1)
    print(int(capital))
    
compound(capital,monthly_percent)