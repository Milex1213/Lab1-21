d={'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
def s(n,st):
 n=list(n)
 for i in range(0 if st==2 else 2,len(n)-1,st):n[i],n[i+1]=n[i+1],n[i]
 return ''.join(n)
def p(t):
 if not(t.isdigit() and int(t)%2 and len(t)>5):return
 c=t;v=set()
 while '000' not in c:
  if c in v:break
  v.add(c);c=s(c,2)
 return s(c,4)
b='';r=[]
for ch in open('1.txt').read():
 b+=ch
 if ch==' ':
  z=p(b.strip())
  if z:r.append(z)
  b=''
if b.strip():z=p(b.strip())
if z and z not in r:r.append(z)
if r:
 [print(i,end=' ') for i in r[:-1]]
 print(' '.join(d[j] for j in r[-1]))
