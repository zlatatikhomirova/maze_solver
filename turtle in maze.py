import turtle



wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour  
wn.setup(1300,700)  
def main(maze):
    queue = [(0, 0)] # use a local variable, not a member
    visited = {} # use a dict, key = coordinate-tuples, value = previous location
    visited[(0, 0)] = (-1, -1)
    end_r, end_c = len(maze), len(maze[0])
    ends = (end_r-1, end_c-1)
    while len(queue) > 0: # don't use running as variable
        # no need to use current; just reuse r and c:
        r, c = queue.pop(0) # you can remove immediately from queue
        if (r, c) == ends:
            joe.goto(-650 + 24 + c * 24, 350 - 24 - r * 24)
            return True
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            new_r = r + dy
            new_c = c + dx
            if (-1 < new_r < end_r) and (-1 < new_c < end_c) and not (new_r, new_c) in visited and maze[new_r][new_c] == 0:
                visited[(new_r, new_c)] = (r, c)
                joe.goto(-650 + 24 + c * 24, 350 - 24 - r * 24)
                queue.append((new_r, new_c))
    return False
 
# maze = [
#   [0, 1, 1, 1, 1, 1, 1],
#   [0, 0, 1, 1, 0, 1, 1],
#   [1, 0, 0, 0, 0, 1, 1],
#   [1, 1, 1, 1, 0, 0, 1],
#   [1, 1, 1, 1, 1, 0, 0]
#   ]
 
# print(main(maze))
 
# maze = [
#     [0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 0, 0, 1, 1],
#     [1, 0, 0, 0, 0, 1, 1],
#     [1, 1, 0, 1, 0, 0, 1],
#     [1, 1, 0, 0, 1, 1, 1]
#   ]
  
# print(main(maze))
 
# maze = [
#   [0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0],
#   [1, 1, 1, 1, 1, 1, 0],
#   [1, 1, 1, 1, 1, 1, 1]
#   ]
  
# print(main(maze))
 
# maze = [
#   [0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 1, 1, 0],
#   [1, 1, 1, 1, 1, 1, 0]
#   ]
  
# print(main(maze))

def setupMaze(grid):
    for y in range(len(grid)):                       # select each line in the grid
        for x in range(len(grid[0])):                # identify each character in the line
            character = grid[y][x]                   # assign the grid reference to the variable character
            screen_x = -650 + 24 + x * 24          # assign screen_x to screen starting position for x ie -588
            screen_y = 350 - 24 - y * 24        # assign screen_y to screen starting position for y ie  288

            if character == 1:                     # if grid character contains an +
                maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                walls.append((screen_x, screen_y))  
                # add coordinate to walls list

            if (x, y) == (len(grid[0])-1, len(grid)-1):                    # if grid character contains an e
                maze.goto(screen_x, screen_y) 
                maze.color("green")        # move turtle to the x and y location and
                maze.stamp()                          # stamp a copy of the turtle (green square) on the screen
                finish.append((screen_x, screen_y))  # add coordinate to finish list

            if (x, y) == (0, 0):                     # if the grid character contains an s
                joe.goto(screen_x, screen_y)      # move turtle to the x and y location
            
                
walls =[]                    # create walls coordinate list
finish = []                  # enable the finish array
grid = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
  ]

shape_x, shape_y = round((1300/2)/(21* len(grid[0])), 0), round((700/2)/(21* len(grid)), 0)
maze = turtle.Turtle()
maze.shape("square")            # the turtle shape
maze.color("white")
# maze.resizemode("user")
# maze.shapesize(shape_x, shape_y, 3)            # colour of the turtle
maze.penup()                    # lift up the pen so it do not leave a trail
maze.speed(3)                   # sets the speed that the maze is written to the screen
# enable the maze class
joe = turtle.Turtle()
joe.color("blue")
joe.speed(2)
# joe.resizemode("user")
ends = (len(grid)-1, len(grid[0])-1)
# joe.shapesize(shape_x, shape_y, 12)

# wn.setup(24*len(grid[0]),24*len(grid))  
joe.penup()
setupMaze(grid)
print(main(grid))             # call the setup maze function
