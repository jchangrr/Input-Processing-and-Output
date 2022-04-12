"""
Assignment #2, Problem #4
Justyn Chang
"""
#print title sequence
print("--------------------------------------------------------------")
title = format("mL Conversion Calculator", ">40")
print(title)
print("--------------------------------------------------------------")
print()

#create input for mL to convert and convert to float
mL_input = input("How many mL would you like to convert? ")
mL_float = float(mL_input)
mL = format(mL_float, ".2f")
#display mL to convert
print(mL, "mL ", end = "...")
print()
print()

#create labels for teaspoons, tablespoons, microliters, and nanoliters
tspn_title = format("... in teaspoons", "<18s")
tbspn_title = format("... in tablespoons", "<18s")
microliter_title = format("... in microliters", "<18s")
nliter_title = format("... in nanoliters", "<18s")

#convert mL to teaspoons, tablespoons, microliters, and nanoliters
tspn_convert = format(mL_float / 4.929, ",.2f")
tspn_fconvert = format(tspn_convert, ">20s")
tbspn_convert = format(mL_float / 14.787, ",.2f")
tbspn_fconvert = format(tbspn_convert, ">20s")
microliter_convert = format(mL_float * 1000, ",.2f")
microliter_fconvert = format(microliter_convert, ">20s")
nliter_convert = format(mL_float * 1000000, ",.2f")
nliter_fconvert = format(nliter_convert, ">20s")

#print conversions and align
print(tspn_title, tspn_fconvert, "tsp")
print(tbspn_title, tbspn_fconvert, "tbsp")
print(microliter_title, microliter_fconvert, "uL")
print(nliter_title, nliter_fconvert, "nL")

#5 ways to crash the program:
#Syntax Errors:
#print(Hello World!)
#1variable = "apple"
#Logic Errors:
#division = 2 / 0
#undefined_variable = apple + 2
#Logic Error:
#num1 = int(input("Choose a number: ")
#num2 = int(input("Choose another number: ")
#difference = num1 + num2
#print("The difference is", difference)
