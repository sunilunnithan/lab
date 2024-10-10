# list comprehension
words = "It is easy to ask for forgiveness than permissions".split()

word_len = [len(word) for word in words]

print(word_len)

# list comprehension with a condition
from mutils import is_prime
print(is_prime(100))	
all_prime = [ x for x in range(100+1) if is_prime(x) ]
print(all_prime)
					
				
 