#!/usr/bin/env python
# coding: utf-8

# In[2]:


personal_dict={"first_name":"Maheen","last_name":"Anwar","age":"19","city":"Karachi"}
for key, value in personal_dict.items():
    print(key+" : "+value)
print("\n add qualification \n")
personal_dict["qualification"]="intermediate"
for key, value in personal_dict.items():
    print(key+" : "+value)
print("\n update qualification \n")
personal_dict["qualification"]="high academic"
for key, value in personal_dict.items():
    print(key+" : "+value)


# In[3]:


cities={
    "Kashmir":{
        "country":"Pakistan",
        "population":12541302,
        "fact":"Kashmir is the most beautiful city of Pakistan. "
    },
    "karachi":{
        "country":"Pakistan",
        "population":15741000,
        "fact":"Karachi is the biggest city of Pakistan"
    },
    "islamabad":{
        "country":"Pakistan",
        "population":1095064,
        "fact":"Islamabad is the Capital of Pakistan"
    }
}
for citykey,cityinfo in cities.items():
    print("\n"+citykey+"\n")
    for city in cityinfo:
        print(city+" : "+str(cityinfo[city]))


# In[4]:


movie='y'
while movie!='n':
    age=int(input("Enter age : "))
    if age>12:
        print("Ticket is 15$")
    elif age>=3:
        print("Ticket is 10$")
    else:
        print("Ticket is free")
    movie=input("do you want to take ticket y/n: ")


# In[6]:


def favorite_book(title):
    print(title)
book_title="My favorite book is Harry Potter."
if(len(book_title)!=0):
    favorite_book(book_title)
else:
    print("Please populate the book title")


# In[8]:


import random
c=0
rNumber=0
while c<3:
    rNumber=int(random.randrange(1,30))
    userNumber=int(input("Enter number between 1 and 30: "))
    c=c+1
    if rNumber>userNumber:
        print("Hidden number is greater\n")
    elif rNumber<userNumber:
        print("Hidden number is Smaller\n")
    else:
        print("Hidden number is equal\n")

