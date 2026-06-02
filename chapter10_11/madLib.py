from pathlib import Path
import re

# Read the text file
path = Path.cwd() / 'madLibs.txt'
with path.open('r', encoding='UTF-8') as f:
    text = f.read()
print(text+'\n\n')

# Find all patterns to replace
matches = re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB', text)

# Ask the user to replace each placeholder
for word in matches:
    if word == 'ADJECTIVE':
        replacement = input('Enter an adjective: ')
    elif word == 'NOUN':
        replacement = input('Enter an noun: ')
    elif word == 'ADVERB':
        replacement = input('Enter an adverb: ')
    elif word == 'VERB':
        replacement = input('Enter an verb: ')

    # Replace only first matches
    text = re.sub(word, replacement, text, count=1)

# Show final text and optionally save it
print('\n--- Mad Lib ---\n')
print(text)

# Save all new changes to existing file
with path.open('w', encoding='UTF-8') as f:
    f.write(text)







