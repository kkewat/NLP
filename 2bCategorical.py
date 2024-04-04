import nltk
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
mycat = CategorizedPlaintextCorpusReader(
        'D:\\NLP\\2024NLP1', r'sample.*\.txt',  cat_pattern = r'.*?_(one|two).*')
print ("Categorize : ", mycat.categories())

print ("\nOne : ", mycat.fileids(categories =['one']))

print ("\nTwo : ", mycat.fileids(categories =['two']))

mycat.words(categories='one')


print ('Avg Word Len\tAvg Sentence Len\t No of Times Each Word Appears On Avg\t FileName')

for fileid in mycat.fileids():
    num_chars = len(mycat.raw(fileid))
    num_words = len(mycat.words(fileid))
    num_sents = len(mycat.sents(fileid))
    num_vocab = len(set([w.lower() for w in mycat.words(fileid)])) 
    print (int(num_chars/num_words),'\t\t\t', int(num_words/num_sents), '\t\t\t',  int(num_words/num_vocab), '\t\t\t\t', fileid)
