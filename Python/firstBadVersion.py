# 278. First Bad Version
# Date: 5/19/23
# You manage a software product, and at some point in the progression
# of version numbers, the product failed an important quality check.
# The isBadVersion API, when given a version number, returns if the
# product has failed the quality check yet.
# Using this API, in the minimum number of API calls, return the
# first bad version out of the given n number of versions that exist.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
     if version >= 4:
          return True
     return False

class Solution(object):
    def firstBadVersion(self, n):
          """
          :type nums: List[int]
          :type target: int
          :rtype: int
          """
          
          if(isBadVersion(0) == True):
               return 0
          
          low = 1
          high = n
          while low <= high:
               mid = (low + high) // 2
               print("---")
               print(low)
               print(high)
               print(mid)
               if isBadVersion(mid) == False:
                    low = mid + 1
               else:
                    if isBadVersion(mid - 1) == True:
                         high = mid - 1
                    else:
                         return mid
          return -1
          
               
print(Solution.firstBadVersion(Solution, 1000))
