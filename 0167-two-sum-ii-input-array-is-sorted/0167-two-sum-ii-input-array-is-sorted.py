class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Problem asks for 1-indexed results
                return [left + 1, right + 1]
            
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []  # Should not be reached based on problem constraints