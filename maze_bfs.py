def main(maze):
    queue = [(0, 0)] # use a local variable, not a member
    visited = {} # use a dict, key = coordinate-tuples, value = previous location
    visited[(0, 0)] = (-1, -1)
    end_r, end_c = len(maze), len(maze[0])
    end = (end_r-1, end_c-1)
    while len(queue) > 0: # don't use running as variable
        # no need to use current; just reuse r and c:
        r, c = queue.pop(0) # you can remove immediately from queue
        if (r, c) == end:
            return True
            # build path from walking backwards through the visited information
            # path = []
            # while r != -1:
            #     path.append((r, c))
            #     r, c = visited[(r, c)]
            # path.reverse()
            # return path
        # avoid repetition of code: make a loop
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            new_r = r + dy
            new_c = c + dx
            if (-1 < new_r < end_r) and (-1 < new_c < end_c) and not (new_r, new_c) in visited and maze[new_r][new_c] == 0:
                visited[(new_r, new_c)] = (r, c)
                queue.append((new_r, new_c))
    return False
 
maze = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
  ]
 
print(main(maze))
 
maze = [
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1]
  ]
  
print(main(maze))
 
maze = [
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
  ]
  
print(main(maze))
 
maze = [
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
  ]
  
print(main(maze))
