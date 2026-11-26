class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.hm = defaultdict(list)
        for i, v in enumerate(wordsDict):
            self.hm[v].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        list1 =  self.hm[word1]
        list2 = self.hm[word2]
        i, j = 0, 0
        mindist = float('inf')
        while i < len(list1) and j < len(list2):
            mindist = min(mindist, abs(list1[i] - list2[j]))
            if list1[i] > list2[j]:
                j += 1
            else:
                i += 1
        return mindist




        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)