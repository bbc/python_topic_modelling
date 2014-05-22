This assumes you have kandlcontentpipeline checked out in a folder next to this one

You will need numpy, scipy and gensim installed, ideally in a virtualenv

python loaddocs.py
python processdocs_lsi.py 50 # number of features to end up with
python setupsim_lsi.py 50   # number of features to end up with

python do_query_lsi.py 50 300 # number of features / document index to find correspondences with


Outputs the document being checked, and the top three similarity references
