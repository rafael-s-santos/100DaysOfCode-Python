#print(len("Hello"))
#print("Hello"[4])

# num_char = len(input("Whats your name ?"))
# new_num_char = str(num_char)
# print("Seu nome tem " + new_num_char + " caracteres" )

#print(type(new_num_char))

# print(70 + float(100.5))

# valor = input("Digite seu numero aqui !\n")
# digito1 = valor[0]
# digito2 = valor[1]
# result = int(digito1) + int(digito2)
# # print(type(soma))

# print("O resultado e " + str(result))

# PEMDAS LR
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtration -

# print(3 * (3 + 3) / 3 - 3)

# weight = input("Input your weight here \n")
# height = input("Input your height here \n")
# float_weight = float(weight)
# float_height = float(height)

# bmi = float_weight / float_height ** 2
# int_bmi = int(bmi)


# print("Seu IMC e " + str(int_bmi))

# print(8 / 4)

# score = 0
# altura = 1.8
# IsWinning = True

# print(f"your score is {score}, sua altura is {altura}, seu boleano e {IsWinning}")


#You have x days, y weeks, and z months left.
#There are 365 days in a year, 52 weeks in a year and 12 months in a year.
#You have 12410 days, 1768 weeks, and 408 months left

# your_age = input("Qual sua idade ? \n")
#GO HORSE
# your_days = int(your_age) * 365
# your_weeks = int(your_age) * 52
# your_months = int(your_age) * 12

# days_90 = (90 * 365) - your_days
# week_90 = (90 * 52) - your_weeks
# months_90 = (90 * 12) - your_months
# days_90 = int(your_age) * 365
# week_90 = int(your_age) * 52
# months_90 = int(your_age) * 12
# message = f"There are {days_90} days, {week_90} weeks, and {months_90} months to last goodbye "
# # print(f"You have {your_days} days, {your_weeks} weeks, and {your_months} months")
# print(message)

## Each person should pay (150.00 / 5 ) * 1.12

# #ENTRADAS DO PROGRAMA
# print("Welcome to the tip calculator")
# valor = float(input("What the value to pay ? R$"))
# gorgeta_bruta = int(input( "How much tip would you like to give? 10/12/15 ? "))
# pagoes = int(input("How many people to split the bill?"))

# #Calcula o valor da gorgeta e apresenta o valor total
# #gorgeta = ( gorgeta_bruta / 100 ) * valor
# valor_total = ( valor + (( gorgeta_bruta / 100 ) * valor))
# # print(valor_total)
# # print(type(valor_total))

#Calcula o valor total a ser pago e apresenta em tela, e ajusta a mesma variavel para entregar sempre dois decimais no final
# valor_final = round(valor_total / pagoes, 2)
# valor_final = "{:.2f}".format(valor_final)
# mensagem_final = f"Each person should pay: ${valor_final} reais"
# print(mensagem_final)

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi_result = weight / (height * height)
# bmi = round(weight / height ** 2)
# bmi_result = 28

if ( bmi_result < 18.5 ):
    print(f"Your BMI is {bmi_result}, you are underweight.")
elif ( bmi_result < 25 ):
    print(f"Your BMI is {bmi_result}, you have a normal weight.")
elif ( bmi_result < 30 ):
    print(f"Your BMI is {bmi_result}, you are slightly overweight.")
elif ( bmi_result < 35 ): 
    print(f"Your BMI is {bmi_result}, you are obese.")
else: 
    print(f"Your BMI is {bmi_result}, you are clinically obese.")