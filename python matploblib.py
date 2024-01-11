#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary
data = {
    'Name': ['Grace', 'Olive', 'Charlie', 'Uriel', 'Eva'],
    'Age': [25, 30, 35, 22, 28],
    'Salary': [50000, 60000, 75000, 48000, 70000]
}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Plotting using Matplotlib
plt.figure(figsize=(8, 6))
plt.bar(df['Name'], df['Salary'], color='blue')
plt.title('Salary Distribution')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()


# In[ ]:




