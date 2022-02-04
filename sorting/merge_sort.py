def merge_sort(nums):
    
    if len(nums) > 1:
        mid = len(nums) // 2 ##split array from middle
        
        left_arr = nums[0:mid] 
        right_arr = nums[mid:] 
        
        merge_sort(left_arr)##sort left subarray
        merge_sort(right_arr)##sort right subarray
        
        i = 0
        j = 0
        k = 0
        ##merge the two sorted arrays in linear time to get a combined sorted array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                nums[k] = left_arr[i]
                i+=1
                
            else:
                nums[k] = right_arr[j]
                j+=1
                
                
            k+=1
                
        while i < len(left_arr):
            nums[k] = left_arr[i]
            i+=1
            k+=1
            
        while j < len(right_arr):
            nums[k] = right_arr[j]
            j+=1
            k+=1
            
        return nums
        
nums = [1,10,9,7,21,5,8]
ans = merge_sort(nums)
print(ans)
## T(N) = 2 T(N/2) + Q(N)
##TIME COMPLEXITY O(NLOGN) BEST CASE, AVERAGE CASE, WORST CASE
##SPACE COMPLEXITY O(N)

##GOES THROUGH THE WHOLE ARRAY EVEN IF IT IS SORTED
##SLOWER FOR SMALLER INPUTS
            
