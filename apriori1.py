n=int(input("Enter the no of transactions:"))
m=int(input("Enter the no of items:"))

#n=9
#m=5
def f1(x):
	count=0
	for i in range(0,n):
		if ((x in t[i])):
			count=count+1
	return count

def f2(x,y):
	count=0
	for i in range(0,n):
		if ((x in t[i]) and y in t[i]):
			count=count+1
	return count

def f3(l):
	x,y,z,count=l[0],l[1],l[2],0
	for i in range(0,n):
		if ((x in t[i] and y in t[i] and z in t[i])):
			count=count+1
	return count

def f4(l):
	w,x,y,z,count=l[0],l[1],l[2],l[3],0
	for i in range(0,n):
		if ((w in t[i] and x in t[i] and y in t[i] and z in t[i])):
			count=count+1
	return count


"""
t=[[1,2,5,0,0],[2,4,0,0,0],[2,3,0,0,0],[1,2,4,0,0],[1,3,0,0,0],
   [2,3,0,0,0],[1,3,0,0,0],[1,2,3,5,0],[1,2,3,0,0]]
"""
t=[]
tin=[]
for x in range(0,n):
	tin=[]
	for y in range(0,m):
		tin.append(0)
	t.append(tin)


for x in range(0,n):
	print("Enter no item present in t",x)
	m1=int(input())
	print("Enter item for t",x)
	for y in range(0,m1):
		t[x][y]=int(input())
print("list:")
print(t)

ms=int(input("Min Support:"))
conf=int(input("Confidence(%):"))
conf=conf/100

c=[]
l1=[]
l=[]
count=0
for x in range(1,m+1):
	l1.append(x)

for x in range(1,m+1):
	count=f1(x)
	c.append(count)
#C1
print("C1:")
print("I=",l1)
print("count=",c)

for x in range(0,m):
	if(c[x]>ms-1):
		l.append(l1[x])

		
print("\nL1:")
print("I=",l)
print("count=",c)

flag=0
while(flag==0):
	#C2

	print("")
	print("C2:\n[x,y,count]")
	lout=[]
	for x in range(1,len(l)+1):
		for y in range(x+1,len(l)+1):
			if ((x in l) and (y in l)):
				lin=[]
				lin.append(x)
				lin.append(y)
				count=f2(x,y)
				lin.append(count)
				lout.append(lin)

	print(lout)

	print("\nL2")
	lout1=[]
	for x in range(0,len(lout)):
		if (lout[x][2]>ms-1):
			lout1.append(lout[x])
	print(lout1)
	if (lout1==[]):
		print("end")
		flag=1
		fl=l
		break

	print("\nC3:\n[x,y,z,count]")
	l3out=[]
	for x in range (0,len(lout1)):
		for y in range(x+1,len(lout1)):
			if (lout1[x][0]==lout1[y][0]):
				l3in=[]
				l3in.append(lout1[x][0])
				l3in.append(lout1[x][1])
				l3in.append(lout1[y][1])
				count=f3(l3in)
				#print(l3in)
				l3in.append(count)
				l3out.append(l3in)
	print (l3out)

	print("\nL3")
	lout2=[]
	for x in range(0,len(l3out)):
		if (l3out[x][3]>ms-1):
			lout2.append(l3out[x])
	print(lout2)
	if (lout2==[]):
		print("end")
		fl=lout1
		flag=1
		break

	l4out=[]
	print("\nC4:\n[w,x,y,z,count]")
	for x in range (0,len(lout2)):
		for y in range(x+1,len(lout2)):
			if (lout2[x][0]==lout2[y][0] and lout2[x][1]==lout2[y][1] ):
				l4in=[]
				l4in.append(lout2[x][0])
				l4in.append(lout2[x][1])
				l4in.append(lout2[x][2])
				l4in.append(lout2[y][2])
				count=f4(l4in)

				#print(l3in)
				l4in.append(count)
				l4out.append(l4in)
	print (l4out)

	print("\nL4")
	lout4=[]
	for x in range(0,len(l4out)):
		if (l4out[x][4]>ms-1):
			lout4.append(l4out[x])
	print(lout4)
	if (lout4==[]):
		print("end")
		flag=1
		fl=lout2
		break

print("final list:",fl)		
"""
outpout
C:\Users\Satnam\Desktop\Python>python apriori1.py
Enter the no of transactions:9
Enter the no of items:5
Enter no item present in t 0
3
Enter item for t 0
1
2
5
Enter no item present in t 1
2
Enter item for t 1
2
4
Enter no item present in t 2
2
Enter item for t 2
2
3
Enter no item present in t 3
3
Enter item for t 3
1
2
4
Enter no item present in t 4
2
Enter item for t 4
1
3
Enter no item present in t 5
2
Enter item for t 5
2
3
Enter no item present in t 6
2
Enter item for t 6
1
3
Enter no item present in t 7
4
Enter item for t 7
1
2
3
5
Enter no item present in t 8
3
Enter item for t 8
1
2
3
list:
[[1, 2, 5, 0, 0], [2, 4, 0, 0, 0], [2, 3, 0, 0, 0], [1, 2, 4, 0, 0], [1, 3, 0, 0, 0], [2, 3, 0, 0, 0], [1, 3, 0, 0, 0], [1, 2, 3, 5, 0], [1, 2, 3, 0, 0]]
Min Support:2
Confidence(%):80
C1:
I= [1, 2, 3, 4, 5]
count= [6, 7, 6, 2, 2]

L1:
I= [1, 2, 3, 4, 5]
count= [6, 7, 6, 2, 2]

C2:
[x,y,count]
[[1, 2, 4], [1, 3, 4], [1, 4, 1], [1, 5, 2], [2, 3, 4], [2, 4, 2], [2, 5, 2], [3, 4, 0], [3, 5, 1], [4, 5, 0]]

L2
[[1, 2, 4], [1, 3, 4], [1, 5, 2], [2, 3, 4], [2, 4, 2], [2, 5, 2]]

C3:
[x,y,z,count]
[[1, 2, 3, 2], [1, 2, 5, 2], [1, 3, 5, 1], [2, 3, 4, 0], [2, 3, 5, 1], [2, 4, 5, 0]]

L3
[[1, 2, 3, 2], [1, 2, 5, 2]]

C4:
[w,x,y,z,count]
[[1, 2, 3, 5, 1]]

L4
[]
end
final list: [[1, 2, 3, 2], [1, 2, 5, 2]]

C:\Users\Satnam\Desktop\Python>"""
