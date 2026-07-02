class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        if (n == 0) return 0;
        
        // dp[i][j] will be true ONLY if the specific substring s[i..j] is a palindrome
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int totalPalindromes = 0;
        
        // Base Case 1: Single letters
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            totalPalindromes++;
        }
        
        // Base Case 2: Two letters
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                totalPalindromes++;
            }
        }
        
        // Recursive Step: Length 3 and greater
        for (int len = 3; len <= n; len++) {
            for (int i = 0; i < n - len + 1; i++) {
                int j = i + len - 1;
                
                // s[i..j] is a palindrome if outer letters match AND inner string is a palindrome
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    totalPalindromes++;
                }
            }
        }
        
        return totalPalindromes;
    }
};
