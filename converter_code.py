convert = input("Would you like to convert WEIGHT, HEIGHT or TEMPERATURE? ")

print( "You have chosen " + convert) 

if convert == "WEIGHT":
   weight = float(input("Input weight in POUNDS: "))
   kg = float(weight / 2.205)
   print(str(weight) + " in pounds is equal to " + str(kg) + " in kilograms.") 
elif convert == "HEIGHT": 
   height = float(input("Input height in INCHES: "))
   cm = float(height * 2.54)
   print(str(height) + " in inches is equal to " + str(cm) + " in centimeters.")
elif convert == "TEMPERATURE":
   temp = float(input("Input temperature in Fahrenheit: "))
   cel = (temp - 32.0) * (5/9) 
   print(str(temp) + " Fahrenheit is equal to " + str(cel) + " in Celsius.")
else:
  print("That is incorrect.")
