#!/usr/bin/env python
# coding: utf-8

# In[4]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# In[8]:


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('I am the Best xD')


# In[9]:


a=[1,2,3,4,5,6,7,8,9,10,11]
even_no = [num for num in a if num % 2 == 0] 
  
print("Even numbers in the list a: ", even_no) 


# In[30]:


def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  
s = "malayalam"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 


# In[32]:


def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for i in range(2,n):
            if(n % i==0):
                return False
        return True             
print(test_prime(12))


# In[39]:


prices = {
    "banana": 30,
    "apple": 20,
    "orange": 25,
    "pear": 25
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0
for x in prices:
    total = total + prices[x] * stock[x]
    print (total)


# In[ ]:


def boughtITEM():
    cart = []
    while True:                                  
        carts = input("\nEnter an item to add it in your cart: \nor Press [ENTER] to finish: \n")
        if carts == "":
            break
        cart.append(carts)
    item_list = ""
    for item in range(0,len(cart)):
        item_list = item_list + cart[item].title() + "\n"
    print("\nItems you have bought is:\n"+item_list)

boughtITEM()

