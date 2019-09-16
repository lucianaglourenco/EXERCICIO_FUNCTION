def tem_33(num):
 for i in range(0,len(num)):
       if num[i] == 3 and num[i+1] == 3:
         return True
 return False



print(tem_33([0,1,3,3,3,7]))