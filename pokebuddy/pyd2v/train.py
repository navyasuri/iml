# import spacy
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk import word_tokenize

fp = open('desc.csv')
numbers = []
descriptions = []
names = []

# Create a list of nums and descriptions

for line in fp:
    line = line.strip().split(",")
    num = line[0]
    numbers.append(num)
    name = line[1]
    names.append(name)
    desc = ",".join(line[2:])
    descs = [elem.split(":")[1] for elem in desc.split("^")]
    # print(num, name, desc, end='\n')
    description = "".join(descs)
    # print(description)
    descriptions.append(description)

tag_data = [TaggedDocument(words=word_tokenize(desc.lower()), tags=[num]) for num, desc in zip(numbers, descriptions)]

# Declare training constants
EPOCHS = 100
SIZE = 50
ALPHA = 0.025
DM = 0 # If 1, word order matters, if 0 doesnt matter (ie bag of words)

d2v = Doc2Vec(vector_size=SIZE, alpha=ALPHA, dm=DM, min_alpha=0.00025, min_count=1)
d2v.build_vocab(tag_data)

for epoch in range(EPOCHS):
    d2v.train(tag_data, total_examples=d2v.corpus_count, epochs=d2v.iter)
    print("Iteration", epoch)
    d2v.alpha-=0.0002
    d2v.min_alpha = d2v.alpha

d2v.save("d2v.model")
print("DONE")