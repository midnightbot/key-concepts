//Q1
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> ans;
        unordered_map<int,int> maps;
       
        for (int i = 0; i < nums.size();i++){
            if (maps.find(target - nums[i])!= maps.end())
            {
                ans.push_back(i);
                ans.push_back(maps[target - nums[i]]);
                    
                return ans;
            }
            
            else{
                maps[nums[i]] = i;
            }
        }
        return ans;
    }
};

// looping over maps
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> freq;
        
        for(int x: nums){
            
            if(freq.find(x)!=freq.end()){
                freq[x]+=1;
            }
            else{
                freq.insert({x,1});
            }
        }
        
        for(auto& it: freq){
            //cout << it.first << it.second;
            if (it.second > (int) nums.size()/2){
                return it.first;
            }
        }
        return 0;
    }
};
