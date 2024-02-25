#day 5
#write a program to take dictionary as input and print key and values of dictionary
'''n=int(input("enter a integer"))
n1=dict()
for i in range(n):
    n1[i]=input("enter items")
print(n1)
print(n1.keys())
print(n1.values())'''
'''n=int(input("enter no of items:"))
d={}
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    d[key]=value
print(d)
for i in d:
    print("key:",i," ","value: ",d[i])
   #using f function
    print(f"key:{i} value:{d[i]}")
    print("key:{} value:{}".format(i,d[i]))
for i in d.keys():
    print(i)
for i in d.values():
    print(i)'''
#phone book search
'''n=int(input("enter the number"))
d={}
d1={}
for i in range(n):
    key=input("enter a name")
    value=int(input("enter a number"))
    d[key]=value
print(d)
for j in range(1):
    key1=input("enter a name")
    value1=int(input("enter a number"))
    d1[key1]=value1
print(d1)
for i in d:
    if i == d1:
        print(i)
        break
    else:
        print("not found")'''
#
'''n=int(input("enter number"))
d={}
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
m=int(input("enter no of search items"))
for i in range(m):
    s=input()
    if s in d:
        print(s,d[s])
    else:
        print("not found")'''
#ip address
'''n,m=map(int,input("enter the number").split(" "))
d={}
d1={}'''
#d1={"google":"8.8.8.8","codeforces":"212.193.33.27","server":"138.197.64.57"}
'''for i in range(n):
    key=input("enter a name")
    value=input("enter a ip")
    d[key]=value
print(d)
for i in range(m):
    keys=input("enter a name")
    values=input("enter a ip")
    d1[keys]=values
print(d1)
for i in range(m):
    if d1 in d:
        print(d1)
    else:
        print("not found")'''
#code
'''d={}
n,m=map(int,input().split(" "))
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
for i in range(m):
    k1,v1=map(str,input().split())
    for i in d:
        if d[i] == v1[:-1]:
            print(f"{k1} {v1} #{i}")'''
#to check vanagram
'''n=input("enter a string")
k=input("enter a string")
n1=list(n)
n2=list(k)
if len(n)==len(k) and n1.sort() == n2.sort():
    print("vanagram")
else:
    print("not vanagram")'''
#
'''s1,s2=map(str,input().split())
print(sorted(list(s1)))
print(sorted(list(s2)))
if len(s1) == len(s2):
      if sorted(list(s1)) == sorted(list(s2)):
          print(True)
      else:
          print(False)
else:
          print(False)'''
#using dictionaries
'''d={}
for i in range(2):
    k,v=map(str,input().split())
    d[k]=v
print(d)
l=list(d.values())
if len(l[0]) == len(l[1]):
    if sorted(list(l[0])) == sorted(list(l[1])):
        print(True)
    else:
        print(False)
else:
        print(False)'''
#matrix
'''n=int(input("enter the difference number"))
l=int(input("enter the elements length"))
l1=[]
for i in range(l):
    l1.append(int(input("enter number")))
print(l1)
for j in range(1,len(l1)):
    if l1[j]-l1[j-1] == n:
        print(True)
        break
else:
    print(False)'''
#find first repeating character
'''s=input()
for 


'''
#composite and prime
'''def dict(n,d):
    for i in range(n):
        key=1
        value="composite"
        d[key]=value
    print(d)

n=int(input("enter a num"))
sum=0
d={}
for i in range(2,n):
    if n%i==0:
        sum+=1
    if sum == 2:
        dict(n,d)'''
# prime and composite
'''def isprime(m):
    for i in range(2,m):
        if m%i==0:
            return "composite"
    else:
        return "prime"
n=int(input())
d={}
for i in range(n):
    k=i+1
    v=isprime(i+1)
    d[k]=v
print(d)'''

#python to students database nested dictionary
'''n=int(input("enter no of students"))
m=int(input("enter subjects"))
d1={}
d={}
for i in range(n):
    key=int(input("enter a roll"))
    for j in range(m):
            keys=input("enter a sub:")
            value=int(input("enter a marks"))
            d[keys]=value
    values=d
    d1[key]=d
print(d1)'''
#
'''n=int(input("enter no of students"))
m=int(input("enter no of subjects"))
d={}
for i in range(n):
    k=input("enter roll no:")
    v={}
    for j in range(m):
        sub=input("enter subject name:")
        marks=int(input('enter marks:'))
        v[sub]=marks
    d[k]=v
for i in d:
    print(i,"=",d[i])
    l=list(d[i].values())
    print(f"{i} : {sum(l)/m}")'''
#OOPS OBJECT ORIENTED PROGRAMMING
#CLASS AND OBJECT
#ENCAPSULATION code1
#METHOD HAVING SAME CLASS NAME IS CONSTRUCTOR BUT NOT IN PYTHON
#SELF CALLS NAME VARIABLE,REPRESENTS THE LOCALITY OF CLASS
#WE SHOULD NOT CALL CONSTRUCTOR IT EXECUTES WHEN OBJ CREATED
'''class student:
    def __init__(self,name,age,sec):
        self.name=name
        self.age=age
        self.sec=sec
        print(name,age,sec)
obj=student("sampath","22","ece-2")
obj1=student("ven","37","ece-b")
obj2=student("sur","32","ece-b")'''
#
'''class eceb:
    def __init__(self,marks,subject):
        self.marks=marks
        self.subject=subject
    def sec1(self,name,age):
        self.name=name
        self.age=age
        #calling constructor values in method
        print(name,age,self.subject,self.marks)
    def sec2(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
        print(name,roll,age,self.subject,self.marks)
obj=eceb("99","maths")
obj.sec1("venkat","22")
obj.sec2("suri","410","23")'''
#
'''class college:
    def __init__(self,name):
        self.name=name
        self.ece1()
        self.ece2()
    def ece1(self):
        print("this is ece-1",self.name)
    def ece2(self):
        print("this is ece-1",self.name)
s=input()
obj=college(s)'''
#
class college:
    def __init__(self):
        print(self.sec1())
        print(self.sec2())
    def sec1(self):
        return "method1"
    def sec2(self):
        return "method2"
obj=college()

        



        
    
            


      
        














