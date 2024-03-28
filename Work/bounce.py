# bounce.py
#
# Exercise 1.5
bounce_ratio = 3/5
i = 1
bounce = 1
while i <= 10:
	bounce = bounce * bounce_ratio
	print(round(100*bounce,4))
	i = i + 1 
