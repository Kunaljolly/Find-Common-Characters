from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = [Counter(word) for word in words]
        common_counts = counts[0]
        for count in counts[1:]:
            common_counts &= count
        return list(common_counts.elements())
