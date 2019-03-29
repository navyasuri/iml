from gensim.models.doc2vec import Doc2Vec
from nltk import word_tokenize
import os

d2v = Doc2Vec.load("d2v_names.model")

string = "super hot fire pokemon. burns everything to ash."
x=d2v.infer_vector(word_tokenize(string.lower()),steps=50, alpha=0.025)
print(x)

y = d2v.docvecs.most_similar([x])
for i in y: print(i)

# def classify(doc):
#     totalpath = os.path.join(os.getcwd(), "d2v.model")
#     d2v = Doc2Vec.load(totalpath)
#     vector = d2v.infer_vector(word_tokenize(doc.lower()),steps=50, alpha=0.025)
#     similars = d2v.docvecs.most_similar([vector])

#     return similars[0][0]