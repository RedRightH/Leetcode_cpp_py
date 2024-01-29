class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = 0,area;
        int left=0; int right= height.size() -1;
        while (left < right){
            if(height[right] <= height[left]){
                area = (right-left)*height[right];
                right -= 1;
            }
            else{
                area = (right-left)*height[left];
                left += 1;
            }
            ans = (area > ans)? area : ans;

        }
        return ans;
    }
};
