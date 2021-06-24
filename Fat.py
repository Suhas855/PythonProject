Weight = input("How much do you weigh: ")
Units = input("Kg or Lb: ")
lb = 2.20462262 * int(Weight)
rounded_lb = round(2.20462262 * int(Weight))
kg = int(Weight) / 2.20462262
rounded_kg = round(int(Weight) / 2.20462262)
if Units == "K" or Units == "k":
    print("Your weight is " + Weight + " kgs")
    print("Your weight is " + str(lb) + "lbs or " + str(rounded_lb))
elif Units == "L" or Units == "l":
    print("Your weight is " + Weight + " lbs")
    print("Your weight is " + str(kg) + " kgs or " + str(rounded_kg))
else:
    print("Enter a valid weight or unit")
