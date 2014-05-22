#!/usr/bin/python

__author__ = 'messen01'

import logging
import sys
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = corpora.Dictionary.load('corpora/hackday.dict')
corpus = corpora.MmCorpus('corpora/hackday.mm')
print(corpus)

num_topics = int(sys.argv[1])

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]

model = models.LsiModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=num_topics)

topics = model.print_topics(num_topics)

model_file = "models/lsi_" + str(num_topics) + "topics"

model.save(model_file)



