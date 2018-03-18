import enchant
dictionary = enchant.DictWithPWL("en-US","customableDictionary.txt")
suggestion = dictionary.suggest('HELLO')
print (suggestion)