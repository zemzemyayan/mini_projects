nums=[6,5,3,5,2,1,2,7,8,9,6]
liste=[]
for i in range(len(nums)):  #i=0 için içerdeki dongu 10 defa donecek
    for j in range(len(nums)):
        if(i==j): break
        if(nums[i]==nums[j]):
            liste.append(nums[i])

print(liste)
