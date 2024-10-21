# Question 2(a)
# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height(meters)
# as parameters and returns their BMI. (BMI = weight/height). Calculate and see BMI category:
# Below 18.5: "Underweight"
# 18.5 to 24.9: "Normal weight"
# 25 to 29.9: "Overweight"
# 30 or above: "Obese"
#Solution
def calculate_bmi():
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))
    bmi = weight / height
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
        return bmi, category
bmi_value, bmi_category = calculate_bmi()
print(f"The value of bmi is: {bmi_value:.2f}, and the category is: {bmi_category}")


# Question2(b)
# Use a function to calculate the volume of a cylinder v = pie*r**2*h. Choose a function name
# line with what you want to achieve. Radius r and height h should be in parameters. 
# Make sure you use the real pie value(import math) 
# Solution
import math
def calculate_cylinder_volume(radius,height):
    volume = math.pi*radius**2*height
    volume = calculate_cylinder_volume(radius,height)
    print(f"The volume of the cylinder is: {volume}")

