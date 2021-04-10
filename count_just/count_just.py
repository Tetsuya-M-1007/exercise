#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


count = 1
while True:
    try:
        word = str(input("Input correct words!:"))
        if count==1 and word=="Where":
            print("茨")
        elif count==2 and word=="are":
            print("城")
        elif count==3 and word=="you?":
            print("県")
        else:
            print(random.randrange(1, 10))
        count+=1
    
    except:
        print("Error!")
        continue
    
    if count>3:
        print("Finish the process!")
        break

