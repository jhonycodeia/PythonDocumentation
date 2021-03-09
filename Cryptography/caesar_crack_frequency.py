import matplotlib.pylab as plt

#these are the etters we are interested in when dealing with frequency-analysis
LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#the method to do frequency analysis: we just count the occurences of the given characters
def frequency_analysis(cipher_text):

	#the text we analyise
	cipher_text = cipher_text.upper()

	#we use a dictionary to store the letter-frequency pair
	letter_frequency = {}

	#initialize the dictionary (of course with 0 frequencies)
	for letter in LETTERS:
		letter_frequency[letter] = 0
		
	#let's consider the text we want to analyse	
	for letter in cipher_text:
		#we keep incrementing the occurence of the given letter
		if letter in LETTERS:
			letter_frequency[letter] += 1
			
	return letter_frequency

#plot the histogram of the letter-frequency pairs
def plot_distribution(letter_frequency):
	centers = range(len(LETTERS))
	plt.bar(centers, letter_frequency.values(), align='center', tick_label=letter_frequency.keys())
	plt.xlim([0,len(LETTERS)-1])
	plt.show()
	
def caesar_crack(cipher_text):
	
	letter_frequency = frequency_analysis(cipher_text)
	print(letter_frequency)
	plot_distribution(letter_frequency)
	
	
if __name__ == "__main__":
	
	cipher_text = 'QBDREQIDMWDFEPECWDLSPGCIVCDMDEQDJVSQDFYHETIWXCDLYRKEVBCDMDEQDUYEPMJMIHDEWDEDTLBWMGMWXDERHDPEXIVDSRCDEXDXLIDQSQIRXDMDEQD SVOMRKDEWDEDWMQYPEXMSRDIRKMRIIVDEXDEDQYPXMREXMSREPDGSQTERBCDMDLEZIDFIIRDMRXIVIWXIHDMRDEPKSVMXLQWDERHDHEXEDWXVYGXYVIWDERHDMXWDMQTPIQIRXEXMSRWDIWTIGMEPPBDMRDNEZEDWMRGIDYRMZIVWMXBCDPEXIVDSRDMDKSXDEGUYEMRXIHD MXLDQEGLMRIDPIEVRMRKDXIGLRMUYIWCDEVXMJMGMEPDMRXIPPMKIRGICDRYQIVMGEPDQIXLSHWDERHDVIGMTIWDWYGLDEWDWSPZMRKDHMJJIVIRXMEPDIUYEXMSRWCDPMRIEVDEPKIFVECDMRXIVTSPEXMSRDERHDIAXVETSPEXMSRCDXLIWIDXLMRKWDQEBDTVSZIDXSDFIDZIVBDZIVBDMQTSVXERXDMRDWIZIVEPDJMIPHWCDWSJX EVIDIRKMRIIVMRKCDVIWIEVGLDERHDHIZIPSTQIRXDSVDMRZIWXQIRXDFEROMRKCDMDLEZIDEDWTIGMEPDEHHMGXMSRDXSDUYERXMXEXMZIDQSHIPWDWYGLDEWDXLIDFPEGOCWGLSPIWDQSHIPCDSVDXLIDQIVXSRCQSHIPC'
	caesar_crack(cipher_text)
	
	