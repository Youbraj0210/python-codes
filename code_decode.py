# coding 

# if word is of less than 3 :- just reverse the string 
# eg ---- of --> fo

# if min 3 to ... 
# eg---> youbraj
# ----- abcoubrajyxyz


# decoding 
#  if word is less than d3 then again reverse it 
# if not then remove the 3 from start and end and remove the last and append it to start


import string
import random


def code(word):
    wlist = word.split(" ")
    new_sentence=[]
    for stuff in wlist:
        if(len(stuff)<3):
            rev = stuff[::-1]
            new_sentence.append(rev)
            # print(rev)  
        else:
            first = stuff[:-len(stuff)+1]
            newstuff = stuff[1:]+first
            start = ''.join(random.choices(string.ascii_lowercase, k=3))
            end = ''.join(random.choices(string.ascii_lowercase, k=3))
            newword = start + newstuff + end
            new_sentence.append(newword)
            # print(newword)
    str = " "
    str = str.join(new_sentence)
    return str 
    

def decode(word):
    wlist = word.split(" ")
    new_sentence = []
    for stuff in wlist:
        if(len(stuff)<3):
            rev = stuff[::-1]
            new_sentence.append(rev)
            # print(rev)
        else:
            newstuff = stuff[3:-3]
            new_word = newstuff[len(newstuff)-1]+newstuff[:-1]
            new_sentence.append(new_word)
            # print(new_word)

    str=" "
    str = str.join(new_sentence)
    return str

word = str(input("enter the sentence you want to code :"))

coded_word = code(word)
decoded_word = decode(coded_word)
print(f"the coded message is {coded_word}")
print(f"the decoded message is {decoded_word}")


