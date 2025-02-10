def stringForList(str):
    newList = list()
    for ch in str:
        newList.append(ch)
    return newList


def mySorted(list):
    tamanho = len(list)
    for i in range(tamanho):
        for j in range(tamanho -1 -i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

def listForString(list):
    ret = ""
    for i in range(len(list)):
        ret = ret + list[i]
    
    return ret


def palindromo(txt):
    a = list()
    b = list()
    for ch in txt:
        a.append(ch)
    for ch in reversed(txt):
        b.append(ch)
    if a.upper() == b.upper():
        print("é faz um palindromo")
    else:
        print("não é um palindromo")




def anagram(str1, str2):
    l = stringForList(str1)
    ll = stringForList(str2)
    ret = mySorted(l)
    rett = mySorted(ll)
    retFinal = listForString(ret)
    retFinall = listForString(rett)
    if retFinal.upper() == retFinall.upper():
        print(str1 + " " + str2 +" ::::: As Strings são Anagramas!")
    else:
        print(str1 + " " + str2 +" ::::: NÃO São Anagramas!")


def anagramDescomplicado(str1,str2):
    ret = sorted(str1)
    rett = sorted(str2)
    ret = "".join(ret)
    rett = "".join(rett)
    if ret.upper() == rett.upper():
        print(str1 + " " + str2 +" ::: São Anagramas!")
    else:
        print(str1 + " " + str2 +" NÃO São Anagramas!")

