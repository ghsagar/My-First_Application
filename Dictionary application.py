print("Hello guys! We are making dictionary application.")
import json
import difflib
from difflib import get_close_matches
information=json.load(open("data.json"))
word=input("please enter a word to know its meaning:")
def know_meaning(w):
    w=w.lower()
    if w in information:
        return information[w]
    elif w.title() in information:
        return information[w.title()]
    elif w.upper()in information:
        return information[w.upper()]
    elif len(get_close_matches(w,information.keys()))>0:
        print(f"do you mean {get_close_matches(w, information.keys())[0]} instead")
        take=input("Y for yes and N for No:")
        if take=="Y" or take=="y":
            return information[get_close_matches(w,information.keys())[0]]
        else:
            return "wrong input, check again!"

    else:
        return "it has no meaning, please check once"

print(know_meaning(word))




