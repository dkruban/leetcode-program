class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Determines if it's possible to reach the last index from the first index.

        Args:
        nums (list[int]): An integer array where each element represents the maximum jump length at that position.

        Returns:
        bool: True if it's possible to reach the last index, False otherwise.
        """
        # Initialize the last position we can reach
        last_position = len(nums) - 1
        
        # Iterate over the array in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # If we can reach the last position from the current position
            if i + nums[i] >= last_position:
                # Update the last position
                last_position = i
        
        # If we can reach the first position, it means we can reach the last index
        return last_position == 0
