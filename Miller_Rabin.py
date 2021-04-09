'''
2.2  Write a program that implements the Miller–Rabin 
algorithm for a user- specified n. The program should 
allow the user two choices: (1) specify a possible wit-
ness a to test using the Witness procedure or (2) spec-
ify a number s of random witnesses for the Miller–Rabin 
test to check. Your program should accept the following 
command line arguments:

	-n <int> and -a <int> or -s <int>
'''
import random
from fastExp import fast_exp



def miller_rabin(q, n, witness=None):
	a = witness if witness!=None else random.randint(2, n-1)
	# fast exponentiation
	x = fast_exp(a, q, n)	
	if x == 1 or x == n-1:
		return True
	while q != n-1:
		x = (x**2) % n-1
		q *= 2
		if x == n-1:
			return True		#found a possibility
		if x == 1:
			return False	#hit the bottom
	return False		# failed to find a possible prime

def is_prime(n, witness=None, num_of_randos=None):
	if n == 2 or n == 3 or n == 5 or n == 7 or n == 9:
		return True
	if n < 2 or n%2 == 0:
		return False
	s = num_of_randos if num_of_randos != None else 1
	q = n-1
	while q&2 == 0:
		q //= 2
	for i in range(s):
		if miller_rabin(q, n) == False:
			return False
	return True


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--n', type=int, help='integer number')
	parser.add_argument('-a', '--witness', 
						type=int, help='integer fixed witness')
	parser.add_argument('-s', '--random', 
						type=int, help='integer number of random witnesses')
	args = parser.parse_args()

	if args.witness != None and args.random != None:
		#give error
		print("ERROR: -a and -s can't both be active")
		exit()
	if is_prime(args.n, args.witness, args.random):
		print("{} is possibly prime".format(args.n))
		exit()
	print('{} is not prime'.format(args.n))
	exit()
