'''
Template 1 
Initial Condition: left = 0, right = length-1
Termination: left > right
Searching Left: right = mid-1
Searching Right: left = mid+1

Template 2
Initial Condition: left = 0, right = length - 1
Termination: left == right
Searching Left: right = mid
Searching Right: left = mid+1

Template 3
Initial Condition: left = 0, right = length-1
Termination: left + 1 == right
Searching Left: right = mid
Searching Right: left = mid

https://leetcode.com/explore/learn/card/binary-search/136/template-analysis/935/
'''
