def convert_data():
    f = open('paper.txt', 'r')
    k = open('keyword.txt', 'r')
    o = open('paper_p.txt', 'a')
    keywords = k.readlines()
    k.close()
    # for i in range(9):
    #     ll = f.readline()
    # ll = f.readline()
    # ll.replace(',', ' ')
    # temp = ll.split()
    # new = []
    # for i in temp:
    #     if (i+'\n') in keywords:
    #         new.append(i)
    # print(new)
    # o.write(' '.join(map(str, new)))
    # o.write('\n')
    for line in f.readlines():
        line.replace(',', ' ')
        temp = line.split()
        new = []
        for i in temp:
            if (i+'\n') in keywords:
                new.append(i)
        if len(new) > 0:
            o.write(' '.join(map(str, new)))
            o.write('\n')
    o.close()
    f.close()


if __name__ == '__main__':
    convert_data()