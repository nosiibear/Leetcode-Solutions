# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built
# with those letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        firstOne = False
        letters = {}
        count = 0
        for i in s:
            if i in letters:
                if letters[i] == 1:
                    count += 2
                    letters[i] = 0
                else:
                    letters[i] = 1
            else:
                letters[i] = 1

        for i in letters.keys():
            if not firstOne:
                if letters[i] == 1:
                    firstOne = True

        return count + (1 if firstOne else 0)

print("count:")
print(Solution.longestPalindrome("a", ""))
