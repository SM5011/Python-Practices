"""
def count(itm):
    c = c_v = 0
    for i in range(itm.index('='),len(itm)):
        if 'a'<=itm[i]<='z' or 'A'<=itm[i]<='Z' or '0'<=itm[i]<='9':
            c+=1
        if itm[i].lower() in ['a','e','i','o','u']:
            c_v+=1
    return c,c_v
lst = ['Name=Shikha','Father name=Muzam','Mother name=Haua','Phone Number=01971700130']
tc=tv=0
for i in lst :
    c,v= count(i)
    tc+=c
    tv+=v
print(tc)
print(tv)
"""
def count(itm):
    c_alpha = 0
    c_vowel = 0
    split_str = itm.split('=')  # Splitting the string into key-value pair
    value = split_str[1]        # Taking the value part
    for char in value:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            c_alpha += 1
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                c_vowel += 1
    return c_alpha, c_vowel

lst = ['Name=Shikha', 'Father name=Muzam', 'Mother name=Haua', 'Phone Number=01971700130']
total_alpha_count = 0
total_vowel_count = 0
for item in lst:
    alpha_count, vowel_count = count(item)
    total_alpha_count += alpha_count
    total_vowel_count += vowel_count

print("Total alphabetic characters:", total_alpha_count)
print("Total vowels:", total_vowel_count)
