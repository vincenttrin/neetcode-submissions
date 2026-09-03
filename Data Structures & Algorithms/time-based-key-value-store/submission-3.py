class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list )

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # binary search through list
        values = self.TimeMap[key]

        if not values or values[0][0] > timestamp: return ""
        if len(values) == 1: return values[0][1]
        l, r = 0, len(values)
        
        res = values[0][1]
        res_time = l

        while l < r:
            m = (r + l) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] < timestamp:
                res_time = values[m][0]
                res = values[m][1]
                l = m + 1
            else:
                r = m

        return res
            