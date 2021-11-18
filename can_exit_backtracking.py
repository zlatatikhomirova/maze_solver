import turtle

def can_exit(grid: list) -> bool:
  """
  0 пустая клетка
  1 стена
  2 финиш
  7 в этой клетке уже были
  """
  ends = (len(grid)-1, len(grid[0])-1)
  def search(r: int, c: int):
      if grid[r][c] == 1 or grid[r][c] == 7:
          return False
      if (r, c) == ends:
          return True
      grid[r][c] = 7
      if     ((r < ends[0] and search(r+1, c))
          or (c > 0 and search(r, c-1))
          or (r > 0 and search(r-1, c))
          or (c < ends[1] and search(r, c+1))):
          return True
      return False
  return search(0, 0)

def draw_maze(grid: list) -> bool:
  """
  0 пустая клетка
  1 стена
  2 финиш
  7 в этой клетке уже были
  """
  wn = turtle.Screen()              
  wn.bgcolor("black")               
  wn.setup(1300,700) 

  maze = turtle.Turtle()
  maze.shape("square")           
  maze.penup()                   
  maze.speed(3)

  joe = turtle.Turtle()
  joe.color("blue")
  joe.shape("circle")
  joe.speed(2)
  joe.penup()

  for y in range(len(grid)):                       
      for x in range(len(grid[0])):                
          character = grid[y][x]                   
          screen_x = -650 + 24 + x * 24          
          screen_y = 350 - 24 - y * 24       

          if character == 1:     
              maze.color("green")                
              maze.goto(screen_x, screen_y)        
              maze.stamp()
          else:
              maze.goto(screen_x, screen_y) 
              maze.color("yellow")
              maze.stamp()                        


          if (x, y) == (0, 0):                     
              joe.goto(screen_x, screen_y)

  ends = (len(grid)-1, len(grid[0])-1)
  def search(r: int, c: int):
      if grid[r][c] == 1 or grid[r][c] == 7:
          return False
      if (r, c) == ends:
          joe.goto(-650 + 24 + c * 24, 350 - 24 - r * 24)
          return True
      grid[r][c] = 7
      if     ((r < ends[0] and search(r+1, c))
          or (c > 0 and search(r, c-1))
          or (r > 0 and search(r-1, c))
          or (c < ends[1] and search(r, c+1))):
          joe.goto(-650 + 24 + c * 24, 350 - 24 - r * 24)
          return True
      return False
  return search(0, 0)

draw_maze([
         [0, 1, 1, 1, 1, 1, 1],
         [0, 0, 1, 1, 0, 1, 1],
         [1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0, 0]
        ])

assert can_exit([
                 [0, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 0, 1, 1],
                 [1, 0, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 0, 0, 1],
                 [1, 1, 1, 1, 1, 0, 0]
                ]) == True, "Test 1. WA."
 
assert can_exit([
                 [0, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 1, 1],
                 [1, 1, 0, 1, 0, 0, 1],
                 [1, 1, 0, 0, 1, 1, 1]
               ]) == False, "Test 2. WA."

assert can_exit([
                 [0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [1, 1, 1, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1, 1, 1]
                ]) == False, "Test 3. WA."
 
assert can_exit([
                 [0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 1, 0],
                 [1, 1, 1, 1, 1, 1, 0]
                ]) == True, "Test 4. WA."
