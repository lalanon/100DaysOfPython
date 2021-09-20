# Day 002
# Tips Calculator

# Tips are 10% here
TIP = 0.1

bill = float(input("How much is the bill: "))

print("\nAt " + "{:.2f}".format(TIP*100) + " percet tip:")
print("Tip: " + "{:.2f}".format(bill*TIP))
print("For a total of: " + "{:.2f}".format(bill + bill*TIP))
