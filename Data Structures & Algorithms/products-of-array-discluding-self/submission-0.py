class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [1] * n 
        l = [1] * n 
        for i in range(n):
            if i == 0:
                l[i] = 1
            else:
                l[i] = nums[i-1] * l[i-1]
        
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                r[i] == 1
            else:
                r[i] = nums[i + 1] * r[i + 1]

        result = []
        for i in range(n):
            result.append(l[i] * r[i])
        return result
        


        