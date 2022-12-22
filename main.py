import pyautogui

from processor import *


def getSpaces(grid, x, y):
    spaces = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == 0 and i == 0:
                pass
            else:
                try:
                    if y+j >=0 and x+i>=0:
                        spaces.append(grid[y + j][x + i])
                except:
                    pass
    return spaces




def flagAllEmpty(grid, y, x):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == 0 and i == 0:
                pass
            else:
                try:
                    if grid[y + j][x + i] == 9:
                        grid[y + j][x + i] = "F"
                except:
                    pass
    return grid

def clickAllEmpty(grid, y, x):
    TopLeft = (23, 251)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == 0 and i == 0:
                pass
            else:
                try:
                    if grid[y + j][x + i] == 9:
                        pyautogui.click(x= TopLeft[0]+((x+i)*20), y=TopLeft[1]+((y+j)*20))
                except:
                    pass

totalMines = 99
image = getImage()

grid = ProcessImage(image)


while totalMines != 0:
    print(totalMines)
    oldGrid = grid
    image = getImage()

    grid = ProcessImage(image)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if oldGrid[i][j] =="F":
                grid[i][j] ="F"


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0 and grid[i][j] != 9 and grid[i][j] != "F":

                spaces = getSpaces(grid, j, i)
                flags = 0
                empty = 0
                for k in range(len(spaces)):
                    if spaces[k] == "F":
                        flags += 1
                    elif spaces[k] == 9:
                        empty += 1
                if grid[i][j] == flags+empty and empty >0:
                    grid = flagAllEmpty(grid, i, j)
                    totalMines = totalMines - empty


                elif grid[i][j] == flags:
                    clickAllEmpty(grid,i,j)
