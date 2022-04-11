"""Writes out a large file containing all sentences in the Icelandic Gigaword Corpus,
nonlemmatized"""

from rmh_extractor import RmhExtractor
from string import punctuation
import sys

folder_in = sys.argv[1]

def extract_sents():
    corpus = RmhExtractor(folder=folder_in)
    with open(folder_in + '_all_sentences.txt', 'w', encoding='utf-8') as out:
        for word in corpus.extract(forms=True, lemmas=True, pos=True):
            if word.word_form == 'LINU_LYKUR_HER':
                out.write('\n')
            else:
                try:
                    if word.pos.startswith('n') and word.pos.endswith('s'):
                        out.write(word.word_form + ' ')
                    elif word.pos.startswith('p'):
                        pass
                    else:
                        out.write(word.word_form.lower() + ' ')
                except:
                    pass

extract_sents()
