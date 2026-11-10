class Solution:

    def encode(self, strs: List[str]) -> str:
        s  = []

        for i in strs:
            s.append(f'{len(i)}#' + i)
        
        return "".join(s)



    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            start = i
            while s[i].isdigit():
                i += 1
            nlen = int("".join(s[start: i]))
            i += 1
            strs.append(s[i: i + nlen])
            i += nlen
        
        return strs

        

        



