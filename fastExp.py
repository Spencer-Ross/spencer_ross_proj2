'''
2.1  Write a program that implements fast exponentiation (successive squaring) modulo n. 
Your program should accept the following command line arguments:

 	-a <int>, -b <int> and -n <int>, for computing a^b mod n
'''

def fast_exp(base, exponent, mod):
	if exponent == 0:
		return 1
	if exponent == 1:
		return base % mod

	x = base
	y = base if (exponent%2 != 0) else 1
	exponent = int(exponent/2)
	while exponent > 0:
		x = x**2 % mod
		if exponent%2 != 0:
			y = x if (y==1) else (y*x)%mod
		exponent = int(exponent/2)
	return y


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', '--a', type=int, help='integer base operator')
	parser.add_argument('-b', '--b', type=int, help='integer exponent')
	parser.add_argument('-n', '--modulus', type=int, help='integer modulus')
	args = parser.parse_args()

	print(fast_exp(args.a, args.b, args.modulus))
