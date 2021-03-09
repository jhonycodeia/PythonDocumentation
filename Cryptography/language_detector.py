import matplotlib.pyplot as plt
	
#we store the english words in a list (maybe a dictionary would be better)	
ENGLISH_WORDS = []

#load the english words
def get_data():
	
	#let's load all the english words from a .txt file
	dictionary = open("english_words.txt","r")

	#initialize the ENGLISH_WORDS list with the words present in the file
	#every word is in a distinct line so that why we have to split('\n')
	for word in dictionary.read().split('\n'):
		ENGLISH_WORDS.append(word)
		
	dictionary.close()
	
#count the number of english words in a given text
def count_words(text):

	#upper case letters are needed
	text = text.upper()
	#transform the text into a list of words (split by spaces)
	words = text.split(' ')
	#matches counts the number of english words in the text
	matches = 0

	#consider all the words in the text and check whether the given word is english or not
	for word in words:
		if word in ENGLISH_WORDS:
			matches = matches + 1
			
	return matches

#decides whether a given text is english or not	
def is_text_english(text):
		
	#number of nglish words in a given text
	matches = count_words(text)

	#you can define your own classification algorithm
	#in this case the assumption: if 80% of the words in the text are english words then
	#it is an english text
	if (float(matches) / len(text.split('\n'))) * 100 >= 80:
		return True
		
	#not an english text
	return False
	
if __name__ == "__main__":
	
	get_data()
	
	text = 'My name is Balazs Holczer from Budapest, Hungary. I am working as a software engineer at the moment'
	print(is_text_english(text))