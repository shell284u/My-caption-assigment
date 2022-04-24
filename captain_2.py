#!/usr/bin/env python
# coding: utf-8

# In[9]:




numbs = int(input("How many nums? "))


n1, n2 = 0, 1
count = 0


if numbs <= 0:
   print("enter a positve number and try again.")

elif numbs == 1:
   print("Fibonacci numbers upto",numbs,"=")
   print(n1)

else:
   print("Fibonacci numbers:")
   while count < numbs:
       print(n1)
       nn = n1 + n2
    
       n1 = n2
       n2 = nn
       count += 1


# 
