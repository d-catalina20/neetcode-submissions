class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int curr_max = nums[0];
        int curr_min = nums[0];
        int res = nums[0];
        for (int i = 1; i < n; i++) {
            int curr = nums[i];
            int temp = max({curr, curr * curr_max, curr * curr_min});
            curr_min = min({curr, curr * curr_max, curr * curr_min});
            curr_max = temp;

            res = max(res, curr_max);
        }
        return res;
    }
};
