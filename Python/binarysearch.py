# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

class Solution(object):
     def search(self, nums, target):
          """
          :type nums: List[int]
          :type target: int
          :rtype: int
          """

          low = 0
          high = len(nums) - 1
          while low <= high:
               mid = (low + high) // 2
               if nums[mid] < target:
                    low = mid + 1
               elif nums[mid] > target:
                    high = mid - 1
               else:
                    return mid
          return -1
          
               
list = [-2, 0, 10, 30, 45]
print(Solution.search(Solution, list, 30))
