class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)
        while minSpeed <= maxSpeed:
            midSpeed = minSpeed + (maxSpeed - minSpeed) // 2
            acc = 0
            for pile in piles:
                acc += -(-pile // midSpeed)
            if acc > h:
                minSpeed = midSpeed + 1
            else:
                maxSpeed = midSpeed - 1
        return minSpeed