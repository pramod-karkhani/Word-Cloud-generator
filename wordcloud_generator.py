import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud , STOPWORDS

df = pd.read_csv(r"Youtube01-Psy.csv")
comment_words = ' '
stopwords = set(STOPWORDS)
for val in df.values:
    val = str(val)
    tokens   = val.split()
 
for i in range(len(tokens)): 
   tokens[i] = tokens[i].lower() 
          
for words in tokens: 
    comment_words = comment_words + words + ' '
  
  
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()     
