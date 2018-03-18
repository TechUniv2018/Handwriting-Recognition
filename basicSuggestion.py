import language_check
# import grammar_check

langTool = language_check.LanguageTool('en-US')
# grammarTool = grammar_check.LanguageTool('en-US')
print ('Enter sentence')
text = input()#'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
# matches = grammarTool.check(text)
# print (matches)
matches = langTool.check(text)
print (language_check.correct(text, matches))

