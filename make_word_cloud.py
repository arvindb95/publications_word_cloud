import re
import nltk
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Save all pdf papers in a directory named papers
# The pdf's will be converted to a single text file by the accompanying shell
# script

paper_text_unclean = open("papers/all_papers.text","r").read()

# Use NLTK packge to remove nouns, pronouns and other trivial words from the
# text

tagged_text = nltk.tag.pos_tag(paper_text_unclean.split())

final_words = [word for word,tag in tagged_text if tag != 'NNP' and tag != 'NNPS' and tag != 'IN' and tag != 'PRP' and tag != 'WDT' and tag != 'WP' and tag != 'WRB' and tag != 'VB' and tag != 'VBG' and tag != 'VBD' and tag != 'VBN' and tag != 'VBP' and tag != 'VBZ']

final_text = ""

for word in final_words:
    final_text = final_text + word + " "

# Use the attached circular stencil or a stensil of your choice

circle_mask = np.array(Image.open("circle_stencil.png"))

# Add more stopwords for the wordcloud package to remove
#
stopwords = set(STOPWORDS)
stopwords.update({"2004dk","Table","Section"})

wc = WordCloud(min_word_length=4,stopwords=stopwords,mask=circle_mask,background_color="#28353C",colormap="Wistia",scale=20,repeat=False).generate(final_text)    

wc.to_file("paper_wordcloud.png")
