class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS= Counter(s)
        listT= Counter(t)
        return listS==listT


