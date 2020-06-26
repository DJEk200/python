subj = {}
clock_len = []
with open('test_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        s = line.split()
        num = ''
        for char in line:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    clock_len.append(int(num))
                    num = ''
    clock = sum(clock_len)
    print(f'Учебнов время: {clock} часов')

