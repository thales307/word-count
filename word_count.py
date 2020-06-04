from collections import Counter
import re

def count_words(sentence):
    counting = re.sub(r"\t|\n|:|!|@|#|\$|%|\^|&|,|\.| '|' |'$| \"|\" |_|''", ' ', sentence.lower())    
    return Counter(counting.split())