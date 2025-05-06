print('This file is used to perform Cloud Computing Practical (Google Colud Console). \n The program is used to greet someone or user')
def greet():
  name = input("Enter your Name ")
  print("Greetings ",name)
  print("Using this program you can perform addition operation.\nDo you want to perform? ")
  choice = input("If yes enter yes ")
  choice.lower()
  if choice == 'yes':
    re=addition()
    print("Addition of two numbers is ",re)

def addition():
  print("Enter below two numbers which are required to do addition ")
  num1 = int(input("Enter first number "))
  num2 = int(input("Enter second number "))
  result = num1 + num2
  return result

greet()
