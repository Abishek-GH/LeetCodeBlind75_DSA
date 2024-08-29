# Solution 1 - Not Optimal
# Basic Approach
# Time Complexity --> O(n^2)
'''
nums = [5]
answer = []
for i, v in enumerate(nums):

    temp = nums[:]
    product = 1
    temp.remove(v)  
    for j in temp:
        product *= j

    answer.insert(i, product)

print(answer)
'''

# Solution 2 --> CHATGPT Response
# Time Complexity --> O(n)
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # Initialize the answer array with 1s

    # Step 1: Calculate the left products and store in answer
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]  # Update left product for next iteration

    # Step 2: Calculate the right products and update answer
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product  # Multiply by right product
        right_product *= nums[i]  # Update right product for next iteration

    return answer
