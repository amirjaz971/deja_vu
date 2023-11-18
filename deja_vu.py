letters=input("enter the letters: ")
a=[]
b=[]
count=0
if letters.isalpha():
    for i in letters:
        a.append(i)

    for i in a:
        if i in b:
            print("deja vu!")
            b.append(i)
            break
        elif i not in b:
            b.append(i)
            count+=1

    
    if count==len(b):
        print("unique!")    










else:
    print("only letters!")