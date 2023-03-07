#!/usr/bin/env python
# coding: utf-8

# In[2]:

pip install pyperclip


# In[8]:


from glob import glob
from os.path import isdir
pathdir = "C:/Users/user/Desktop/memo"


# In[23]:


s = glob(f"{pathdir}/*")
pathDir= sorted(s)[-1]


# In[26]:


File = open(f"{pathDir}", "r",  encoding='UTF8')
text = File.readlines()
loadCode = text[5]
File.close()


# In[30]:


import re
regex = re.compile(r'"(.+)"')
matchobj = regex.search(loadCode)
SaveCode = matchobj.group()


# In[31]:


code = SaveCode.replace('"',"").split()


# In[32]:


import pyperclip
pyperclip.copy(code[1])


# In[ ]:




