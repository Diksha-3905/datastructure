#You are given a 2D grid heightMap representing an elevation map. Water can be trapped between bars. Return the total amount of water trapped after raining.

import heapq

def trapRainWater(heightMap):
    if not heightMap or not heightMap[0]:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = [[False]*n for _ in range(m)]
    pq = []

    # Push all boundary cells into min-heap
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                heapq.heappush(pq, (heightMap[i][j], i, j))
                visited[i][j] = True

    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    trapped = 0
    max_height = 0

    while pq:
        h, x, y = heapq.heappop(pq)
        max_height = max(max_height, h)

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                trapped += max(0, max_height - heightMap[nx][ny])
                heapq.heappush(pq, (heightMap[nx][ny], nx, ny))

    return trapped

# Test
heightMap = [[1,4,3,1,3,2],
             [3,2,1,3,2,4],
             [2,3,3,2,3,1]]
print(trapRainWater(heightMap))  # Output: 4
