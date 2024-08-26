# sum_numbers.py

# Read input from the input.txt file
# with open('input.txt', 'r') as file:
#     input_data = file.read()




# Solution 1
# Approach --> Brute Force
# Time complexity --> O(n^2)

'''
class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):  
                if i == j:
                    continue  
                else:
                    if nums[i] + nums[j] == target:
                        return [i, j]
                
numbers = [3, 3]
target = 6

solution = Solution()
result = solution.twoSum(numbers, target)
'''


# Solution 2
# Approach --> HashMap
# Time Complexity O(n log n)

'''class Solution:
    def twoSum(self, nums, target):
        mpp = {}
        n = len(nums)
        
        for i in range(n):
            num = nums[i]
            more_needed = target - num
            if more_needed in mpp:
                return [mpp[more_needed], i]
            mpp[num] = i

numbers = [3, 3]
target = 6

solution = Solution()
result = solution.twoSum(numbers, target)
'''  


# Solution 3 Optimal 
# Approach -> Greedy (2 Pointer)

class Solution:
    def twoSum(self, nums, target):
        left = 0
        n = len(nums)
        right = n-1
        nums.sort()
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return "Yes"
            elif sum < target:
                left += 1
            else:
                right += 1
        return "No"

numbers = [3, 3]
target = 6

solution = Solution()
result = solution.twoSum(numbers, target)
# Write the output to the output.txt file
with open('output.txt', 'w') as file:
    file.write(f"The sum of the numbers is: {result}")

