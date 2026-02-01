def minCostClimbingStairs(cost):
    for i in range(len(cost) - 3, -1, -1):
        print(i)
        cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])
cost = [1,2,3]
print(minCostClimbingStairs(cost))