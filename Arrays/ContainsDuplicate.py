    
def containsDuplicate(nums):
	return len(set(nums)) != len(nums)


'''set items are unordered, unchangeable, and do not allow duplicate values.'''
'''sort() can only use in lists and sorted() accept any iterable'''
''' what i did is that i try to sort the arrays with another list and then iterate to find the first equal elemnts so return True otherwise retur False but the sort funct
ion have a O(n log n)'''

##Brute Force ##
def containsDuplicat(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if  nums[i] == nums[j]:
                return True
    return False
##Testing Function 
answer = containsDuplicat([2,1,3,2])
print(answer)

