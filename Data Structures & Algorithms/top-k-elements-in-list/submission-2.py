class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = dict.fromkeys(set(nums), 0)
        for i in nums:
            hm[i] += 1
        kMax = [[] for _ in range(len(nums) + 1)]
        for e in hm:
            kMax[hm[e]].append(e)
        result = []
        i, j = 0, len(nums)

        while i < k:
            while len(kMax[j]) == 0:
                j -= 1
            result += (kMax[j])
            i += len(kMax[j])
            j -= 1
        
        return result


        
        
        
            

        

        
        


