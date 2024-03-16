"""codewars link: https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


#solution
def pig_it(text):
    new_text = ''
    for word in text.split(' '):
        if word.isalpha():
            new_text += word[1:] + word[0] + 'ay '
        else:
            new_text += word
    return new_text.strip()