from gensim.models.doc2vec import Doc2Vec
from nltk import word_tokenize

d2v = Doc2Vec.load("d2v.model")

string = ""
x=d2v.infer_vector(word_tokenize(string.lower()),steps=50, alpha=0.025)
print(x)

y = d2v.docvecs.most_similar([x])
print(y)