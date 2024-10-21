# QUESTION1 (a)
# Temperature Classifier: Using a function, write a Python script that takes a temperature
# as input and classifies it into the following categories:
# Below 0° C: Freezing
# 0 to 10° C : Cold
# 11 to 20° C: Moderate
# 21 to 30° C: Warm
# Above 30° C: Hot
def classify_temperature(temperature):
    if temperature < 0:
        return "Freezing"
    elif 0 <= temperature <= 10:
        return "Cold"
    elif 11 <= temperature <= 20:
        return "Moderate"
    elif 21 <= temperature <= 30:
        return "Warm"
    else:
        return "Hot"
        temp = float(input("Enter the temperature in °C: "))
        classification = classify_temperature(temp)
        print(f"The temperature is classified as: {classification}")


# QUESTION1 (b)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere
# with radius 8.
# Use a function and make sure the radius is entered from the keyboard and provide the 
#answer in 1 decimal
# Solution:
def volume_of_the_sphere():
    import math
    radius = int(input("/nEnter the radius of the sphere: "))
    pie = math.pi
    volume = (4/3)*pie*radius**2
    print(f"The volume of the sphere with radius {radius} is {volume:.1f}")
    volume_of_the_sphere()