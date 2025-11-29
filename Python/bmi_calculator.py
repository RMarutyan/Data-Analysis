'''
1. Write a Python script that defines a function calculate_bmi(weight, height) to calculate a
persons Body Mass Index (BMI) using the formula:
2. python
3. BMI = weight (kg) / (height (m) ** 2)
4. Include the if __name__ == "__main__": block to:
● Take user input for weight (in kilograms) and height (in meters).
● Call the calculate_bmi() function to calculate BMI.
● Print a message to classify the BMI:
● BMI < 18.5: "Underweight"
● 18.5 <= BMI < 25: "Normal weight"
● 25 <= BMI < 30: "Overweight"
● BMI >= 30: "Obese"
5. Save the script as bmi_calculator.py.'''
#Function to calculate Body Mass Index (BMI)
def calculate_bmi(weight, height):
    bmi = weight/ (height ** 2)
    return bmi
#inputs
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
#calculation
bmi = calculate_bmi(weight, height)
#classification
if bmi < 18.5:
    print("Your BMI is", round(bmi,2), "which is classified as Underweight.")
elif 18.5 <= bmi < 25:
    print("Your BMI is", round(bmi,2), "which is classified as Normal weight.")
elif 25 <= bmi < 30:
    print("Your BMI is", round(bmi,2), "which is classified as Overweight.")        
else:
    print("Your BMI is", round(bmi,2), "which is classified as Obese.") 
