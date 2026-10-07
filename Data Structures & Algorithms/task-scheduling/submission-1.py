class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_tasks = Counter(tasks)
        maxHeap = [-freq for freq in count_tasks.values()]
        q = deque()
        cycle = 0
        heapq.heapify(maxHeap)

        while len(maxHeap) > 0 or len(q) > 0:
            cycle += 1
            
            if not maxHeap:
                cycle = q[0][1]
            else:
                curr = -heapq.heappop(maxHeap)
                curr -= 1;
                if curr > 0:
                    q.append([-curr, cycle + n])

            if q and q[0][1] == cycle:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return cycle


        