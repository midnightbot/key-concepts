def bubble_sort(nums):
    
    for x in range(len(nums)):
        for y in range(len(nums)-x-1):
            swapped = False
            if nums[y] > nums[y+1]:
                nums[y],nums[y+1] = nums[y+1],nums[y]
                swapped = True
                
            if swapped == False:##if no pair swapped in this inner loop, this means array is already sorted
                break
                
    return nums
    
    
nums = [1,9,6,7,10,12,4]
ans = bubble_sort(nums)
print(ans)

##TIME COMPLEXITY : O(N^2) WORST CASE AND AVERAGE CASE
##TIME COMPLEXITY : O(N) BEST CASE (OCCURS WHEN ARRAY IS ALREADY SORTED)
##SPACE COMPLEXITY : O(1)
