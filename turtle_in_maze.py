import turtle

def setupMaze(grid):
    for y in range(len(grid)):                       # select each line in the grid
        for x in range(len(grid[0])):                # identify each character in the line
            character = grid[y][x]                   # assign the grid reference to the variable character
            screen_x = -588 + (x * 24)               # assign screen_x to screen starting position for x ie -588
            screen_y = 288 - (y * 24)                # assign screen_y to screen starting position for y ie  288

            if character == 1:                     # if grid character contains an +
                maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                walls.append((screen_x, screen_y))   # add coordinate to walls list

            if (screen_x, screen_y) == ends:                    # if grid character contains an e
                end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                finish.append((screen_x, screen_y))  # add coordinate to finish list

            if (screen_x, y) == (0, 0):                     # if the grid character contains an s
                sprite.goto(screen_x, screen_y)      # move turtle to the x and y location
maze = turtle.Turtle()
maze.shape("square")            # the turtle shape
maze.color("white")             # colour of the turtle
maze.penup()                    # lift up the pen so it do not leave a trail
maze.speed(0)                   # sets the speed that the maze is written to the screen
# enable the maze class
sprite = sprite()
end = turtle.Turtle() # enable the sprite  class
end.shape("square")
end.color("green")
end.penup()
end.speed(0)
walls =[]                    # create walls coordinate list
finish = []                  # enable the finish array
grid = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
  ]
ends = (len(grid)-1, len(grid[0])-1)
setupMaze(grid)              # call the setup maze function
