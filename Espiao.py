#Escreva uma funcao que receba uma lista de interiros e retorne True
#se contem um 007 em ordem, mesmo que nao continuo.

def espiao (num):
 for i in range(0,len(num)):
       if num[i] == 0 and num[i+1] == 0 and num[i+2] == 7:
         return True



print(espiao([0,1,0,0,0,7]))