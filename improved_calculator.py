while True:
  print("Initializing calculator... Type 'quit' to exit")
  operator = str(input("Enter an operator (+, -, *, /): "))
  if operator == "quit":
    print("Calculator turned off")
    break

  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter another number: "))

  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    result = num1 / num2
  else:
    print("Invalid operator")

  print(f"{num1} {operator} {num2} = {result}")