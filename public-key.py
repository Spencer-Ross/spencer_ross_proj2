import sys, argparse
from random import getrandbits
from fastExp import fast_exp
from Miller_Rabin import is_prime 

rands: int = 10 # number of checks for isPrime

def keygen():
	pubName: str = 'pubkey.txt'
	priName: str = 'prikey.txt'
	p = getPrime(bits=32)
	# print(p)

def getPrime(bits=8):
	p: int = getrandbits(bits)
	while not is_prime(n=p, num_of_randos=rands):
		p = getrandbits(bits)
	print('p is {}'.format(p))


def encrypt():
	pass
def decrypt():
	pass

def main(args):
	inputfile: str  = args.inputfile
	outputfile: str = args.outputfile
	key: bool = args.keygen
	e: bool	  = args.e_flag
	d: bool	  = args.d_flag

	if key:
		keygen()
	elif e:
		encrypt()
	elif d:
		decrypt()
	else:
		print("ERROR: no options specified")
		exit()

	
	# output.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-e', '--e_flag', action='store_true', help='encrypt input file')
	parser.add_argument('-d', '--d_flag', action='store_true', help='decrypt input file')
	parser.add_argument('-in', '--inputfile', help='specify input file')
	parser.add_argument('-out', '--outputfile', help='specify output file')
	parser.add_argument('-keygen', '--keygen', action='store_true', help='specify key file')
	args = parser.parse_args()
	if (args.e_flag and args.d_flag) or (args.keygen and (args.e_flag or args.d_flag)):
		#give error
		print("ERROR: conflicting flags active")
		exit()
	main(args)
