This assumes you have kandlcontentpipeline checked out in a folder next to this one

You will need numpy, scipy and gensim installed, ideally in a virtualenv

In the examples below, 50 is the number of features, 300 is the document index

python loaddocs.py
python processdocs_lsi.py 50 
python setupsim_lsi.py 50 

python do_query_lsi.py 50 300

python do_query_lsi.py 50 500

Outputs the document being checked, and the top three similarity references
