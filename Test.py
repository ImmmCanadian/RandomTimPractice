class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.strip()
        count=0
        for i in range(len(s), 0, -1):
            if(s[i-1]==" "):
                break
            else:
                count += 1
        return count

s= Solution()
print(s.lengthOfLastWord("a"))
