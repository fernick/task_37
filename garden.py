# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read 
# at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences 
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities 
# you found that spaCy gave one of the words of your sentences - did you expect this?

#importing needed library
import spacy #This statement should work if you have spaCy installed 

nlp = spacy.load('en_core_web_sm')

#garden sentence
sent_1 = "The old man the boat, Matthew."
sent_2 = "The complex houses married and single soldiers and their families, Bujumbura."
sent_3 = "The horse raced past the barn fell, Mbuye."
sent_4 = "The sour drink from the ocean, Milan."
sent_5 = "We painted the wall with cracks,Nzeyimana."


gardenpathSentences =(sent_1, sent_2,sent_3,sent_4,sent_5)

#Initializing the tokenization process
for sentence in gardenpathSentences:
    print(sentence)
    doc = nlp(sentence)

    #tokenization
    print([token.orth_ for token in doc])

    #entity recognition
    print([(i, i.label_, i.label) for i in doc.ents])

##Comment
'''
SpaCy is quite smart in categorizing cities, name of people.
I even put a name of a person in my local language and Spacy recognized it.
Also I put a name of a village in Burundi and it recognized it. I did not expect it, 
Impressive!!

'''



