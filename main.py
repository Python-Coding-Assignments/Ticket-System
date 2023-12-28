import Constants.constant as constant

#declarations and initializations of variables
numAdults = numChildren = numSeniors = 0
totalBeforeTax = totalTax = totalAfterTax = 0

#getting input from user
print("FSU Football 2022 Ticket Purchasing System\n")
print("Input the number of:\n\tAdults\n\tChildren (up to age 12)\n\tSeniors (65+)")
numAdults = int(input("Adults --> "))
numChildren = int(input("Children --> "))
numSeniors = int(input("Seniors --> "))
print("-------------------------------")

#calculating total cost, before and after tax, and tax amount
totalBeforeTax = (numAdults * constant.adults) + (numChildren * constant.children) + (numSeniors * constant.seniors)
totalTax = totalBeforeTax * constant.tax
totalAfterTax = totalBeforeTax + totalTax

#printing cost information to user
print("TOTAL (before tax) = $" + str(round(totalBeforeTax, 2)) + "\nTax = $" + str(round(totalTax, 2)))
print("TOTAL COST (after tax) = $" + str(round(totalAfterTax, 2)))
print("\nThanks for purchasing your tickets!")