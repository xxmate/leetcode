'''
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()

first = intervals[0][0]
last = intervals[0][1]
output = []

for i in range(1, len(intervals)):
    start = intervals[i][0]
    end = intervals[i][1]

    if start <= last:
        if end > last:
            last = end
    else:
        output.append([first, last])
        first = start
        last = end

output.append([first, last])

print(output)
