from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
from xml.etree import ElementTree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import seaborn as sns
import os

def getString(path):      # you give me path of .xml file, I'll give you return you text content
	per=ET.parse(path)
	p=per.findall('./body/body.content/block')
	inputString = ""
	for oneper in p:
		for child in oneper:
			inputString = inputString + " " + str(child.text)
	return inputString

def process_text(doc_set):
	texts = []
	tokenizer = RegexpTokenizer(r'\w+')
	en_stop = get_stop_words('en')
	p_stemmer = PorterStemmer()
	for item in doc_set:
		raw = item.lower()
		tokens = tokenizer.tokenize(raw)
		stopped_tokens = [item for item in tokens if not item in en_stop]
		stemmed_tokens = [p_stemmer.stem(item) for item in stopped_tokens]
		texts.append(stemmed_tokens)
	# for i in range(len(texts)):
	# 	print(texts[i])
	# 	print()
	return texts

def create_ldaModel(texts):
	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]
	lda = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word = dictionary, passes=20)
	for topic_id in range(lda.num_topics):
		topk = lda.show_topic(topic_id, 10)
		topk_words = [ w for w, _ in topk ]
		print('{}: {}'.format(topic_id, ' '.join(topk_words)))


def create_wordcloud(texts):
	long_string = ', '.join(str(item) for item in texts)
	wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
	wcloud = wordcloud.generate(long_string)
	plt.figure()
	plt.imshow(wcloud, interpolation="bilinear")
	plt.axis("off")
	plt.show()

def get_doc():
	doc_set = []
	pre_path = "/home/yoki/Github/timeline/query/sports"
	files= os.listdir(pre_path)
	for file in files:
		path = pre_path + "/" + file
		inputString = getString(path)
		doc_set.append(inputString)
	return doc_set

doc_set = get_doc()
texts = process_text(doc_set)
create_ldaModel(texts)
create_wordcloud(doc_set)