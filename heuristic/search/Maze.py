# application of DFS

# given a maze of size NxN represented by a 2D matrix
# matrix[i][j] takes either of 2 values: 0 or 1
# 1 means path (i.e. u can go), 0 means wall (i.e. u cannot go)
# find the way to go from top left corner (0,0) to bottom right corner (m-1.n-1)
# given that you can only go up/down, left/right


# application: navigate a robot in most effective manner
# approaches: 1. if we know the maze, can use heavy-weight graph algo like Dijkstra algorithm and A* search
# 2. if we don't know the maze, use backtracking (DFS)


# Note: prioritise go down and go right to get better (shorter) path (given start at top left and end at bottom right)
# go up and go down are still in need in certain cases (like m)

class MazeProblem:
    def __init__(self, maze):
        # this is 2D representation of maze
        # 0: obstacle, 1: valid cell
        self.maze = maze

        # it will store solution (S for solution cell)
        self.solution = [['-' for _ in range(len(maze))] for _ in range((len(maze[0])))]


    def find_solution(self):
        if self.solve(0, 0):
            self.show_solution()
        else:
            print('There is no solution..')

    def solve(self, row, col):
        # if we have found the destination (bottom right cell) then it is done
        if self.is_finished(row, col):
            return True

        if self.is_valid(row, col):
            self.solution[row][col] = 'S'

            # go right
            if self.solve(row, col+1):
                return True

            # go down
            if self.solve(row+1, col):
                return True

            # go up
            if self.solve(row-1, col):
                return True

            # go left
            if self.solve(row, col-1):
                return True

            # backtrack as no solution
            self.solution[row][col] = '-'

        return False

    def is_finished(self, row, col):
        if row == len(self.maze) - 1 and col == len(self.maze[0]) - 1:
            self.solution[row][col] = 'S'
            return True
        return False

    def is_valid(self, row, col):
        if row < 0 or row >= len(self.maze) or col < 0 or col >= len(self.maze[0]):
            return False

        # can go if the cell is not obstacle and the cell has not been visited (to avoid infinity loop)
        return self.maze[row][col] == 1 and self.solution[row][col] != 'S'

    def show_solution(self):
        print('\n'.join(''.join(str(x) for x in row) for row in self.solution))

if __name__ == '__main__':
    m = [[1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1],
          [0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1]
         ]

    MazeProblem(m).find_solution()

    m1 = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [1, 1, 0, 0],
          [1, 1, 1, 1],
          ]

    MazeProblem(m1).find_solution()
