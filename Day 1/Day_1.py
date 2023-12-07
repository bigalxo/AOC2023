input = open('.\Day 1\input.txt', 'r')
content = [line.strip() for line in input.readlines()]

values = 0
for line in content:
    ints = []
    for char in line:
        try: 
            number = int(char)
            ints.append(number)
        except ValueError:
            continue
    values += int(str(ints[0]) + str(ints[-1]))
print(values)

