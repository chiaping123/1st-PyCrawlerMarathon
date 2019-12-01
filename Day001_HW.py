#!/usr/bin/env python
# coding: utf-8

# # 資料來源與檔案存取
# 
# * 資料來源與取得
# * 開放資料
# * 資料儲存格式
# * Python 存取檔案

# ## 利用 Python 下載檔案

# In[22]:


from urllib.request import urlretrieve

# urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./1.txt")
urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./data/Homework.txt")


# In[23]:


import os, sys

# 打開文件（預設位置會是跟 .ipynb 程式相同的目錄）
dirs = os.listdir( './data/' )

# 顯示所有文件
for file in dirs:
    print(file)


# ## 利用 Python 存取檔案

# In[24]:


with open("./data/Homework.txt", "w") as fh:
    f = fh.write("Hello World")
    print(f)
    
with open("./data/Homework.txt", "r") as fh:
    f = fh.read()
    print(f)


# ## 作業目標
# 
# * 1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
# * 2.（實作）完成一個程式，需滿足下列需求：
#     * 下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
#     * 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
#     * 將「Hello World」字串覆寫到 Homework.txt 檔案
#     * 檢查 Homework.txt 檔案字數是否符合 Hello World 字數
# 

# In[ ]:





# In[ ]:




