class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Step 1: Mark the indices corresponding to seen numbers as negative
        for i in range(len(nums)):
            # Get the index corresponding to the current number
            # We use abs() because the number might have already been marked negative
            index = abs(nums[i]) - 1
            
            # If the number at that index is positive, make it negative
            if nums[index] > 0:
                nums[index] = -nums[index]
                
        # Step 2: Find all indices that still have positive numbers
        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # Index `i` corresponds to the number `i + 1`
                missing_numbers.append(i + 1)
                
        return missing_numbers