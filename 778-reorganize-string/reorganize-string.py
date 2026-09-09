class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [[-v, k] for k, v in count.items()]
        prev = None
        heapq.heapify(maxheap)
        news = []
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt, char = heapq.heappop(maxheap)
            news.append(char)
            cnt += 1
            if prev:
                heapq.heappush(maxheap,prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return "".join(news)



            #put in counter, if theres muttiple of the same letter, put them at the end one at a time of the arr, if any letter occurs > half the time its not pssible
