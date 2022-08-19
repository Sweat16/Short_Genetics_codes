#%%
"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
is the string sc formed by reversing the symbols of s

, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s

of length at most 1000 bp.

Return: The reverse complement sc
of s.
"""
#%%
DNA = input("enter your DNA string: ")
DNA_reversed = list(DNA)[::-1]

for i in range(len(DNA)) :
    if DNA_reversed[i] == "A" :
        DNA_reversed[i] = "T"
    elif DNA_reversed[i] == "T" :
        DNA_reversed[i] = "A"
    elif DNA_reversed[i] == "C" :
        DNA_reversed[i] = "G"
    elif DNA_reversed[i] == "G" :
        DNA_reversed[i] = "C"

DNA_reversed_transcriped = ""

for i in DNA_reversed:
    DNA_reversed_transcriped += i   