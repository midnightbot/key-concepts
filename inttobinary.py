#Finding binary representation of a given number



## left shift = X * 2
## right sheft = X / 2


a = 16
strs = "" 
for x in range(10):
    if a & (1 << x) != 0:
        strs+="1"
        
    else:
        strs+="0"
print(strs[::-1])       
print(str(int(strs[::-1])))


