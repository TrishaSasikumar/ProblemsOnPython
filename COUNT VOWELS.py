str = input("ENTER ANY WORD")
vowels="aeiouAEIOU"
count=0
for i in str:
    if i in vowels:
        count = count+1
print(count)
