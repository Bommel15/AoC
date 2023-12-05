# ADVENT OF CODE DAY 1

# Given an input with digits in the string make a new integer consisting of the first and last digits (if given 1 digit, it is the first AND last)

import re
import sys

input = open("Day1-Data.txt","r").read()

# Getting data
split = str(input).lower().split("\n")

# Init
matches = []
total = 0
position = 0
lookup_dict = {
    "one": 1,
    "two": 2,
    "three":3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine":9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0
}

# Constants
keys = list(lookup_dict.keys())
idxs = list(range(1000))

# Parse rows
for row in split:
    # Filter out special chars
    # row = ''.join(e for e in row if e.isalnum())

    key_idxs = dict.fromkeys(idxs) # Init the dict
    # Find keys
    for key in keys:
        if re.search(fr"{key}",row):
            key_idx = row.index(key)
            key_idxs[key_idx] = key

        key_idxs = {k: v for k, v in key_idxs.items() if v is not None} # Trim the None items
        key_idxs = dict(sorted(key_idxs.items()))
    
    min_row_idx = min(key_idxs.keys())
    max_row_idx = max(key_idxs.keys())

    min_value = key_idxs[min_row_idx]
    max_value = key_idxs[max_row_idx]
    
    min_value = lookup_dict[min_value]
    max_value = lookup_dict[max_value]
    
    value = min_value*10 + max_value
    total = total + value

print(total)
    