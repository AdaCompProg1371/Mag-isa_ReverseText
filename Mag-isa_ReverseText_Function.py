# The Codes for Making a Reversed Word Sentence
# Function and Codes for Reversing Words in a Sentence
import numbers

def the_function(x):
    return x[::-1]

sample_txt = the_function(input("Texts Here:"))

if sample_txt == numbers:
    print("Error Reported! Enter text only.")
else:
    print("Output:" , sample_txt)