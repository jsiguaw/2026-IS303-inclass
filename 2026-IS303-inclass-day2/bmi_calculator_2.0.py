"""

Inputs:
- name
- height
- weight
- age
- sex

Processes:
- Input Validation
- Calculate BMI = weight / height**2 * 703
- Categorize BMI:
    - Underweight: BMI < 18.5
    - Normal weight: 18.5 <= BMI < 25
    - Overweight: 25 <= BMI < 30
    - Obese: BMI >= 30
    - Severely Obese: BMI >= 40

Outputs:
- Report for an individual

"""

#INPUTS
name = input("Name: ")
height = input("Height (inches): ")
weight = input("Weight (pounds): ")
age = input("Age: ")
sex = input("Sex (Male/Female): ").lower()

# Input Validation
age = age.replace(".","",1) 
age_is_int = age.isdigit()
if age_is_int == True:
    age = int(age)
age_is_reasonable = True
if age_is_int == True and (age <= 120 and age >= 1):
    age_is_reasonable = True

sex = sex.lower()
sex_is_valid = True
if sex == "Male" or sex == "Female":
    sex_is_valid = True

height = height.replace(".","",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = True
if height_is_int == True and (height <= 120 and height >= 12):
    height_is_reasonable = True

weight = weight.replace(".","",1)
weight_is_int = weight.isdigit()
if height_is_int == True:
    weight = int(weight)    
weight_is_reasonable = True
if weight_is_int == True and (weight <= 500 and weight >= 25):
    weight_is_reasonable = True

ready_to_process = True

if age_is_int == False or age_is_reasonable == False:
    print("You entered a non-expected age, please use whole numbers between 1 and 120.")
    ready_to_process = False

if sex_is_valid == False: 
    print("You entered a non-expected sex, please enter a valid sex.")
    ready_to_process = False

if height_is_int == False or height_is_reasonable == False:
    print("You entered a non-expected height, please use whole numbers between 12 and 120.")
    ready_to_process = False

if weight_is_int == False or weight_is_reasonable == False:
    print("You entered a non-expected weight in pounds, please use whole numbers between 25 and 500.")
    ready_to_process = False

"""

- Calculate BMI = weight / height**2 * 703
- Categorize BMI:
    - Underweight: BMI < 18.5
    - Normal weight: 18.5 <= BMI < 25
    - Overweight: 25 <= BMI < 30
    - Obese: BMI >= 30
    - Severely Obese: BMI >= 40

"""

if ready_to_process == True:
    bmi = (weight / height ** 2) * 703
    bmi_catagory = ""
    if bmi < 18.5:
        bmi_catagory = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        bmi_catagory = "Normal weight"
    elif bmi >= 25 and bmi < 30:    
        bmi_catagory = "Overweight"
    elif bmi >= 30 and bmi < 40:
        bmi_catagory = "Obese"
    elif bmi >= 40:
        bmi_catagory = "Severely Obese"
    else:
        bmi_catagory = "Unknown"

    # Report
    print(f"Report for {name}:\n"
        f"{age} year old {sex}\n"
        f"Your BMI is {bmi}\n"
        f"Your BMI catagory is: {bmi_catagory}")
    
    
    
