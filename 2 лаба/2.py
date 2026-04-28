```python
import re

with open("1.txt") as f:
    text=f.read()

nums=re.findall(r'\d+',text)
a=[x for x in nums if len(x)>5 and int(x)%2==1]

r=[]
f_flag=False
p=0
i=0

while i<len(a):
    if i+1<len(a):
        x,y=a[i],a[i+1]
        if not f_flag or p%2==0:
            r.extend([y,x])
        else:
            r.extend([x,y])
            p+=1
        if re.search(r'000',x) or re.search(r'000',y):
            f_flag=True
        i+=2
    else:
        r.append(a[i])
        i+=1

if r:
    print(' '.join(r[:-1]),end=' ')
    d={'0':'ноль','1':'один','2':'два','3':'три','4':'четыре',
       '5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
    print(' '.join(d[c] for c in r[-1]))
```
