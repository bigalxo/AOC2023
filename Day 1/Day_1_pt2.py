def main():
    input = open('.\Day 1\input.txt', 'r')
    content = [line.strip() for line in input.readlines()]
    content = ['twone5']
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

def convert(line): # This function scans the line twice, forwards and backwards, and makes up to two conversions 
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    found = False
    for i in range(len(line)): #scanning the string left to right 
        if found == True: 
            break
        for word in words:
            if line [i:].startswith(word):
                line = line[:i] + str(words.index(word)) + line[i + len(word):]
                found = True

    found = False
    for i in range(len(line)): #scanning the string right to left
        if found == True:
            break
        i = i*-1
        for word in words:
            if line [i:].startswith(word):
                if i + len(word) == 0: #prevents the entire string being rewritten if the end position lands on 0 
                    end = ''
                else:
                    end = line[i + len(word):]
                line = line[:i] + str(words.index(word)) + end
                found = True
    return line

if __name__ == '__main__':
    main()