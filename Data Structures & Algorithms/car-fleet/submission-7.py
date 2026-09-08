class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []

        for car in cars:
            time = (target - car[0]) / car[1]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)