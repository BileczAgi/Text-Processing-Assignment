"""
Original Pylvax Assignment:
Text processing

The following four exercises are about processing text. Download the following text file and save it as sample.txt in a folder: http://paste.ee/r/DPASQ

Part A - Palindromes

Write a program which prints out all palindromes from the text, case insensitive, in alphabetic order. Case insensitive, and exclude all non-alphabetic words and one letter words. 

Part B - Word statistics

How many words are in the text? How many distinct ones? Case insensitive, and exclude all non-alphabetic words.
Print out, in descending order the top 20 most frequent word in the text, including how many times they are present. Case insensitive, and exclude all non-alphabetic words.

Part C - Sentence statistics

Print out the following:

Shortest and longest sentences and how long they are by two different metrics: based on word count and character count.
Group sentences by their endings in to 3 groups: ., ?, !. Print out the average length for each group, based on words counts.
"""

###################################################
#Preparation

# read file

def read_text(filename):
    opened_file=open(filename)
    opened_text=opened_file.read()
    return opened_text

# clean text

#actors names are all caps followed by a ":"" at the beginning of their lines. The function below removes these before further processing the text, because these are not intengrant part of the text, however, the removed names get contained in an actors_names dictionary
def remove_actors_names(text): 
    word_list=text.split()
    n=0
    actors_names={}
    for word in word_list:
        if word.isupper() and word[-1]==":":
            try:
                actors_names[word_list[n]]+=1
            except KeyError:
                actors_names[word_list[n]]=1

            word_list[n]="\n"
        n+=1
    nameless_text=" ".join(word_list)
    return nameless_text
    return actors_names





def clean_text(text):
     text=text.lower()
     cleaned_text=text.replace(",","").replace(";","").replace(":","").replace("-","").replace("(","").replace(")","").replace("?"," ?").replace("!"," !").replace("."," .")
     return cleaned_text


#print clean_text(remove_actors_names(read_text("sample.txt")))
##############################################################
#Part A)
#Write a program which prints out all palindromes from the text, case insensitive, in alphabetic order. Case insensitive, and exclude all non-alphabetic words and one letter words.


##############################################################
#Part B - Word statistics
#How many words are in the text? How many distinct ones? Case insensitive, and exclude all non-alphabetic words.
#Print out, in descending order the top 20 most frequent word in the text, including how many times they are present. Case insensitive, and exclude all non-alphabetic words.

#word counts

def word_counter(text):
    list_of_words=[word for word in text.split() if len(word)>1 & word.isalpha()]
    return list_of_words

#count of distinct words    

def distinct_words(list):
    dict_of_words={}
    for word in list:
        try:
            dict_of_words[word]+=1
        except KeyError:
            dict_of_words[word]=1
    return dict_of_words


print distinct_words(word_counter(clean_text(remove_actors_names(read_text("sample.txt")))))
