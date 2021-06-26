print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
your_Choice = str(input("Your choice: ")).upper()
if your_Choice == "C" :
    starting_Temperature = float(input("Please enter the temperature in Fahrenheit: "))
    temperature_Celsius = (starting_Temperature-32)*5/9
    print("The temperature in Celsius is ",temperature_Celsius,".")
elif your_Choice == "F" :
     starting_Temperature = float(input("Please enter the temperature in Celcius: "))
     temperature_Fahrenheit = (starting_Temperature * 9/5) + 32
     print("The temperature in Fahrenheit is ",temperature_Fahrenheit,".")
    
    
    

