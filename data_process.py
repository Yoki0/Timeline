import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')

def dataProcessing(string):
	stop_words = set(stopwords.words('english'))
	tokens = word_tokenize(string)
	tokens = [w for w in tokens if not w in stop_words]
	porter = PorterStemmer()
	stems = []
	for t in tokens:    
		stems.append(porter.stem(t))
	print(stems)


string = "The quick brown fox jumps over the lazy dog"
dataProcessing(string)
