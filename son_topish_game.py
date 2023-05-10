# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:51:23 2023

@author: user
"""
import random
print("son topish o'yin o'ynaymiz")
def son_top(x=10):
   
   print(f" 1 dan {x} gacha bitta son o'ylayman siz topishga harakat qilasiz ")
  
   x=random.randint(1,10)
   f=int(input("qaysi son deb oylaysiz? \n >>>"))
   taxminlar=0
   while True :
       taxminlar+=1
       if x<f:
           f=int(input("kichikroq son kirirting \n >>>"))
       elif x>f:
           f=int(input("kattaroq son kirirting \n >>>"))
          
       else:
           
           print(f" {taxminlar} ta urinishda  topdingiz tabriklayman")
           break
   return taxminlar
def  son_top_pc(x=10):
     print(f" 1 dan {x}  gacha istalgan son o'ylang men topishga harakat qilaman")
     rozilik=input(" o'ynaymizmi? \n >>>")
     a=random.randint(1, 10)
     taxminlar=0
     while rozilik :
         taxminlar+=1
         f=input(f" siz {a} ni o'yladingiz topdimmi? to'gri (T) katta(+) yoki kichik bolsa (-) qoying \n >>>")
         if f=='-':
           
             a=random.randint(1, a-1)
             
             f=input(f" siz {a} ni o'yladingiz topdimmi? to'gri (T) katta(+) yoki kichik bolsa (-) qoying \n >>>")
         elif f=='+':
       
             a=random.randint(a+1, 10)
             
             f=input(f" siz {a} ni o'yladingiz topdimmi? to'gri (T) katta(+) yoki kichik bolsa (-) qoying \n >>>")
         else:
             break
     print(f" men {taxminlar} ta urinish da topdim")

     return taxminlar
def game1(x=10):
    yana =True
    while yana :
        taxmin_user=son_top(x)
        taxmin_pc=son_top_pc(x)
        if taxmin_pc>taxmin_user:
            print("siz yutdingiz !")
        elif taxmin_pc<taxmin_user:
            print('men yutdim !')
        else:
            print("durrang !")
        yana=int(input(" yana o'ynaymizmi ? ha(1)/ yo'q(0) \n >>>"))
print(game1(10))