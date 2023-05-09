words = set()
with open("all.txt", encoding = 'utf-8', mode = 'r') as f:
    for line in f:
        s = line.strip('\n').strip()
        words.add(s)
with open("all.txt", encoding = 'utf-8', mode = 'w') as f:
    for i in sorted(words):
        f.write(i + '\n')