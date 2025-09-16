# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

if __name__ == "__main__":
    tests = [
        [1,3,4,2,2],
        [3,1,3,4,2],
        [3,3,3,3,3], 
    ]

    for arr in tests:
        print(f"{arr} -> {Solution().findDuplicate(arr)}")
