import turtle 

def can_exit(grid: list) -> bool:
        queue = [(0, 0)] 
        visited = {} 
        visited[(0, 0)] = (-1, -1)
        end_r, end_c = len(grid), len(grid[0])
        ends = (end_r-1, end_c-1)
        while len(queue) > 0: 
            r, c = queue.pop()
            if (r, c) == ends:
                return True
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                new_r = r + dy
                new_c = c + dx
                if (-1 < new_r < end_r) and (-1 < new_c < end_c) and not ((new_r, new_c) in visited or grid[new_r][new_c]):
                    visited[(new_r, new_c)] = (r, c)
                    queue.append((new_r, new_c))
        return False
    
def draw_maze(grid: list):
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
                
    
    queue = [(0, 0)] 
    visited = {} 
    visited[(0, 0)] = (-1, -1)
    end_r, end_c = len(grid), len(grid[0])
    ends = (end_r-1, end_c-1)
    while len(queue) > 0: 
        r, c = queue.pop()
        if (r, c) == ends:
            joe.goto(-650 + 24 + c * 24, 350 - 24 - r * 24)
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            new_r = r + dy
            new_c = c + dx
            if (-1 < new_r < end_r) and (-1 < new_c < end_c) and not ((new_r, new_c) in visited or grid[new_r][new_c]):
                visited[(new_r, new_c)] = (r, c)
                joe.goto(-650 + 24 + c * 24, 350 - 24 - r * 24)
                queue.append((new_r, new_c))  


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
