#!/usr/bin/python

__author__ = 'messen01'

import sys

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

corpus = corpora.MmCorpus('corpora/hackday.mm')

num_topics = int(sys.argv[1])

model = models.LsiModel.load("models/lsi_" + str(num_topics) + "topics")

index = similarities.MatrixSimilarity(model[corpus])

index.save("indexes/" + str(num_topics) + "topics_lsi.index")

