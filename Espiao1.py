#Escreva uma funcao que receba uma lista de interiros e retorne True
#se contem um 007 em ordem, mesmo que nao continuo.

def espiao(num):
   for i in range(len(num)):
     if num[i] == 0:
         for j in range(i+1, len(num)):
             if num[j] == 0:
                 for h in range(j+1, len(num)):
                     if num[h] == 7:
                       return True

print(espiao([1,2,0,2,0,7]))