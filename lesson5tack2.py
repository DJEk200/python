num = 0
i = 0
with open('text.txt') as f:
    for lines, line in enumerate(f, 1):
        wordslist = line.split()
        num = len(line.split())
        i += 1
        print(f'В {i} строке количество слов: {num}')
print(lines)