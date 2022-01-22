def run():
    f = open("economy.txt", "r")
    o = open("economy_p.txt", "a")
    for line in f.readlines():
        t = line.lower()
        o.write(t)
    f.close()
    o.close()


if __name__ == '__main__':
    run()