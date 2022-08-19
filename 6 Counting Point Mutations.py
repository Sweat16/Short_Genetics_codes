#%%
"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t

. See Figure 2.

Given: Two DNA strings s
and t

of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
.
"""
#%%
DNA_1 = input("enter the first DNA string: ")
DNA_2 = input("enter the second DNA string: ")

count = len(DNA_1)
for i in range(len(DNA_1)):
    if DNA_1[i] == DNA_2[i]:
        count -= 1