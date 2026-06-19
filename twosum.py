# rezvane

l1=[1,2,3,4,5,6,7]
target=9
res=[(l1[i],l1[j]) for i in range(len(l1)) for j in range(i,len(l1)) if l1[i] + l1[j] == target]
print(res)
