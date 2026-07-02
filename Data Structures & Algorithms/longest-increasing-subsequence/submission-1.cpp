class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0);
        dp[0] = 1;
        int maxi = 1;
        for (int i = 1; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (dp[j] + 1 > dp[i] && nums[j] < nums[i]) {
                    dp[i] = dp[j] + 1;
                }
            }
            if (dp[i] > maxi) {
                maxi = dp[i];
            }
        }
        return maxi;
    }
};
