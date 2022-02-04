def flatten(B):##O(B)
    nums = []
    for x in range(len(B)):
        for y in range(len(B[x])):
            nums.append(B[x][y])
            
    return nums
def radix_sort(nums,max_digits):##O(MAX_DIGTIS * (N+B))
    
    for digit in range(0,max_digits): ##O(MAX_DIGITS)
        B = [[] for x in range(10)]
        
        for item in nums:##O(N)
            thisdigit = item // 10 ** digit%10
            B[thisdigit].append(item)
            
            
        nums = flatten(B)##O(B)
        
    return nums
        
        
nums = [1,10,12,444,321,100]
max_digits = len(str(max(nums)))
ans = radix_sort(nums,max_digits)

print(ans)
##TIME COMPLEXITY O(D * (N+B))
##D - MAX_DIGITS
##N - INPUT SIZE
##B - BASE (HERE 10)

##IF K IS THE LARGEST NUMBER
## D = LOG B(K)
##TIME COMPLEXITY O(LOGB(K) * (N+B))

##SPACE COMPLEXITY : O(N)
