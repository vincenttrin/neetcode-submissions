# 1. turn the array into a max heap
# 2. pop 2 largest values and smash them
# 3. if difference > 0, add back to heap
# 4. continue until 1 or 0 stones remain.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heapq.heapify_max(stones)

        while stones and len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)

            diff = stone1 - stone2
            if diff > 0:
                heapq.heappush_max(stones, diff)
            
        if stones: 
            return stones[0]
        else:
            return 0