# Item Cost
num = float(input("Enter a Purchase Price: "))
# loyalty Points
num_2 = float(input("Enter Loyalty Points: "))
# THC Percentage
num_3 = float(input("Enter THC Amount: "))
# Veteran Discount
vet_disc = float(num * .10)

# Taxes to be collected
weed_tax_1 = float(num * .0789)
weed_tax_2 = float(num * .0705)
weed_tax_3 = float(num * .04)
weed_tax_4 = float(num * .10)

tax_total = weed_tax_1 + weed_tax_2 + weed_tax_3
tax_total_2 = weed_tax_1 + weed_tax_2 + weed_tax_3 + weed_tax_4

# Sums of totals


# if statement for percentage totals
if(num_3 <= 35):
    print("Total Taxes for less than 35% = ","$", tax_total)
    print("Total with taxes and discounts = ","$",)
    print("Total without taxes and discounts = ","$",)
else:
    print("Total Taxes for greater than 35% = ","$", tax_total_2)
    print("Total with taxes and discounts = ","$",)
    print("Total without taxes and discounts = ","$",)

#print("Veteran Discount = ","$", vet_disc)
#print("Total without discounts", "$", total_2 )
#print("Total with discounts = ","$", total)