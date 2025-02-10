# 1 - Solução
# txt = input("type the word you want to check if it is a palindrome:")

# txtInvert = txt[::-1]

# if txt == txtInvert:
#     print("Is a Palindromo")
# else:
#     print("Is not a Palindromo")

# 2 - Solução
palavrainput = "renner"
# comprimento = len(palavrainput)


a = list()
b = list()
for ch in palavrainput:
    a.append(ch)
for ch in reversed(a):
    b.append(ch)

print(a)
print(b)

if a == b:
    print("é faz um palindromo")
else:
    print("não é um palindromo")

