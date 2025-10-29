weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Overweight"
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")
