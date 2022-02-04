##INSERTION SORT
##ALWAYS PICKS UP AN ELEMENT AND PLACES IT AS ITS CORRECT POSITION

def insertion_sort(nums):
    
    for x in range(1,len(nums)): ## O(N)
        elem = nums[x]
        
        y = x-1
        
        while y>=0 and elem < nums[y]: ## O(N)
            nums[y+1] = nums[y]
            y-=1
            
        nums[y+1] = elem
        
        
    return nums
    
nums = [1,100,12,444,321,10]
ans = insertion_sort(nums)
print(ans)

##TIME COMPLEXITY O(N*N)
##SPACE COMPLEXITY O(1)
