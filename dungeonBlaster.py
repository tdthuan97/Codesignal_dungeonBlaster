def dungeonBlaster(m):
    startRow, startCol = -1,-1
    for i in range(len(m)):
        if "*" in m[i]:
            startRow = i
            startCol = m[i].find("*")
    stack = [[startRow,startCol]]
    visited = [[startRow,startCol]]
    key = []
    door = {}
    while len(stack) != 0:
        s = stack.pop()
        r,c = s[0],s[1]
        up,left,right,down = r - 1,c - 1,c + 1,r + 1
        if up == -1:
            up = len(m) - 1
        if left == -1:
            left = len(m[0]) - 1
        if right == len(m[0]):
            right = 0
        if down == len(m):
            down = 0
        if "^" in [m[up][c],m[r][left],m[r][right],m[down][c]]:
            return True
        if m[up][c] != "#" and [up,c] not in visited:
            if m[up][c].islower() or m[up][c] == " ":
                if m[up][c].islower():# see key
                    key.append(m[up][c])# save key
                    if m[up][c].upper() in door:# check if key in door (see door before key, so open door saw before)
                        stack.append(door[m[up][c].upper()])# add door position into stack 
                        visited.append(door[m[up][c].upper()])# set at door position visited
                stack.append([up,c])
                visited.append([up,c])                
            if m[up][c].isupper():# check if see door
                door[m[up][c]] = [up,c]# save key = door with value = position of door
                if m[up][c].lower() in key:# check if door in key (see key before door)
                    stack.append([up,c])# open door and save position of door
                    visited.append([up,c])# ...
                
        if m[r][left] != "#" and [r,left] not in visited:
            if m[r][left].islower() or m[r][left] == " ":
                if m[r][left].islower():
                    key.append(m[r][left])
                    if m[r][left].upper() in door:
                        stack.append(door[ m[r][left].upper() ])
                        visited.append(door[ m[r][left].upper() ])
                stack.append([r,left])
                visited.append([r,left])
            if m[r][left].isupper():
                door[m[r][left]] = [r,left]
                if m[r][left].lower() in key:
                    stack.append([r,left])
                    visited.append([r,left])
        
        if m[r][right] != "#" and [r,right] not in visited:
            if m[r][right].islower() or m[r][right] == " ":
                if m[r][right].islower():
                    key.append(m[r][right])
                    if m[r][right].upper() in door:
                        stack.append(door[ m[r][right].upper() ])
                        visited.append(door[ m[r][right].upper() ])
                stack.append([r,right])
                visited.append([r,right])
            if m[r][right].isupper():
                door[m[r][right]] = [r,right]
                if m[r][right].lower() in key:
                    stack.append([r,right])
                    visited.append([r,right])
        
        if m[down][c] != "#" and [down,c] not in visited:
            if m[down][c].islower() or m[down][c] == " ":
                if m[down][c].islower():
                    key.append(m[down][c])
                    if m[down][c].upper() in door:
                        stack.append(door[m[down][c].upper()])
                        visited.append(door[m[down][c].upper()])
                stack.append([down,c])
                visited.append([down,c])
            if m[down][c].isupper():
                door[m[down][c]] = [down,c]
                if m[down][c].lower() in key:
                    stack.append([down,c])
                    visited.append([down,c])
        
    return False
