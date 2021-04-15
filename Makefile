encrypt: 
	python3 wsu-pub-crypt.py -e -in ptext.txt -k pubkey.txt -out ctext.txt
decrypt:
	python3 wsu-pub-crypt.py -d -in ctext.txt -k prikey.txt -out dtext.txt
genkey:
	python3 wsu-pub-crypt.py -genkey
eKabir:
	python3 wsu-pub-crypt.py -e -in ptext.txt -k test_pubkey.txt -out ctext.txt
dKabir:
	python3 wsu-pub-crypt.py -d -in ctext.txt -k test_prikey.txt -out dtext.txt
diff:
	sdiff -s dtext.txt ptext.txt
eArt:
	python3 wsu-pub-crypt.py -e -in art.txt -k pubkey.txt -out ctext.txt
dArt:
	python3 wsu-pub-crypt.py -d -in ctext.txt -k prikey.txt -out dtext.txt