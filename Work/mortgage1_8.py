# mortgage.py
#
# Exercise 1.8
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_counter = 0 
additional_payment = 1000.0

while principal > 0:
	principal = principal * (1 + rate /12) - payment
	total_paid = total_paid + payment
	while month_counter < 12:
		principal = principal - additional_payment
		total_paid = total_paid + additional_payment
		month_counter = month_counter + 1

print('Total Paid', round(total_paid,2))