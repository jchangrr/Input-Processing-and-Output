"""
Assignment #2, Problem #2
Justyn Chang
"""
#have user input two numbers between 0 and 999
number1_input = input("Enter a number between 0 and 999: ")
number2_input = input("Enter another number between 0 and 999: ")

#convert to integers
number1 = int(number1_input)
number2 = int(number2_input)

#separate ones place
number1_ones = number1 % 10
number2_ones = number2 % 10

#separate tens place
number1_tens = (number1 // 10) % 10
number2_tens = (number2 // 10) % 10

#separate hundreds place
number1_hundreds = (number1 // 10) // 10
number2_hundreds = (number2 // 10) // 10

#add ones place
ones_sum = number1_ones + number2_ones
#add tens place
tens_sum = number1_tens + number2_tens
#add hundreds place
hundreds_sum = number1_hundreds + number2_hundreds

#create labels for ones, tens, and hundreds places
ones_title = format("Sum of ones", "<15s")
tens_title = format("Sum of tens", "<15s")
hundreds_title = format("Sum of hundreds", "<15s")

#print results of adding each place values
print(ones_title, "=", number1_ones, "+", number2_ones, "=", ones_sum)
print(tens_title, "=", number1_tens, "+", number2_tens, "=", tens_sum)
print(hundreds_title, "=", number1_hundreds, "+", number2_hundreds, "=", hundreds_sum)
