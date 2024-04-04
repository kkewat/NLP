#study of tagged corpora – tagged words
import nltk

nltk.corpus.brown.tagged_words()
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news',  tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.keys()

#Tagged Sentences
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
print(brown_sents)
print(brown_tagged_sents)
