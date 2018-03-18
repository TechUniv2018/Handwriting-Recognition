from enchant.checker import SpellChecker
import enchant
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

s = SpellChecker("en_US")
print ('Enter sentence')
text = input()
s.set_text(text)
correctedInput = s.get_text()
for err in s:
    bestratio = 0
    suggestedWord = ''
    dictionary = enchant.DictWithPWL("en-US","customableDictionary.txt")
    suggestion = dictionary.suggest(err.word)
    for suggest in suggestion:
        ratio = similar(err.word, suggest)
        if ratio > bestratio:
            suggestedWord = suggest
            bestratio = ratio
    correctedInput = correctedInput.replace(err.word, suggestedWord)
print(correctedInput)