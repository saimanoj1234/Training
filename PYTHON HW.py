#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Func to find max of 3 numbers


firstnumber = int(input(" enter the first number"))
secondnumber= int(input(" enter the second number"))
thirdnumber= int(input(" enter the third number"))
def long():
    if  firstnumber>secondnumber and firstnumber>thirdnumber:
        l=firstnumber
    elif secondnumber>firstnumber and secondnumber>thirdnumber:
        l= secondnumber
    else :
        l= thirdnumber
    print("longest number:", l)

long()


# In[16]:


#Sum of all numbers in list

def sum(num):
    tot=0
    for i in num:
        tot = tot+ i
    return tot
print(sum((2,3,4,5)))


# In[18]:


#Mul of all numbers in list
def mul(num):
    tot=1
    for i in num:
        tot = tot * i
    return tot
print(mul((2,3,4,5)))


# In[19]:


#Rev of a string
def rev(x):
    return x[::-1]
s = rev("hello")
print(s)


# In[21]:


#Mul arg with any  unknown number
def nmul(x,n):
    return x*n
s = nmul("hello",4)
s1 = nmul("hello",6)
print(s,s1)


# In[26]:


#Even odd using lambda
l=[1,2,3,4,5]
print(l)
even= list(filter(lambda x: x%2==0, l))
print(even)
odd= list(filter(lambda x: x%2!=0, l))
print(odd)


# In[29]:





# In[31]:


#remove duplicates from a list
array=[1,2,3,6,5,6,5,7,8]

output=[]
for ele in array:
    if ele not in output:
        output.append(ele)
print(output)


# In[33]:


#smallest in list
def s_list(list):
    min = list[0]
    for i in list:
        if i < min:
            min = 1
    return min
print(s_list([1,2,3]))


# In[38]:


#largest in list
def l_list(list):
    max = list[0]
    for i in list[1:]:
        if i > max:
            max = i
    return max
print(l_list([1,2,3]))


# In[42]:


# even numbers in list
list1 = [0,9,4,6,8]
 

for num in list1:
    if num % 2 == 0:
        print(num)
  


# In[45]:


#Write a Python program to sort a list of dictionaries using Lambda.
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
after_sort = sorted(models, key = lambda x: x['color'])
print(after_sort)


# In[ ]:




