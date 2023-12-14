class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        rowSum = [0]*rows
        colSum = [0]*cols
        print(rowSum)
        for x in range(rows):
            rowSum[x] = sum(grid[x])
                   
        for x in range(cols):
            tempSum = 0
            for y in range(rows):
                tempSum += grid[y][x]
            colSum[x] = tempSum
                   
        for x in range(rows):
            for y in range(cols):
                grid[x][y] = 2*rowSum[x]-cols + 2*colSum[y] -rows
                   
        return grid