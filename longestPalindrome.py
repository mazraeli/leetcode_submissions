class Solution(object):
    
    def palindrome(self, s, i, j):
        
        while (i >= 0 and j < len(s) and s[i] == s[j]):
            i -= 1
            j += 1
        
        return s[i+1:j]


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        arr_len = len(s)

        result = ''

        for i in range(arr_len):
            # even-length palindrome
            res1 = self.palindrome(s, i, i + 1)
            # odd-length palindrome
            res2 = self.palindrome(s, i, i)

            if (len(res1) > len(res2)):
                if (len(res1) > len(result)):
                    result = res1
            elif (len(res2) > len(result)):
                result = res2

        return result
