import math
import itertools


# Function to count the number of ones in a binary number

def num_one(x):
	z=bin(x)[2:]
	sum=0
	for i in z:
		sum=sum+int(i)
	return sum

#function to check if both arrays are equal 

def areEqual(arr1, arr2):
	x=arr1.copy()
	y=arr2.copy()
	x.sort()
	y.sort()
	if x== y:
		return True
	else:
		return False


#input of variables
nu_var=int(input("Enter the number of variables:"))

#Checking if the number of variables is a non-zero or negative value
while nu_var <= 0:  
   nu_var=int(input("ERROR! please enter a positive value for the number of variables:"))

#input of minterms  
nu_minterm=int(input("Enter the number of minterms:"))

#checking if the number of minterms is a non-zero or negative value or if its a number greater than the maximum allowed for the number of values
zero = 0
smaller = 0
while not(zero) and not(smaller):
   if nu_minterm <= 0:
      nu_minterm=int(input("ERROR! please enter a positive value for the number of minterms:"))
   elif nu_minterm > 2**(nu_var):
      nu_minterm=int(input("ERROR! please enter a valid value for the number of minterms:"))
   else:
      zero = 1
      smaller = 1

      

#Getting the values of the minterms and checking if its in range for the allowed minterms
arr=[]
arr3=[]
i =0
while i < nu_minterm:
        x=int(input("Enter min term:"))
        if x >= 2**(nu_var) or x<0:
                print("ERROR please enter a vaild number for the minterm")
        else:
           z = num_one(x)
           arr.append(x)
           arr3.append(z)
           i += 1
	        

#variable to check the totality function 
numOfMinterms = len(set(arr))

#getting number of groups

arr2=arr
unique_groups = set(arr3)
num_groups = len(unique_groups)

sarr=[[]]

for i in arr:
        if i == 0:
                sarr = [[[0]]]



group_number = 0
pairs_number = 0
counter = 0

#sorting the minterms according to their group number

for i in range(max(arr3)):
  group_number += 1
  sarr.append([])
  for j in arr:
                 
       if num_one(j) == group_number:
           

           sarr[i+1].append([j])
       

  
for i in sarr:
        if i == []:
                sarr.remove([])                

#First comparison
prime_arr=[]
s2arr=[]
z=0
q=0
for i in range(len(sarr)-1):
        
        l1=len(sarr[i])

        l2=len(sarr[i+1])
        

        for x in range(l1):
                       
                       for y in range(l2):
                                      
                          z =  (sarr[i+1][y][0]) -  (sarr[i][x][0])

                          if z>0:
                                      
                                if math.log(z, 2).is_integer():

                                        q=q+1
                                      
                                        s2arr.append([sarr[i][x][0],z])
                                      
                                        if sarr[i][x][-1] != "p":
                                      
                                                sarr[i][x].append("p")
                                       
                                        if sarr[i+1][y][-1] !="p":
                                      
                                                sarr[i+1][y].append("p")

                                      
                       

#sorting the comparison
                               
s3arr = []
for i in range(len(s2arr)):
    s3arr.insert(i, [])
    if len(s2arr) == 1 :
            s3arr[i].append(s2arr[0])
    else:        
       for j in s2arr:
               if num_one(j[0]) == pairs_number:
                       s3arr[i].append(j)
    pairs_number += 1
pairs_number = 0      
for i in range(len(s3arr)):
   for j in s3arr:
        if j == []:
                s3arr.remove([])
                
  
#picking the prime implicants and putting them in an array

#piece of code 1
for i in range(len(sarr)):
        l1=len(sarr[i])
        for x in range(l1):
                       if sarr[i][x][-1]!="p":
                               prime_arr.append(sarr[i][x][0:])
if len(s2arr)==2:
        z=abs(s2arr[1][0]-s2arr[0][0])
happen2=0
if z!=0:
        if len(s2arr)==2 and not(math.log(z, 2).is_integer()):
                if len(s2arr[0])==2:
                        for i in s2arr:
                               prime_arr.append(i)
                        happen2=1        
                        happen=1

happen = 0
#piece of code 2
if len(s3arr)== 1 and happen2==0:
        happen = 1
        for k in s3arr[0]:
                prime_arr.append(k)
                


# All comparisons
if q !=0 and len(sarr)>2:
        li=1
        while li!=0 and len(s3arr)>1:
                li=0
                s2arr=[]
                sarr=s3arr
                s3arr=[]
                s4arr=[]
                for i in range(len(sarr)-1):
        
                 l1=len(sarr[i])

                 l2=len(sarr[i+1])
        

                 for x in range(l1):
                       
                               for y in range(l2):
                                      
                                  z =  (sarr[i+1][y][0]) -  (sarr[i][x][0])

                                  if sarr[i][x][-1] == "p":
                                          g1=sarr[i][x][1 : (len(sarr[i][x])-1)]
                                  else:
                                          g1=sarr[i][x][1 : (len(sarr[i][x]))]

                                  if sarr[i+1][y][-1] == "p":
                                          g2=sarr[i+1][y][1 : (len(sarr[i+1][y])-1)]
                                  else:
                                          g2=sarr[i+1][y][1 : (len(sarr[i+1][y]))]       
                                  if z>0:
                                  
                                          if math.log(z, 2).is_integer() and areEqual(g1,g2): 

                                                  li=li+1

                                                  mn=[]

                                                  mn.append(sarr[i][x][0])

                                                  for k in g1:

                                                         mn.append(k)
                                                

                                                  mn.append(z)        
                                                  s2arr.append(mn)
                                      
                                                  if sarr[i][x][-1] != "p":
                                      
                                                        sarr[i][x].append("p")
                                       
                                                  if sarr[i+1][y][-1] !="p":
                                      
                                                        sarr[i+1][y].append("p")

  
                
                
   
                # removing the similar prime implicants
                if len(s2arr)==0:
                        pass

                elif len(s2arr)==1:
                        s4arr=s2arr
                else:        
                        for i in range(len(s2arr)-1):
                                z=0
                                for d in range(i+1,len(s2arr)):
                                        if s2arr[i][0]==s2arr[d][0]:
                                                if areEqual(s2arr[i],s2arr[d]):
                                                        z=z+1
                                if z==0:
                                        s4arr.append(s2arr[i])
                        z=0
                        for d in range(len(s4arr)):
                                if s2arr[-1][0]==s4arr[d][0]:
                                        if areEqual(s2arr[-1],s4arr[d]):
                                                z=z+1

                                               
                        if z==0:
                                s4arr.append(s2arr[-1])

          
                #prime inserting
                for i in range(len(sarr)):
        
                        l1=len(sarr[i])
                        for x in range(l1):
                                   if sarr[i][x][-1]!="p":
                                           
                                          prime_arr.append(sarr[i][x][0:])
                         
                #sorting the comparison
                aser = len(s4arr)
                kiol=0
                for i in s4arr:
                        for x in s4arr :
                                if num_one(i[0])!=num_one(x[0]):
                                        kiol=kiol +1
                                      
                        
                for i in range(num_groups):
                   s3arr.insert(i, [])
                      
                   if aser == 1:
                           s3arr[i].append(s4arr[0])
                   elif aser !=1 and kiol==0:
                           s3arr=[s4arr]
                   else:
                     for j in s4arr:

                       if num_one(j[0]) == pairs_number:
                               s3arr[i].append(j)
                       if j == []:
                              aser +=1
                   pairs_number  += 1  
             
                for i in range(len(s4arr)):
                          for j in s4arr:
                                if j == []:
                                    s4arr.remove([])
                
                num_groups -= 1

                
#another prime insertion incase the peace of code 2 didnt occur didn't happen
#piece of code 3
if len(s3arr)==1 and not (happen):
        for k in s3arr[0]:
                prime_arr.append(k)

# removing the similar prime implicants
prime_arr1=[]
if len(prime_arr)==1:
        prime_arr1=prime_arr
else :       
        for i in range(len(prime_arr)-1):
                 z=0
                 for d in range(i+1,len(prime_arr)):
                        if prime_arr[i][0]==prime_arr[d][0]:
                                  if areEqual(prime_arr[i],prime_arr[d]):
                                          z=z+1
                 if z==0:
                         prime_arr1.append(prime_arr[i])
                         z=0
                         for d in range(len(prime_arr1)):
                                if prime_arr[-1][0]==prime_arr1[d][0]:
                                        if areEqual(prime_arr[-1],prime_arr1[d]):
                                                z=z+1

                                               
                         if z==0:
                                prime_arr1.append(prime_arr[-1])

if len(prime_arr1)==0 and len(prime_arr)!=0:
        prime_arr1.append(prime_arr[0])

        
print("Number of prime Implicant:"+str(len(prime_arr1)))

# representing the prime implicants using letters(props to asora & ashour)
def letter(elem,varible):
    B="A B C D E F G H I J K L M N O P Q R"
    q=B.split()
    vn=q[0:varible]
    vn.reverse()
    z=bin(elem[0])[2:]
    diff=varible-len(z)
    numar=[]
    for i in range(len(z)):
        numar.append(z[i])

    numar.reverse()    
    if diff ==0:
        pass
    else:
        for i in range(diff):
            numar.append('0')

    for i in range(varible):
        if numar[i]=='0':
            vn[i]=vn[i]+"'"

    #print(vn)
    if len(elem)==1:
         vn.reverse()
         return ("".join(vn))
    else:
        csc=elem[1:]
        wer=[]
        for i in csc:
            wer.append(math.log(i,2))
        
        cxz=[]
        for i in range(len(vn)):
            if not(i in wer):
                cxz.append(vn[i])
        #print(cxz)
        cxz.reverse()
        return "".join(cxz)

# printing prime implicants in letter form       
asora_ashour = 0    
prime_letters = []    
for i in prime_arr1:
        asora_ashour = letter(i, nu_var)
        prime_letters.append(asora_ashour)

print("Prime Implicants :  " + "    ".join(prime_letters))        

                
#a function to eliminate the rows and columns covered by the 
def essential(matrix = [], *args):
    for n in range(rows):
        if(matrix[x][n] == 1):
            for a in range(cols):
                matrix[a][n] = 0
        else:
            matrix[x][n] = 0
        
    
#construct the table    
prime  = len(prime_arr1)
minterms = 2**(nu_var+1)
rows, cols = (minterms, prime)
matrix = [[0 for i in range(rows)] for j in range(cols)]
# create an array that contains the numbers of the essential prime implicants
ess = []
# add the prime implicants to the table
p2 = []
temp = []
z = 0
for i in range(len(prime_arr1)):
        temp.append(prime_arr1[i][0])
        for j in range(len(prime_arr1[i])):    
            a  = list(itertools.combinations(prime_arr1[i][1:],j))
            for x in range(len(a)):
                for y in range(len(a[x])):
                    z = z + a[x][y] 
                    temp.append(prime_arr1[i][0]+z)
                z = 0
        p2.append(temp)
        temp = []
for i in range(len(p2)):
        for j in range(len(p2[i])):
                matrix[i][p2[i][j]] = 1
                                
#check for essential prime implicants		
z = 0
x = 0

for i in range(rows):
    for j in range(cols):
        if(matrix[j][i] == 1):
            z = z + 1
            x = j
    if (z == 1):
        ess.append(prime_letters[x])
        essential(matrix, x)
    z = 0

essp =  " , ".join(ess)

if len(ess) != 0 :
  print("Number of Essential Prime Implicants:",len(ess))
  print("Essential Prime Implicants:",essp)
else :
  print("Number of Essential Prime Implicants: 0")
  print("Essential Prime Implicants:","None")

#final answer part 1
if len(ess) == 1:
  ans_1 = ess[0]
else :
  ans_1 =  " + ".join(ess)

import numpy as np
import string 

#Matching minterms with Pn
arr = np.array(matrix,dtype="object")
#print(arr)
indx = np.shape(arr)[0]+1
imp = np.array([i for i in range(1,indx)])

a_imp= arr*imp[:,np.newaxis]
col = np.shape(a_imp)[1]
pet_arr= []
for i in range(0,col):
      s_imp = a_imp[:,i]
      s_imp = s_imp[s_imp != 0]
      pet_arr.append(s_imp)
pet_arr = np.array(pet_arr,dtype="object")
pet_arr=[x for x in pet_arr if np.shape(x)[0] != 0]

#unique array :
import itertools
uni = []
for element in itertools.product(*pet_arr):
    uni.append(np.unique(np.array(element)))

#Multiplying Pn     
unique_data = [list(x) for x in set(tuple(x) for x in uni)]
uni2 = np.array(unique_data, dtype="object")
indx = np.shape(uni2)[0]

uni_3=[]

# elements to be absorbed
for i in range(0,indx-1):
        for j in range(i+1, indx):
               if all(elem in unique_data[i]  for elem in unique_data[j]) :
                    uni_3.append(unique_data[i])
                    
               if all(elem in unique_data[j]  for elem in unique_data[i]):
                  uni_3.append(unique_data[j])

# Absorption            
uni_f =[]
uni_f = [ x for x in unique_data if x not in uni_3] 


#mapping
for i in range(0, len(uni_f)):
  for j in range(0,len(uni_f[i])):
    for k in range (0, len(prime_letters)):
      if uni_f[i][j] == k + 1:
        uni_f[i][j] = prime_letters[k]


for i in range(0,len(uni_f)):
    uni_f[i] =  " + ".join(uni_f[i])


# cost
cost = [1 for i in range(0, len(uni_f))]

#check for petrick , print according to min cost
if len(uni_f) != 0 :
  for i in range(0,len(uni_f)):
    for j in range(0,len(uni_f[i])):
        if uni_f[i][j] == ' ' or uni_f[i][j] == "'" or len(uni_f[i]) == 1:
          cost[i] = cost[i] - 1
        if uni_f[i][j] == "'" and len(uni_f[i]) == 2 :
          cost[i] = cost[i] - 1
        cost[i] = cost[i] + 1

  min = cost[0] 
  x = 0
  for i in range(0, len(cost)):
    if cost[i] < min :
      min = cost[i]
      x = i 
  ans_2 = uni_f[x]


#Final answer
if numOfMinterms == 2**nu_var:
  print("Function : 1 ")
elif len(uni_f) == 1 :
  print("Function :", ans_1)

elif len(ess) == 0:
  print("Function :", ans_2)
else:
  print("Function :", ans_1, "+", ans_2)
  
