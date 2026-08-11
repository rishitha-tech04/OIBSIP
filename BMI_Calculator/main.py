print("BMI Calculator")

try:
    weight = float(input("Enter your weight kg: "))
    height = float(input("Enter your height meters: "))

    if weight >0 and height >0:
        bmi= weight /(height*height)

        print("BMI is:", round(bmi, 1))

        if bmi < 18.5:
            print("category: underweight")
        elif bmi < 25:
            print("categoty: normal")
        elif bmi < 30:
            print("category: overweight")
        else:
            print("category: obese")
    else:
        print("weight and height must be generated than zero")

except ValueError:
    print("Please enter numbers only.")