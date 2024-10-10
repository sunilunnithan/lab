def lucas():
	yield 2
	a = 2 
	b = 1
	while True:
		yield b
		a, b = b, a + b # tuple unpacking


# for x in lucas():
# 	print(x)


#pring the sum of first ten million square
# the paren in sum is used as a generator function
# if we use list, it will consume 40MB of memory
sum_million = sum(x*x for x in range(1000000 + 1))
print(sum_million)

# sum of first 1000 prime
from mutils import is_prime
first_1000= sum(x for x in range(1001+1) if is_prime(x))
print(first_1000)

from itertools import islice, count
is_slice_1000 = islice((x for x in count() if is_prime(x)),1000)
print(is_slice_1000)

#zip
sunday = [60,90,80,30,40]
monday = [50,90,80,90,40]
tuesday = [90,70,80,60,40]


for item in zip(sunday,monday):
	print(item)

for temps in zip(sunday,monday,tuesday):
	print("min = {:4.1f} max = {:4.1f} average = {:4.1f}".format(max(temps), min(temps),sum(temps)/ len(temps)))


	