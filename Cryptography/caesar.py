#we need the alphabet because we convert letters into numerical values to be able to use
#mathematical operations (note we encrypt the spaces as well)
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

#caesar encryption algorithm
def caesar_encrypt(plain_text):

	#the encrypted message
	cipher_text = ''
	#we make the algorithm case insensitive
	plain_text = plain_text.upper()
	
	#consider all the letters in the plain_text
	for c in plain_text:
		#find the numerical representation (index) associated with that character in the alphabet
		index = ALPHABET.find(c)
		#caesar encryption is just a simple shift of characters according to the key
		#use modular arithmetic to transform the values within the range [0,num_of_letters_in_alphabet]
		index = (index+KEY)%len(ALPHABET)
		#keep appending the encrypted character to the cipher_text
		cipher_text = cipher_text + ALPHABET[index]
		
	return cipher_text
	
#caesar decryption algorithm: basically the same but using -KEY in this case
def caesar_decrypt(cipher_text):

	plain_text = ''
	
	for c in cipher_text:
		index = ALPHABET.find(c)
		index = (index-KEY)%len(ALPHABET)
		plain_text = plain_text + ALPHABET[index]
		
	return plain_text
	
if __name__ == "__main__":
	
	encrypted = caesar_encrypt('This is an example')
	print(encrypted)
	encrypted = 'QBDREQIDMWDFEPECWDLSPGCIVCDMDEQDJVSQDFYHETIWXCDLYRKEVBCDMDEQDUYEPMJMIHDEWDEDTLBWMGMWXDERHDPEXIVDSRCDEXDXLIDQSQIRXDMDEQD SVOMRKDEWDEDWMQYPEXMSRDIRKMRIIVDEXDEDQYPXMREXMSREPDGSQTERBCDMDLEZIDFIIRDMRXIVIWXIHDMRDEPKSVMXLQWDERHDHEXEDWXVYGXYVIWDERHDMXWDMQTPIQIRXEXMSRWDIWTIGMEPPBDMRDNEZEDWMRGIDYRMZIVWMXBCDPEXIVDSRDMDKSXDEGUYEMRXIHD MXLDQEGLMRIDPIEVRMRKDXIGLRMUYIWCDEVXMJMGMEPDMRXIPPMKIRGICDRYQIVMGEPDQIXLSHWDERHDVIGMTIWDWYGLDEWDWSPZMRKDHMJJIVIRXMEPDIUYEXMSRWCDPMRIEVDEPKIFVECDMRXIVTSPEXMSRDERHDIAXVETSPEXMSRCDXLIWIDXLMRKWDQEBDTVSZIDXSDFIDZIVBDZIVBDMQTSVXERXDMRDWIZIVEPDJMIPHWCDWSJX EVIDIRKMRIIVMRKCDVIWIEVGLDERHDHIZIPSTQIRXDSVDMRZIWXQIRXDFEROMRKCDMDLEZIDEDWTIGMEPDEHHMGXMSRDXSDUYERXMXEXMZIDQSHIPWDWYGLDEWDXLIDFPEGOCWGLSPIWDQSHIPCDSVDXLIDQIVXSRCQSHIPC'
	encrypted= 'WHATYHMWHYL'
	decrypted = caesar_decrypt(encrypted)
	print(decrypted)
	