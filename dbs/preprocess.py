import nltk
from nltk import sent_tokenize
from nltk.tokenize import MWETokenizer
# text = '''Hello everyone . welcome to the Great Learning .
# Mr. Smith("He isn't an instructor") and Johann S. Baech
# (He is  an instructor.) are waiting for you . They'll join you soon.
# Hope you enjoy a lot'''
# tokenizer = MWETokenizer([['Great', 'Learning'], ['Johann', 'S.', 'Baech'], ['a', 'lot']],separator='_')
# for t in sent_tokenize(text):
#     x = tokenizer.tokenize(t.split())
#     print(x)

def token_word():
    k = open('keyword.txt', 'r')
    c = open('courpus_p.txt', 'r')
    re = open('paper.txt', 'a')
    merge = []
    # print(k.readline().replace('\n', '').split('_'))
    for key in k.readlines():
        merge.append(key.replace('\n', '').split('_'))
    for line in c.readlines():
        tokenize = MWETokenizer(merge, separator='_')
        for tt in sent_tokenize(line):
            temp = tokenize.tokenize(tt.split())
            re.write(' '.join(map(str, temp)))
            re.write('\n')
    k.close()
    c.close()
    re.close()


if __name__ == '__main__':
    token_word()