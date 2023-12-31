import re

def substitute_digits(input_string):
    word_to_digit = { 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                     'nine': '9' }
    for word, digit in word_to_digit.items():
        input_string = input_string.replace(word, f'{word}{digit}{word}')
    return input_string


with open('input', 'r') as f:
    x = f.read().strip().split('\n')
    x = [substitute_digits(k) for k in x]
    x = [re.sub(r'\D', '', k) for k in x]
    print(sum([int(f'{k[0]}{k[-1]}') for k in x]))
