# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x=int(input("inter an integer:"))
st=0
if x==0:
  print("the cube root of 0 is 0")
else:
  while True:
    st+=1

    if st**3==abs(x):
        if x>0:
          print("the cube root of " + str(x) + " is " + str(st))
          break
        if x<0:
            st=- st
            print("the cube root of " + str(x) + " is " + str(st))
            break
    elif st**3>abs(x):
        print("the cube root of "+str(x)+" is not perfect cupe")
        break
    
