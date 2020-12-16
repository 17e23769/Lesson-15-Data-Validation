print("Enter a number between 1 and 10:")
not_validated = True
while not_validated:
  try:
    number = int(input())
    print (f"number is {number}")
    not_validated = False
  except ValueError:
    print("You must enter a number between 1 and 10:")

if number <11 and number >0:
  not_validated = False
else:
  print("number is out of range, try again")
  not_validated = True