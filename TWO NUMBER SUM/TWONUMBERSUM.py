# Time complexity =O(n*n) and space complexity=O(1) this is first try of normal type
def twonumsum(arr,targetsum):
    for i in range(len(arr)-1):
        firstno=arr[i]
        for j in range(i+1,len(arr)-1):
            if firstno + arr[j]==10:
                return [firstno,arr[j]]

    return []

arr1=[2,3,4,5,1,11,-1,12]
targetsum=10
print(twonumsum(arr1,targetsum))


# time complexity=O(n) and space complexity=O(n) this is second type requires least time but requires space
#here we uses a dictionary thats why space complexity increased
def twonumsum(arr,targetsum):
    store={}
    for num in arr:
        numneed=targetsum-num
        if numneed in store:
            return [numneed,num]
        else:
            store[num]=True
    return []

arr1=[2,3,4,5,1,-1,12,11]
targetsum=10
print(twonumsum(arr1,targetsum))

#time complexity=O(nln(n)) and space complexity=O(1) this is third type requires comparitively less time in less space
#soting requires ln(n) types
def twonumsum(arr,targetsum):
    arr.sort()
    left,right=0,len(arr)-1
    while left<right:
        raw=arr[left] + arr[right]
        if raw==targetsum:
            return [arr[left],arr[right]]
        elif raw < targetsum:
            left+=1
        else:
            right-=1
    return []
arr1=[2,3,4,5,1,-1,12,11]
targetsum=10
print(twonumsum(arr1,targetsum))
