def reverse_vowels(s):
    import re
    vow = ('a','e','i','o','u', 'A','E','I','O','U')
    vowels = []
    new_L = []
    lst1 = list(s)
    for i in lst1:
        if i in vow:
            vowels.append(i)
            new_L.append('-_')
        if re.match(r'[\D]', i) and i not in vow:
            new_L.append(i)
    rev_vow = list(reversed(vowels))
    fin_chg = []
    for j in new_L:
        if re.match(r'[\D]', j) and j!='-_':
            fin_chg.append(j)
        if j=='-_':
            first_char = rev_vow.pop(0) 
            fin_chg.append(first_char)
    return ''.join(fin_chg)


print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Hello"))
print(reverse_vowels("Bears walking through yellow stone national park"))