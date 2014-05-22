#!/usr/bin/python

__author__ = 'messen01'

import sys
import logging
import json
import os

from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

num_topics = int(sys.argv[1])

model = models.LsiModel.load("models/lsi_" + str(num_topics) + "topics")

corpus = corpora.MmCorpus('corpora/hackday.mm')
index = similarities.MatrixSimilarity.load("indexes/" + str(num_topics) + "topics_lsi.index")

doc_to_test = int(sys.argv[2])

sims = index[model[corpus[doc_to_test]]]

sims = sorted(enumerate(sims), key=lambda item: -item[1])

content_dir = "../kandlcontentpipeline/content/processed/"

json_files = map((lambda file: json.load(open(content_dir + file))), os.listdir(content_dir))

file_urls = map((lambda json: json['url']), json_files)
file_bodies = map((lambda json: json['body']), json_files)

print "Doc to test"
print "-------------------------------------------------------------------------"
print file_urls[doc_to_test]
print file_bodies[doc_to_test]
print "-------------------------------------------------------------------------"
print "Top three results"
print "-------------------------------------------------------------------------"
print file_urls[sims[1][0]]
print file_bodies[sims[1][0]]
print "-------------------------------------------------------------------------"
print file_urls[sims[2][0]]
print file_bodies[sims[2][0]]
print "-------------------------------------------------------------------------"
print file_urls[sims[3][0]]
print file_bodies[sims[3][0]]
print "-------------------------------------------------------------------------"
