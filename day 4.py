#day 4 list and data structures
#program to print the sum of even palindromes in a range and also list
'''def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0
n,m=map(int,input("enter the number").split(" "))
l1,l2=[],[]
for i in range(n,m+1):
    flag=palindrome(i)
    if flag==1:
        l1.append(i)
    if i%2==0:
        if flag==1:
            l2.append(i)
print(l1)
print(sum(l2))'''
#python to sum of given matrix
'''r,c=int(input("enter row")),int(input("enter column"))
l=[]
l1=[]
for i in range(r):
    l.append(list(map(int,input("enter elements").split(" "))))
#print(l)
summ=0
for j in l:
    l1.append(sum(l[j]))
print(sum(l1))
    print(j)
    summ+=sum(j)
print(summ)'''

#product of matrix
'''r,c=int(input("enter row")),int(input("enter column"))
l=[]
l1=[]
for i in range(r):
    l.append(list(map(int,input("enter elements").split(" "))))
pro=1
for j in l:
    print(j)
    for i in j:
        pro*=i
print(pro)'''
# write a program sum of max and min elements using tuple
'''
min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        sum+=j
        if j > max:
            max=j
        if j < min:
            min=j
print("average",sum/(r*c))
print("sum of min and max",max+min)'''
#programto print sum of elements last column of matrix
'''r,c=int(input("enter row")),int(input("enter column"))
l=[]
l1=[]
sum=0
for i in range(r):
     l.append(tuple(map(int,input("enter elements").split(" "))))
for i in l:
     sum+=i[c-1]
print(sum)'''
#program to add two matrices
'''r,c=int(input("enter row")),int(input("enter column"))
l=[]
for i in range(r):
     l3[i]=[0]*r
for i in range(r):
     l.append(tuple(map(int,input("enter elements").split(" "))))
print(tuple(l))
r,c=int(input("enter row")),int(input("enter column"))
l1=[]
for i in range(r):
     l1.append(tuple(map(int,input("enter elements").split(" "))))
print(tuple(l1))
l2=[0]*r
for i in range(r):
     for j in range(c):
          l2[i][j]=l1[i][j]+l[i][j]
for i in l3:
     print(i)'''
#sets
#s=set()
a=set([1,2,3,4,5])
b=set([5,6,7,8,9])
a1={1,2,3,4}
b1={2,3}
'''print(a|b)
print(a.intersection(b))
print(a&b)
print(b.intersection_update(a))
print(b)
print(a.intersection_update(a))
print(a)'''
'''print(a.difference(b))
print(a-b)
a.difference_update(b)
print(a)
print(a.symmetric_difference(b))
print(a^b)
a.symmetric_difference_update(b)
print(a)'''
'''print(a1.isdisjoint(b1))
print(a1.issuperset(b1))
print(b1.issuperset(a1))
print(a1.issubset(b1))
print(b1.issubset(a1))
print(sorted(a))'''
# set problems
#to check whether string is panagram
'''import string
n=input("enter the name")
n=n.lower()
s1=string.ascii_lowercase
if set(n) == set(s1):
    print("panagram")
else:
    print("not panagram")'''
#python to count of vowels in the word and list of vowels in sentence usingfunction
'''n=input("enter name").split()
count=0
s=""
l=[]
for i in n:
    if i == "aeiouAEIOU":
        l.append(i)
        count=count+1
    print("count:",count)
    print("vowels",l)'''
#sir code
def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i.lower() in "aeiouAEIOU":
            vc+=1
            s1+=i
    print("vowel count:",vc)
    print(list(set(s1)))
l=input().split()
for i in l:
    counting(i)

            




    

     
     






        
        
        
        

    
    


    






            
        
        
        
        
