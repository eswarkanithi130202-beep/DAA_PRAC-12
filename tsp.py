def tsp(i, visited):
    if visited == (1 << n) - 1:
        return cost[i][0]

    if (i, visited) in dp:
        return dp[(i, visited)]

    ans = float('inf')

    for j in range(n):
        if not (visited & (1 << j)):
            ans = min(ans, cost[i][j] + tsp(j, visited | (1 << j)))

    dp[(i, visited)] = ans
    return ans


def find_path(i, visited):
    path = [i]

    while visited != (1 << n) - 1:
        for j in range(n):
            if not (visited & (1 << j)):
                if cost[i][j] + tsp(j, visited | (1 << j)) == tsp(i, visited):
                    path.append(j)
                    visited |= (1 << j)
                    i = j
                    break

    path.append(0)
    return path


n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
cost = [list(map(int, input().split())) for _ in range(n)]

dp = {}

minimum_cost = tsp(0, 1)
path = find_path(0, 1)

print("Minimum travelling cost:", minimum_cost)
print("Optimal path:", " -> ".join(map(str, path)))
