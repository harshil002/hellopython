
def run(path):
    finaldict= {}
    file = open(path)
    pos = open("positive-words.txt")
    neg = open("negative-words.txt")
    posList, negList = [],[]
    for words in pos:
        posList.append(words.strip('\n'))
    for words in neg:
        negList.append(words.strip('\n'))
    for line in file:
        flag = 0
        line = line.lower().strip()
        for negWords in negList:
            if " "+negWords+" " in " "+line+" ":
                flag = 1
                break
        if flag == 1:
            continue
        for posWords in posList:
            if " "+posWords+" " in " "+line+" ":
                finaldict.setdefault(posWords, 0)
                finaldict[posWords] += 1
    file.close()
    pos.close()
    neg.close()
    return finaldict


if __name__ == "__main__":
    finaldict=run('textfile')
    print(finaldict)