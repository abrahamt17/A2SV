class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        kelvin_str = "{:.5f}".format(kelvin)
        fahrenheit_str = "{:.5f}".format(fahrenheit)
        return [float(kelvin_str), float(fahrenheit_str)]
         
         
   
   
    
    # Convert Celsius to Fahrenheit
   
    
    # Return the results formatted to five decimal places
 


