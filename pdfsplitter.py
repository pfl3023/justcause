#!/usr/bin/env python
# coding: utf-8

# In[3]:


import PyPDF2
import re
import pandas as pd
import numpy as np
import pandas.io.sql as sqlio
import os
from PyPDF2 import PdfReader, PdfWriter


# In[6]:


object = PyPDF2.PdfReader(r"C:\Users\prish\Downloads\IIMB Case Prep Book.pdf") # input file location

NumPages = len(object.pages)


# In[7]:


print(NumPages)


# In[8]:


regex = r'\s*P\s*r\s*o\s*f\s*i\s*t\s*a\s*b\s*i\s*l\s*i\s*t\s*y\s*'
String = regex


# In[11]:


my_lis = []
for i in range(0, NumPages):
    PageObj = object.pages[i] 
    Text = PageObj.extract_text() 
    print(Text)
    print()
    print("----------------------------------")
    print()
    ResSearch = re.search(String, Text)
    if ResSearch != None:
        my_lis.append(i)
print(my_lis)


# In[20]:


output = PyPDF2.PdfWriter()
for i in my_lis:
    output.add_page(object.pages[i])
    if i == my_lis[-1]:
        outputStream = open(r"C:\Users\prish\Downloads\IIMB Case Prep Book.pdf".format(i), "wb")# output file location
        output.write(outputStream)
        outputStream.close()


# In[ ]:





# In[ ]:




