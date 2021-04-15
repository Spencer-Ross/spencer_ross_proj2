# imports and globals
import sys, argparse, random
from random import getrandbits
from fastExp import fast_exp
from Miller_Rabin import is_prime 

rands: int = 10 	# number of checks for isPrime
wordSize: int = 4 	# number of bytes/word

# Key Related Functions --------------------------------------------------------------
def gen_key():
	''' Generates the public and private keys.
		It will overwrite existing files of the
		same name, and the generator is always
		2 and the prime is derived from this
	'''
	pubName: str = 'pubkey.txt'
	priName: str = 'prikey.txt'
	# these values are hardcoded for the assignment
	bits: int = 32
	gen2: int = 2
	prime: int = generator(k=bits)
	randNum: int  = random.randint(a=1, b=(prime-1))
	e2: int = fast_exp(base=gen2, exponent=randNum, mod=prime)
	print('p:', prime, 
		'\tg:', gen2,
		'\te2:', e2,
		'\td:', randNum)

	with open(pubName, 'w') as pubout, open(priName, 'w') as priout:
		pubout.write('{} {} {}'.format(prime, gen2, e2))
		priout.write('{} {} {}'.format(prime, gen2, randNum))
	return

def getPrime(bits=8):
	''' Generates a prime from using the Miller-
		Rabin function. The prime number is of
		the bit size specified by the 'bits' var
	'''
	prime: int = getrandbits(bits)
	while not is_prime(n=prime, num_of_randos=rands):
		prime = getrandbits(bits)
	return prime

def generator(k=8):
	''' expects some value k that is a bit size.
		This function inversely creates a prime
		from a hardcoded generator 2 rather than
		the other way.
	'''
	prime: int = 0 # not prime and fails Miller-Rabin fast
	while not is_prime(n=prime, num_of_randos=rands):
		qrime: int = 0		# reset q
		# number below is hard coded to allow for (gen mod p = 2)
		while qrime%12 != 5:
			qrime = getPrime(bits=(k-1))
		prime = 2*qrime + 1			# if isPrime then ensures strength
	return prime


# Encryption related functions -------------------------------------------------------
def encrypt(e1, e2, prime, plaintext):
	''' Description
		here
	'''
	ciphers: list = [''] * 2
	randomNum = random.randint(a=0, b=(prime-1))
	ciphers[0] = fast_exp(base=e1, exponent=randomNum, mod=prime)
	# Using:
	# ab mod n = [(a mod n)(b mod n)] mod n
	# ciphers[1] = (plaintext * e2**randomNum) % prime
	# becomes...
	factor1 = plaintext % prime
	factor2 = fast_exp(base=e2, exponent=randomNum, mod=prime)
	ciphers[1] = (factor1*factor2) % prime
	return ciphers

	
# Decryption related functions -------------------------------------------------------
def decrypt(ciphers, prikey, prime):
	''' This takes in a dictionary of two cipher integer, c1 and c2, 
		along with a private key int and a prime number.
		
		It uses the shortcut equation in the project spec to recombine 
		c1 and c2 into the original int for the plaintext
	'''
	# Need to do ((c1**(p-1-d) mod p) * (c2 mod p)) mod p
	c1, c2 = int(ciphers['c1']), int(ciphers['c2'])
	prime, prikey = int(prime), int(prikey)
	factor1: int = fast_exp(base=c1, exponent=(prime-1-prikey), mod=prime)
	factor2: int = c2 % prime
	plaintext: int = (factor1*factor2) % prime
	return plaintext
	

# Procedure related functions --------------------------------------------------------
def str_to_int(word):
	''' takes in a string and takes every char from it, converts it to Ascii,
		concats it to the low end of the previous character. The final value
		is an integer.
	'''
	total: int = 0
	for c in word:
		# print(ord(c))
		total = total<<8 ^ ord(c)
		# print(total)
	return total

def int_to_str(num):
	word: str = ''
	mask: int = 0xFF
	while num != 0:
		c = mask & num
		# print('c={}'.format(chr(c)))
		num = num>>8
		word = chr(c) + word
		# print('word='+word+'|')
	return word

def main(args):
	inputfile: str  = args.inputfile
	outputfile: str = args.outputfile
	keyfile: str 	= args.keyfile
	key: bool = args.genkey
	e: bool	  = args.e_flag
	d: bool	  = args.d_flag

	if key:
		gen_key()
	elif e:
		# Reading key from file and plaintext from input file
		with open(keyfile, 'r') as pubin, open(inputfile, 'r') as fin:
			pubkey: list = pubin.read().split()
			plainT: str = fin.read()
		# print('public key data is...')			#DEBUG
		# print('p:', pubkey[0], 					#DEBUG
		# 	'\tg:', pubkey[1],						#DEBUG
		# 	'\te2:', pubkey[2])						#DEBUG
		# print('plain:\n'+ plainT)					#DEBUG
		# chunk plain text into words of size n | is defined at top
		words = [plainT[i : i+wordSize] for i in range(0, len(plainT), wordSize)]
		# print(words)								#DEBUG
		with open(outputfile, 'w') as fout:
			fout.write('') # to erase the output file
		with open(outputfile, 'a') as fout:	
			# Where the actual call for encrypt w/ one word at a time		
			for word in words:
				wordInt = str_to_int(word)
				# print(wordInt)							#DEBUG
				ciphers = encrypt(int(pubkey[1]), int(pubkey[2]), int(pubkey[0]), wordInt)
				# print('c1: {}, c2: {}'.format(ciphers[0],ciphers[1]))
				fout.write('{} {}\n'.format(ciphers[0],ciphers[1]))
	elif d:
		# Reading key from file
		with open(keyfile, 'r') as privin:#, open(inputfile, 'r') as fin:
			prikey: list = privin.read().split()
		# Reading ciphers from input file into a master list
		cipherlist = list()
		ciphers = {'c1' : 0, 'c2' : 0}
		fin = open(inputfile, 'r')
		for line in fin:	
			ciphers['c1'], ciphers['c2'] = line.split()
			cipherlist.append(ciphers.copy())
			# print(ciphers['c1'], ciphers['c2'])			#DEBUG
		# for dic in cipherlist:							#DEBUG
		# 	print(dic)
		# print('p:', prikey[0], 							#DEBUG
		# 		'\tg:', prikey[1],
		# 		'\te2:', prikey[2])
		with open(outputfile, 'w') as fout:
			fout.write('')
		with open(outputfile, 'a') as fout:
			for ciphers in cipherlist:
				# print('c1:{},c2:{}'.format(ciphers['c1'], ciphers['c2']))
				wordInt = decrypt(ciphers=ciphers, prikey=prikey[2], prime=prikey[0])
				# print('pInt:{}'.format(wordInt))
				word = int_to_str(wordInt)
				# print(word+'|')
				fout.write(word)
	else:
		print('ERROR: no options specified')
	
	return


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-e', '--e_flag', action='store_true', help='encrypt input file')
	parser.add_argument('-d', '--d_flag', action='store_true', help='decrypt input file')
	parser.add_argument('-in', '--inputfile', help='specify input file')
	parser.add_argument('-out', '--outputfile', help='specify output file')
	parser.add_argument('-k', '--keyfile', help='specify key file')
	parser.add_argument('-genkey', '--genkey', action='store_true', help='generates keys')
	args = parser.parse_args()
	if (args.e_flag and args.d_flag) or (args.genkey and (args.e_flag or args.d_flag)):
		#give error
		print('ERROR: conflicting flags active')
		exit()
	main(args)
	exit()
