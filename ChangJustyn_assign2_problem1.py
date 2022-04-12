"""
Assignment #2, Problem #1
Justyn Chang
"""
#print title sequence
print("This program will project how much money you can earn by investing money in a high-yield savings account over a 3 month period.")
print()

#have user input initial investment amount and rate
invest = input("To begin, enter how much money you would like to initially invest (i.e. 500): ")
rate = input("Next, enter your projected annual interest rate. For example, enter 5 for 5%: ")

print()
print("------- Calculating -------")
print()

#create labels for month, starting balance, interest, and ending balance, and then align
month = "Month"
start_balance = "Starting Balance"
interest = "Interest"
end_balance = "Ending Balance"

fmonth = format(month, "<1s")
fstart_balance = format(start_balance, "<19s")
finterest = format(interest, "<10s")


print(fmonth, fstart_balance, finterest, end_balance)

#calculate starting balance, interest, and ending balance for first month, then print
month1 = "1"
fl_invest = float(invest)
month1_bal = format(fl_invest, ",.2f")
fl_rate = float(rate)
rate_percent = fl_rate / 100
monthly_rate = rate_percent / 12
month1_int = format(monthly_rate * fl_invest, ",.2f")
fl_month1_int = float(monthly_rate * fl_invest)
month1_end = format(fl_month1_int + fl_invest, ",.2f")

fmonth1 = format(month1, "<5s")
fmonth1_bal = format(month1_bal, "<19s")
fmonth1_int = format(month1_int, "<10s")
      
print(fmonth1, fmonth1_bal, fmonth1_int, month1_end)

#calculate starting balance, interest, and ending balance for second month, then print
month2 = "2"
fl_invest2 = float(fl_month1_int + fl_invest)
month2_bal = format(fl_invest2, ",.2f")
month2_int = format(monthly_rate * fl_invest2, ",.2f")
fl_month2_int = float(monthly_rate * fl_invest2)
month2_end = format(fl_month2_int + fl_invest2, ",.2f")

fmonth2 = format(month2, "<5s")
fmonth2_bal = format(month2_bal, "<19s")
fmonth2_int = format(month2_int, "<10s")
      
print(fmonth2, fmonth2_bal, fmonth2_int, month2_end)

#calculate starting balance, interest, and ending balance for third month, then print
month3 = "3"
fl_invest3 = float(fl_month2_int + fl_invest2)
month3_bal = format(fl_invest3, ",.2f")
month3_int = format(monthly_rate * fl_invest3, ",.2f")
fl_month3_int = float(monthly_rate *fl_invest3)
month3_end = format(fl_month3_int + fl_invest3, ",.2f")

fmonth3 = format(month3, "<5s")
fmonth3_bal = format(month3_bal, "<19s")
fmonth3_int = format(month3_int, "<10s")
      
print(fmonth3, fmonth3_bal, fmonth3_int, month3_end)
