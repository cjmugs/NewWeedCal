# Item Cost
num = float(input("Enter a Purchase Price: "))
# loyalty Points
num_2 = float(input("Enter Loyalty Points: "))
# THC Percentage
num_3 = float(input("Enter THC Amount: "))
# Veteran Discount
vet_disc = float(num * .10)

# Taxes to be collected
weed_tax_1 = float(num * .0896)
weed_tax_2 = float(num * .0864)
weed_tax_3 = float(num * .04)
weed_tax_4 = float(num * .10)

tax_total = weed_tax_1 + weed_tax_2 + weed_tax_3
tax_total_2 = weed_tax_1 + weed_tax_2 + weed_tax_3 + weed_tax_4

# Sums of totals without discounts
result_1 = num + tax_total 
result_2 = num + tax_total_2

# Sums of totals with discounts
result_3 = num + tax_total - vet_disc - num_2
result_4 = num + tax_total_2 - vet_disc - num_2
# if statement for percentage totals
if(num_3 <= 35):
    print("Total Taxes for less than 35% THC = ","$", tax_total)
    print("Total with taxes and veteran discount = ","$", result_3)
    print("Total with taxes and without discounts = ","$", result_1)
else:
    print("Total Taxes for greater than 35% THC = ","$", tax_total_2)
    print("Total with taxes and veteran discount = ","$", result_4)
    print("Total with taxes and without discounts = ","$", result_2)

