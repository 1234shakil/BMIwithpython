wight = int(input('Enter your wigth (kg):'))
hieght = int(input('Enter your hieght (in):'))

this_bmi = wight / ((hieght * 0.0254)**2)

if this_bmi < 18.4 :
    print(f"Your BMI is : {this_bmi} Underwigth")
    print('Your code is succesfuly run')
elif this_bmi > 18.5 and this_bmi < 24.9 :
    print(f"Your BMI is : {this_bmi} Normal")
    print('Your code is succesfuly run')
elif this_bmi > 25.0 and this_bmi < 39.9 :
    print(f"Your BMI is : {this_bmi} Overwigth")
    print('Your code is succesfuly run')
elif this_bmi > 40.0 :
    print(f"Your BMI is : {this_bmi} Obese")
    print('Your code is succesfuly run')
