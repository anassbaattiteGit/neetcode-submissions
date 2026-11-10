class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = dict.fromkeys(set(nums), 0)
        for i in nums:
            hm[i] += 1
        kMax = []
        for i in range(k):
            max_key = max(hm, key=hm.get)
            kMax.append(max_key)
            hm[max_key] = float('-inf')
        
        return kMax[:k]
        
            

        

        
        


