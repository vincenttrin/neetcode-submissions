# Approaches:
# 1. Array/Heaps - sort based on distance from origin
# 2. 

import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points_heap = []
        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(points_heap, (d, [x,y]))
        k_points = []
        for _ in range(k):
           # append the k closest points.
            k_points.append(heapq.heappop(points_heap)[1])

        return k_points