class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i,j,f=0;
        for(i=0;i < nums.size()-1;i++){
            for(j=i+1;j < nums.size();j++)
                if (nums[i] + nums[j] == target){
                    f=1;
                    break;
                }
            if (f==1){
                break;
            }
        }
        return {i,j};
    }
};
