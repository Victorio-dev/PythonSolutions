
grid = ["" for _ in range(9)]

for case in range(int(input())):
    i = 0
    for _ in range(3):
        for cell in input():
            grid[i] = cell
            i += 1
            
    try: input()
    except: pass # No empty lne after test case
    
    wins = {
        "O": False,
        "X": False,
        ".": None
    }
    
    # Horiz
    for i in range(0, 7, 3):
        if grid[i]==grid[i+1]==grid[i+2]:
            wins[grid[i]] = True
            
    # Vertical
    for i in range(3):
        if grid[i]==grid[i+3]==grid[i+6]:
            wins[grid[i]] = True
            
    # Diag
    if grid[0]==grid[4]==grid[8]:
        wins[grid[0]] = True
    
    if grid[2]==grid[4]==grid[6]:
        wins[grid[2]] = True
    
    # X wins
    if wins["X"] and not wins["O"] and grid.count("X")==grid.count("O")+1:
        print("yes")
        
    # X loses
    elif not wins["X"] and wins["O"] and grid.count("X")==grid.count("O"):
        print("yes")

    # Undecided
    elif wins["X"]==wins["O"]==False and 0<=grid.count("X")-grid.count("O")<=1:
        print("yes")
    
    else:
        print("no")