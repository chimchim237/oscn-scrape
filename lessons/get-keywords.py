#get-keywords.py

import obo

test = 'this test sentence has eight words in it'
ngrams = obo.getNGrams(test.split(), 5)

print(obo.nGramsToKWICDict(ngrams))