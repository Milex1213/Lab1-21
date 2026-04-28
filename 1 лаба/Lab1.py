with open("1.txt") as f:
    a = [x for x in f.read().split() if len(x) > 5 and int(x) % 2 == 1]

r=[]
found=False
pair_index=0
i=0

while i<len(a):
    if i+1<len(a):
        x,y=a[i],a[i+1]
        if not found:
            r+=[y,x]
        else:
            if pair_index%2==0:
                r+=[y,x]
            else:
                r+=[x,y]
            pair_index+=1
        if not found and ('000' in x or '000' in y):
            found=True
        i+=2
    else:
        r.append(a[i])
        i+=1

for x in r[:-1]:
    print(x,end=' ')

if r:
    d={'0':'ноль','1':'один','2':'два','3':'три','4':'четыре',
       '5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
    print(' '.join(d[c] for c in r[-1]))
