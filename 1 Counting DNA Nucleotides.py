DNA = input("enter your DNA string: ")
count_A = 0
count_T = 0
count_C = 0
count_G = 0

for i in range(len(DNA)):  
    if DNA[i] == "A" :
        count_A += 1
    elif DNA[i] == "T" :
        count_T += 1
    elif DNA[i] == "C" :
        count_C += 1
    elif DNA[i] == "G" :
        count_G += 1
        
    