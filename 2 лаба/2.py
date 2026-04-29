import re

with open("1.txt") as f:
    text = f.read()

nums = re.findall(r'\b\d{5,}[13579]\b', text)

r = []
found = False
pair_index = 0
i = 0

while i < len(nums):
    if i + 1 < len(nums):
        x, y = nums[i], nums[i + 1]
        if not found:
            r += [y, x]
            if '000' in x or '000' in y:  # без regex
                found = True
                pair_index = 0
        else:
            if pair_index % 2 == 0:
                r += [x, y]
            else:
                r += [y, x]
            pair_index += 1
        i += 2
    else:
        r.append(nums[i])
        i += 1

for x in r[:-1]:
    print(x, end=' ')

if r:
    d = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три',
        '4': 'четыре', '5': 'пять', '6': 'шесть',
        '7': 'семь', '8': 'восемь', '9': 'восемь'
    }
    print(' '.join(d[c] for c in r[-1]))
