# Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if (len(s) == 0):
            return 0
        
        max_length = 1
        for c in range(0, len(s) - 1):
            dict = {s[c] : 1}
            count = 1
            for cc in range(c + 1, len(s)):

                # first, check the availability
                if (s[cc] in dict.keys()):
                    break

                dict[s[cc]] = 1
                count += 1
                
                # update the max length var
                if (count > max_length):
                    max_length = count

        return max_length
