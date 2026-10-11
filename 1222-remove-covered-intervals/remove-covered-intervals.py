class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x:(x[0],-x[1]))
        end = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][1] <= end:
                count += 1
            else:
                end = intervals[i][1]
        return len(intervals)-count



