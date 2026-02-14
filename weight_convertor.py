weight = int(input("Weight: "))
measure = print("Type 'K' if Kg or 'L'if Lbs")
unit = input("Kg or Lbs: ")

if unit == "L":
    weight_in_kg = weight / 2.2
    print("Weight in Kg: " + str(weight_in_kg))
elif unit == "K":
    weight_in_lbs = weight * 2.2
    print("Weight in Lbs: " + str(weight_in_lbs))
else:
    print("Cannot convert weight")
          