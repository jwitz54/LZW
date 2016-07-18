import string

def compress ( uncompressed ):
	
	#Initialize Dictionary
	letters = string.ascii_uppercase
	dictionary = {}
	dictionaryLength = 0

	i = 0
	for letter in letters:
		dictionary[letter] = i
		i = i + 1
	dictionaryLength = i
	#print(dictionary[0])

	#Compress the file
	curr = ''
	next = ''
	compressed = ''
	
	i = 0
	dictIdx = dictionaryLength
	while uncompressed[i] != '#':
		next = uncompressed[i]
		if dictionary.has_key(curr + next):
			curr = curr + next
		else:
			dictionary[curr + next] = dictIdx
			if uncompressed[i + 1] == '#':
				compressed = compressed + str(dictionary[curr]) + ' #'
			else:
				compressed = compressed + str(dictionary[curr]) + ' '
			curr = next
			dictIdx = dictIdx + 1
		i = i + 1
	return compressed

def decompress( compressed ):
	#Initialize Dictionary
	letters = string.ascii_uppercase
	dictionary = {}
	dictionaryLength = 0

	i = 0
	for letter in letters:
		dictionary[i] = letter
		i = i + 1
	dictionaryLength = i

	#Decompress
	uncompressed = ''
	currcode = ''
	prevcode = ''

	codes = compressed.split(' ')

	i = 0
	dictIdx = dictionaryLength
	while codes != '#':
		currcode = codes[i]
		translation = dictionary[currcode]
		uncompressed = uncompressed + translation
		
	return

compress( 'WHOWHOWHATWHOWHATWHATWHOHOW#' )