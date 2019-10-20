import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')

def dataProcessing(string):     # you give me string, I give you processed words
	stop_words = set(stopwords.words('english'))
	tokens = word_tokenize(string)
	tokens = [w for w in tokens if not w in stop_words]
	porter = PorterStemmer()
	stems = []
	for t in tokens:    
		stems.append(porter.stem(t))
	print(stems)


string = "This Movie Is Horrib, Today is beautiful, tomorrow is also beautiful,I  is you. You is I"
tokens = dataProcessing(string)
