    
def containsDuplicate(nums):
	return len(set(nums)) != len(nums)


'''set items are unordered, unchangeable, and do not allow duplicate values.'''
'''sort() can only use in lists and sorted() accept any iterable'''
''' what i did is that i try to sort the arrays with another list and then iterate to find the first equal elemnts so return True otherwise retur False but the sort funct
ion have a O(n log n)'''

