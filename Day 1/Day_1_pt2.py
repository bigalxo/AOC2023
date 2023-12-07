def main():
    input = open('.\Day 1\input.txt', 'r')
    content = [line.strip() for line in input.readlines()]
    values = 0
    for line in content:
        line = convert(line)
        ints = []
        for char in line:
            try: 
                number = int(char)
                ints.append(number)
            except ValueError:
                continue
        values += int(str(ints[0]) + str(ints[-1]))
    print(values)

def convert(line):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    found = False
    for i in range(len(line)):
        if found == True:
            break
        for word in words:
            if line [i:].startswith(word):
                line = line[:i] + str(words.index(word)) + line[i + len(word):]
                found = True

    found = False
    for i in range(len(line)):
        if found == True:
            break
        i = i*-1
        for word in words:
            if line [i:].startswith(word):
                if i + len(word) == 0:
                    end = ''
                else:
                    end = line[i + len(word):]
                line = line[:i] + str(words.index(word)) + end
                found = True
    return line

if __name__ == '__main__':
    main()