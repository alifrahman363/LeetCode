class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # strip removes the whitespace of the start and end
        stripped = s.strip()
        strList = stripped.split(" ")
        lastWord = strList[-1]
        return len(lastWord)

        