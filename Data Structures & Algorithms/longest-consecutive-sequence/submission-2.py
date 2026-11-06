class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxS = 0
        for i in numSet:
            if i - 1 not in numSet:
                j = i
                k = 1
                while j + 1 in numSet:
                    k += 1
                    j += 1
                maxS = max(maxS, k)
        
        return maxS



                
            


                        

        
        