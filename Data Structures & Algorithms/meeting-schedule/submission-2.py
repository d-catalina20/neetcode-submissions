"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals_sorted = sorted(intervals, key=lambda interval: interval.start)
        prev_interval = intervals_sorted[0]
        for i in range(1, len(intervals_sorted)):
            curr_interval = intervals_sorted[i]
            if curr_interval.start < prev_interval.end:
                return False
            prev_interval = curr_interval
        return True
