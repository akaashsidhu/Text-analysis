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
from nltk.tokenize import word_tokenize 
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

loki = []

for line in text.find_all('b', text=re.compile("\s+LOKI\s+")):
        loki.append(line.next_sibling.strip())

#print(len(loki))
#There are 80 lines for loki but they need cleaning up

loki[0] = "You have heart."
loki[5] = "Freedom. Freedom is life's great lie."
loki[7] = "Well, then..."
loki[11] = "You don't have the Tesseract yet."
loki[15] = "Kneel before me."
loki[16] = "I said. KNEEL!!!"
loki[17] = "Is not this simpler? Is this not your natural state? It's the unspoken truth of humanity, that you crave subjugation. The bright lure of freedom diminishes your life's joy in a mad scramble for power, for identity. You were made to be ruled. In the end, you will always kneel."
loki[19] = "Look to your elder, people. Let him be an example."
loki[20] = "The soldier. A man out of time."
loki[22] = "I'm not overly fond of what follows."
loki[23] = "I missed you too."
loki[24] = "Oh, you should thank me. With the Bifrost gone how much dark energy did the Allfather have to muster to conjure you here? Your precious Earth."
loki[26] = "Your father. He did tell you my true parentage, did he not?"
loki[27] = "I remember a shadow. Living in the shade of your greatness. I remember you tossing me into an abyss. I was and should be king!"
loki[28] = "And you're doing a marvelous job with that. The humans slaughter each other in droves, while you idly threat. I mean to rule them. And why should I not?"
loki[32] = "I don't have it. You need the cube to bring me home, but I've sent it off I know not where."
loki[34] = "It's an impressive cage. Not built, I think, for me."
loki[35] = "Oh, I've heard."
loki[38] = "There's not many people that can sneak up on me."
loki[42] = "Tell me."
loki[44] = "Ah, no. But I like this. Your world in the balance, and you bargain for one man?"
loki[47] = "You lie and kill in the service of liars and killers."
loki[48] = "You pretend to be separate, to have your own code, something that makes up for the horrors. But they are a part of you, and they will never go away!"
loki[49] = "I won't touch Barton. Not until I make him kill you! Slowly. Intimately. In every way he knows you fear! And when he'll wake just long enough to see his good work, and when he screams, I'll split his skull! This is my bargain, you mewling quim!"
loki[50] = "No, you brought the monster."
loki[51] = "What?"
loki[53] = "The humans think us immortal. Should we test that?"
loki[54] = "Am I?"
loki[68] = "How will your friends have time for me,when they're so busy fighting you?"
loki[70] = "You will all fall before me."
loki[72] = "It's too late. It's too late to stop it."
loki[73] = "Sentiment."
loki[75] = "ENOUGH! YOU ARE, ALL OF YOU ARE BENEATH ME! I AM A GOD, YOU DULL CREATURE, AND I WILL NOT BE BULLIED..."

loki = list(filter(None, loki))

loki = [t.replace("\r\n", "") for t in loki]
l = [t.replace("           ", " ") for t in loki] 
loki = [t.replace("          ", " ") for t in l]
print(loki)

stop_words=set(["a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are", "aren", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "couldn", "couldn't", "d", "did", "didn", "didn't", "do", "does", "doesn", "doesn't", "doing", "don", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn", "hadn't", "has", "hasn", "hasn't", "have", "haven", "haven't", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "isn", "isn't", "it", "it's", "its", "itself", "just", "ll", "m", "ma", "me", "mightn", "mightn't", "more", "most", "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now", "o", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "re", "s", "same", "shan", "shan't", "she", "she's", "should", "should've", "shouldn", "shouldn't", "so", "some", "such", "t", "than", "that", "that'll", "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "ve", "very", "was", "wasn", "wasn't", "we", "were", "weren", "weren't", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "won", "won't", "wouldn", "wouldn't", "y", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "could", "he'd", "he'll", "he's", "here's", "how's", "i'd", "i'll", "i'm", "i've", "let's", "ought", "she'd", "she'll", "that's", "there's", "they'd", "they'll", "they're", "they've", "we'd", "we'll", "we're", "we've", "what's", "when's", "where's", "who's", "why's", "would", "able", "abst", "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj", "affected", "affecting", "affects", "afterwards", "ah", "almost", "alone", "along", "already", "also", "although", "always", "among", "amongst", "announce", "another", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "apparently", "approximately", "arent", "arise", "around", "aside", "ask", "asking", "auth", "available", "away", "awfully", "b", "back", "became", "become", "becomes", "becoming", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "believe", "beside", "besides", "beyond", "biol", "brief", "briefly", "c", "ca", "came", "cannot", "can't", "cause", "causes", "certain", "certainly", "co", "com", "come", "comes", "contain", "containing", "contains", "couldnt", "date", "different", "done", "downwards", "due", "e", "ed", "edu", "effect", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "especially", "et", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "except", "f", "far", "ff", "fifth", "first", "five", "fix", "followed", "following", "follows", "former", "formerly", "forth", "found", "four", "furthermore", "g", "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "go", "goes", "gone", "got", "gotten", "h", "happens", "hardly", "hed", "hence", "hereafter", "hereby", "herein", "heres", "hereupon", "hes", "hi", "hid", "hither", "home", "howbeit", "however", "hundred", "id", "ie", "im", "immediate", "immediately", "importance", "important", "inc", "indeed", "index", "information", "instead", "invention", "inward", "itd", "it'll", "j", "k", "keep", "keeps", "kept", "kg", "km", "know", "known", "knows", "l", "largely", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "lets", "like", "liked", "likely", "line", "little", "'ll", "look", "looking", "looks", "ltd", "made", "mainly", "make", "makes", "many", "may", "maybe", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "million", "miss", "ml", "moreover", "mostly", "mr", "mrs", "much", "mug", "must", "n", "na", "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "ninety", "nobody", "non", "none", "nonetheless", "noone", "normally", "nos", "noted", "nothing", "nowhere", "obtain", "obtained", "obviously", "often", "oh", "ok", "okay", "old", "omitted", "one", "ones", "onto", "ord", "others", "otherwise", "outside", "overall", "owing", "p", "page", "pages", "part", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly", "potentially", "pp", "predominantly", "present", "previously", "primarily", "probably", "promptly", "proud", "provides", "put", "q", "que", "quickly", "quite", "qv", "r", "ran", "rather", "rd", "readily", "really", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "respectively", "resulted", "resulting", "results", "right", "run", "said", "saw", "say", "saying", "says", "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sent", "seven", "several", "shall", "shed", "shes", "show", "showed", "shown", "showns", "shows", "significant", "significantly", "similar", "similarly", "since", "six", "slightly", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specifically", "specified", "specify", "specifying", "still", "stop", "strongly", "sub", "substantially", "successfully", "sufficiently", "suggest", "sup", "sure", "take", "taken", "taking", "tell", "tends", "th", "thank", "thanks", "thanx", "thats", "that've", "thence", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "thereto", "thereupon", "there've", "theyd", "theyre", "think", "thou", "though", "thoughh", "thousand", "throug", "throughout", "thru", "thus", "til", "tip", "together", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "ts", "twice", "two", "u", "un", "unfortunately", "unless", "unlike", "unlikely", "unto", "upon", "ups", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "v", "value", "various", "'ve", "via", "viz", "vol", "vols", "vs", "w", "want", "wants", "wasnt", "way", "wed", "welcome", "went", "werent", "whatever", "what'll", "whats", "whence", "whenever", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "whim", "whither", "whod", "whoever", "whole", "who'll", "whomever", "whos", "whose", "widely", "willing", "wish", "within", "without", "wont", "words", "world", "wouldnt", "www", "x", "yes", "yet", "youd", "youre", "z", "zero", "a's", "ain't", "allow", "allows", "apart", "appear", "appreciate", "appropriate", "associated", "best", "better", "c'mon", "c's", "cant", "changes", "clearly", "concerning", "consequently", "consider", "considering", "corresponding", "course", "currently", "definitely", "described", "despite", "entirely", "exactly", "example", "going", "greetings", "hello", "help", "hopefully", "ignored", "inasmuch", "indicate", "indicated", "indicates", "inner", "insofar", "it'd", "keep", "keeps", "novel", "presumably", "reasonably", "second", "secondly", "sensible", "serious", "seriously", "sure", "t's", "third", "thorough", "thoroughly", "three", "well", "wonder", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "co", "op", "research-articl", "pagecount", "cit", "ibid", "les", "le", "au", "que", "est", "pas", "vol", "el", "los", "pp", "u201d", "well-b", "http", "volumtype", "par", "0o", "0s", "3a", "3b", "3d", "6b", "6o", "a1", "a2", "a3", "a4", "ab", "ac", "ad", "ae", "af", "ag", "aj", "al", "an", "ao", "ap", "ar", "av", "aw", "ax", "ay", "az", "b1", "b2", "b3", "ba", "bc", "bd", "be", "bi", "bj", "bk", "bl", "bn", "bp", "br", "bs", "bt", "bu", "bx", "c1", "c2", "c3", "cc", "cd", "ce", "cf", "cg", "ch", "ci", "cj", "cl", "cm", "cn", "cp", "cq", "cr", "cs", "ct", "cu", "cv", "cx", "cy", "cz", "d2", "da", "dc", "dd", "de", "df", "di", "dj", "dk", "dl", "do", "dp", "dr", "ds", "dt", "du", "dx", "dy", "e2", "e3", "ea", "ec", "ed", "ee", "ef", "ei", "ej", "el", "em", "en", "eo", "ep", "eq", "er", "es", "et", "eu", "ev", "ex", "ey", "f2", "fa", "fc", "ff", "fi", "fj", "fl", "fn", "fo", "fr", "fs", "ft", "fu", "fy", "ga", "ge", "gi", "gj", "gl", "go", "gr", "gs", "gy", "h2", "h3", "hh", "hi", "hj", "ho", "hr", "hs", "hu", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ic", "ie", "ig", "ih", "ii", "ij", "il", "in", "io", "ip", "iq", "ir", "iv", "ix", "iy", "iz", "jj", "jr", "js", "jt", "ju", "ke", "kg", "kj", "km", "ko", "l2", "la", "lb", "lc", "lf", "lj", "ln", "lo", "lr", "ls", "lt", "m2", "ml", "mn", "mo", "ms", "mt", "mu", "n2", "nc", "nd", "ne", "ng", "ni", "nj", "nl", "nn", "nr", "ns", "nt", "ny", "oa", "ob", "oc", "od", "of", "og", "oi", "oj", "ol", "om", "on", "oo", "oq", "or", "os", "ot", "ou", "ow", "ox", "oz", "p1", "p2", "p3", "pc", "pd", "pe", "pf", "ph", "pi", "pj", "pk", "pl", "pm", "pn", "po", "pq", "pr", "ps", "pt", "pu", "py", "qj", "qu", "r2", "ra", "rc", "rd", "rf", "rh", "ri", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "rv", "ry", "s2", "sa", "sc", "sd", "se", "sf", "si", "sj", "sl", "sm", "sn", "sp", "sq", "sr", "ss", "st", "sy", "sz", "t1", "t2", "t3", "tb", "tc", "td", "te", "tf", "th", "ti", "tj", "tl", "tm", "tn", "tp", "tq", "tr", "ts", "tt", "tv", "tx", "ue", "ui", "uj", "uk", "um", "un", "uo", "ur", "ut", "va", "wa", "vd", "wi", "vj", "vo", "wo", "vq", "vt", "vu", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y2", "yj", "yl", "yr", "ys", "yt", "zi", "zz"])
#These are words that will be filtered out

token = []

for i in range(74):
    token.append(word_tokenize(loki[i]))
#This will tokenize every word in the loki list

filtered_sentence = []

for i in range(74):
    for w in token[i]:
        if w not in stop_words:
            filtered_sentence.append(w)

#print(filtered_sentence)
#This is a filtered sentence without stop words

filtered_sentence = list(filter(None, filtered_sentence))


l = [ x for x in filtered_sentence if "." not in x ]
l = [ x for x in l if "," not in x ]
l = [ x for x in l if "?" not in x ]
l = [ x for x in l if "!" not in x ]
l = [ x for x in l if "I" not in x ]
l = [ x for x in l if "You" not in x ]
l = [ x for x in l if "'ve" not in x ]
l = [ x for x in l if "'s" not in x ]
l = [ x for x in l if "n't" not in x ]
l = [ x for x in l if "YOU" not in x ]
l = [ x for x in l if "ME" not in x ]
l = [ x for x in l if "AM" not in x ]
l = [ x for x in l if "A" not in x ]
l = [ x for x in l if "What" not in x ]
l = [ x for x in l if "'d" not in x ]
l = [ x for x in l if "That" not in x ]
l = [ x for x in l if "There" not in x ]
l = [ x for x in l if "The" not in x ]
l = [ x for x in l if "But" not in x ]
l = [ x for x in l if "Did" not in x ]
l = [ x for x in l if "not" and "NOT" not in x ]
l = [ x for x in l if "THE" not in x ]
l = [ x for x in l if "Can" not in x ]
l = [ x for x in l if "How" not in x ]
l = [ x for x in l if "Not" not in x ]
l = [ x for x in l if "Should" not in x ]
l = [ x for x in l if "BE" not in x ]
l = [ x for x in l if "'m" not in x ]
l = [ x for x in l if "To" not in x ]
l = [ x for x in l if "This" not in x ]
l = [ x for x in l if "Well" not in x ]
l = [ x for x in l if "'re" not in x ]
l = [ x for x in l if "He" not in x ]
l = [ x for x in l if "Let" not in x ]
#Words that weren't filtered out but should be

wordcloud = WordCloud(background_color="white").generate(" ".join(l))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
#This is a basic word cloud

mask = np.array(Image.open(requests.get('http://www.pngmart.com/files/2/Loki-PNG-Transparent-Image.png', stream=True).raw))
#Link to the image for the word cloud
def generate_wordcloud(words, mask):
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', mask=mask).generate(" ".join(l))
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
wc = generate_wordcloud(l, mask)
#This is a wordcloud using a custom image

lc = WordCloud(width = 512, height = 512, background_color='white', mask=mask)
lc.generate(" ".join(l))
plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
plt.imshow(lc)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()

image_colors = ImageColorGenerator(mask)
fig, axes = plt.subplots(1, 3)
axes[0].imshow(lc, interpolation="bilinear")
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
axes[1].imshow(lc.recolor(color_func=image_colors), interpolation="bilinear")
axes[2].imshow(mask, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()
plt.show()
#This shows 3 images, 2 word clouds, 1 with custom colors matching the original image and another with default colors
