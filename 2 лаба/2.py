import re

d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}

def s(n, step):
    n = list(n)
    start = 0 if step == 2 else 2
    for i in range(start, len(n)-1, step):
        n[i], n[i+1] = n[i+1], n[i]
    return ''.join(n)

def p(t):
    if not re.match(r'^[1-9]\d{5,}$', t) or int(t) % 2 == 0:
        return None
    c = t
    v = set()
    while True:
        if '000' in c:
            break
        if c in v:
            break
        v.add(c)
        c = s(c, 2)
    return s(c, 4)

def main():
    with open('1.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    lexemes = re.split(r'\s+', text.strip())
    results = []
    for lexeme in lexemes:
        if lexeme:
            res = p(lexeme)
            if res:
                results.append(res)
    if results:
        if len(results) > 1:
            print(' '.join(results[:-1]), end=' ')
        print(' '.join(d[ch] for ch in results[-1]))

if __name__ == "__main__":
    main()
