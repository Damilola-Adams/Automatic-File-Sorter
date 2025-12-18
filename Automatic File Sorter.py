#!/usr/bin/env python
# coding: utf-8

# In[1]:mmmmmmmm


import os, shutil


# In[25]:


path = r"C:/Users/HP PAVILION/Documents/DS/"


# In[26]:


file_name = os.listdir(path)


# In[29]:


folder_names = ['csv files', 'ipynb files', 'pdf files', 'text files']

for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        #print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if '.csv' in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    if '.ipynb' in file and not os.path.exists(path + "ipynb files/" + file):
        shutil.move(path + file, path + "ipynb files/" + file)
    if '.pdf' in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    if '.txt' in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)


# In[ ]:




