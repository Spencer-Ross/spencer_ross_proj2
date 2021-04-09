name: 	Spencer Ross
email:	spencer.ross@wsu.edu

Files included:
	fastExp.py 		- Fast exponentiation function
	Miller-Rabin.py - check if number is prime using Miller-Rabin test
	README.txt 				<--- you are here

These scripts are both fully independant and can run on their own. The
Miller-Rabin script imports the fast exponentiation script. 


fastExp.py:
	Implements fast exponentiation (successive squaring) modulo n. 

 		-a <int>, -b <int> and -n <int>, for computing a^b mod n
To run fastExp.py:
	#for computing a^b mod n
	$ python3 fastExp.py -a <int> -b <int> -n <int> 

	for example:
		$ python3 fastExp.py -a 10 -b 5 -n 100009 


Miller-Rabin.py:
	Implements the Miller–Rabin	algorithm for a user specified n. The 
	program allows the user two choices: (1) specify a possible witness 
	'a' to test using the Witness procedure or (2) specify a number 's' 
	of random witnesses for the Miller–Rabin test to check. 

To run Miller-Rabin.py:
	$ python3 Miller-Rabin.py -n <int> -a <int> OR -s <int>

	for example:
		$ python3 Miller–Rabin.py -s 100 -n 29389543
		or
		$ python3 python3 Miller–Rabin.py -a 3 -n 293




Spencer Ross
