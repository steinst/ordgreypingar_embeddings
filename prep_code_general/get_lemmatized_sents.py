"""Writes out a large file containing all sentences in the Icelandic Gigaword Corpus,
lemmatized"""

from rmh_extractor import RmhExtractor
import sys

folder_in = sys.argv[1]

def extract_sents():
    corpus = RmhExtractor(folder=folder_in)
    sent_end = ['.', '?', '!']
    with open(folder_in + '_all_sentences_lemmatized.txt', 'w', encoding='utf-8') as out:
        for word in corpus.extract(forms=True, lemmas=True, pos=True):
            if word.word_form == 'LINU_LYKUR_HER':
                out.write('\n')
            else:
                try:
                    if word.pos.startswith('n') and word.pos.endswith('s'):
                        out.write(word.lemma + ' ')
                    elif word.pos.startswith('p'):
                        pass
                    else:
                        out.write(word.lemma.lower() + ' ')
                except:
                    pass

extract_sents()
