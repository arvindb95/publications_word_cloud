import re
import nltk
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Convert your papers to text using the attached shell script (requires pdftotext to be installed)

paper_text_unclean = open("papers.txt","r").read()

tagged_text = nltk.tag.pos_tag(paper_text_unclean.split())

final_words = [word for word,tag in tagged_text if tag != 'NNP' and tag != 'NNPS' and tag != 'IN' and tag != 'PRP' and tag != 'WDT' and tag != 'WP' and tag != 'WRB' and tag != 'VB' and tag != 'VBG' and tag != 'VBD' and tag != 'VBN' and tag != 'VBP' and tag != 'VBZ']

final_text = ""

for word in final_words:
    final_text = final_text + word + " "

circle_mask = np.array(Image.open("circle_stencil.png"))

stopwords = set(STOPWORDS)
stopwords.update({"2004dk","Table","Section"})

wc = WordCloud(min_word_length=4,stopwords=stopwords,mask=circle_mask,background_color="#28353C",colormap="Wistia",scale=20,repeat=False).generate(final_text)    

wc.to_file("paper_wordcloud.png")
