#Greg Phillips
#9/5/17
#tipCalculator.py

mealPrice = float(input("Write price of meal here "))
tipPercent = float(input("write percent tipped here "))
print("You should tip", round(mealPrice*(tipPercent/100), 2))
