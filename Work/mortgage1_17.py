# mortgage.py
#
# Exercise 1.8
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_counter = 0 
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

while principal > 0:
	principal = principal * (1 + rate /12) - payment

	total_paid = total_paid + payment
	if month_counter >= extra_payment_start_month and month_counter < extra_payment_end_month:
		principal = principal - extra_payment
		total_paid = total_paid + extra_payment
	month_counter = month_counter + 1
	if principal < 0:
		total_paid = total_paid + principal
		principal = 0.0
	print(f'{month_counter:5d} {total_paid:10.2f} {principal:10.2f}')

print('Total Paid : ', f'{total_paid:10.2f}')
print('Month      : ', f'{month_counter:10d}')