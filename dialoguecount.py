#import libraries

import urllib.request as urllib2
from bs4 import BeautifulSoup
import requests
import re
import nltk
import matplotlib.pyplot as plt
import io
import urllib
import requests
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

url = requests.get("https://www.imsdb.com/scripts/Avengers,-The-(2012).html").text
soup = BeautifulSoup(website_url, "lxml")
text = soup.pre
#Retrieve script from IMSDB 

list1 = [b.string for b in text.findAll('b')]
#Finds all bolded text (usually character name)
list2 = [t.replace("\r\n", "") for t in list1]
#Removes the \r\n
list3 = [t.strip(' ') for t in list2] 
#Removes white space
list4 = [t.replace("\xad", "") for t in list3]

names = ["TONY", "THOR", "STEVE", "NATASHA", "BANNER", "BLACK WIDOW", "IRON MAN", "CAPTAIN AMERICA", "JARVIS", "HAWKEYE", "CLINT BARTON", "NICK FURY", "SELVIG", 
       "AGENT MARIA HILL", "LOKI", "AGENT PHIL COULSON", "HULK", "IRON MAN (V.O.)", "HAWKEYE (V.O.)", "BLACK WIDOW (V.O.)", 
        "CAPTAIN AMERICA (V.O.)", "STEVE (V.O.)", "NICK FURY (V.O.)", "LOKI (V.O.)", "TONY (V.O.)", ]
#Define the names of the main characters including voice over appearances

new_list = [item for item in list4 if item in names]
#Goes through the list and compares to the list of names of main characters to print
print(new_list)

new_list[:] = [s.replace('NICK FURY (V.O.)', 'NICK FURY') for s in new_list]
new_list[:] = [s.replace('LOKI (V.O.)', 'LOKI') for s in new_list]
new_list[:] = [s.replace('BLACK WIDOW (V.O.)', 'NATASHA') for s in new_list]
new_list[:] = [s.replace('BLACK WIDOW', 'NATASHA') for s in new_list]
new_list[:] = [s.replace('TONY (V.O.)', 'TONY') for s in new_list]
new_list[:] = [s.replace('IRON MAN', 'TONY') for s in new_list]
new_list[:] = [s.replace('IRON MAN (V.O.)', 'TONY') for s in new_list]
new_list[:] = [s.replace('CAPTAIN AMERICA', 'STEVE') for s in new_list]
new_list[:] = [s.replace('HAWKEYE (V.O.)', 'CLINT BARTON') for s in new_list]
new_list[:] = [s.replace('HAWKEYE', 'CLINT BARTON') for s in new_list]
new_list[:] = [s.replace('HULK', 'BANNER') for s in new_list]
new_list[:] = [s.replace('STEVE (V.O.)', 'STEVE') for s in new_list]
#Voices overs and aliases should be placed into the main characters name in order to accuratley count their lines

my_dict = {i:new_list.count(i) for i in new_list}
print(my_dictpd.DataFrame(list(d.items())))

df = pd.DataFrame(list(my_dict.items()))
df.columns = ['Character','Dialogue Count']
df = df.drop([10], axis=0)
df
#Create a dataframe and rename columns

ax = df.plot.bar(x='Character', y='Dialogue Count', rot=0)
plt.ylabel('Dialogue Count') #Y-axis label
plt.title('Which main character in \nThe Avengers (2012) speaks the most?') #Title
ax.get_legend().remove() #Removes legend, irrelevant in this situation
plt.xticks(rotation=90) #Vertical x-axis 
plt.show()
