text = '''
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code 
readability with its use of significant indentation. Its language constructs as well as its object-oriented approach 
aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and 
garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), 
object-oriented and functional programming. It is often described as a "batteries included" language due to its 
comprehensive standard library. Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC 
programming language, and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced 
new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference 
counting). Python 3.0 was released in 2008 and was a major revision of the language that is not completely 
backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.
'''


def sentence_analyzer(text):
    analyzed = {}
    for something in text:
        something = something.lower()
        if something in analyzed:
            analyzed[something] += 1
        else:
            analyzed[something] = 1
    return analyzed


format_1 = sentence_analyzer(text)

for something in format_1:
    print('The character', something, 'is occuring', format_1[something], 'times in the text.')
