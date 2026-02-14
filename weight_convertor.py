weight = float(input("Weight: "))
measure = print("Type 'K/k' if Kg or 'L/l'if Lbs")
unit = input("Kg or Lbs: ")

if unit.upper() == "L":
    weight_in_kg = weight // 2.2
    print("Weight in Kg: " + str(weight_in_kg))
elif unit.upper() == "K":
    weight_in_lbs = weight * 2.2
    print("Weight in Lbs: " + str(weight_in_lbs))
else:
    print("Cannot convert weight")
          