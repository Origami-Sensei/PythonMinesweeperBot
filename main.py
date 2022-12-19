from PIL import ImageGrab
import time
import pyautogui
import math

input()
pyautogui.moveTo(489, 581)
pyautogui.click()
time.sleep(0.5)


def check():
    px = ImageGrab.grab().load()
    startx = 266
    starty = 448
    data = []
    for i in range(0, 8):
        finaly = starty + 46.325 * i
        line = ""
        for j in range(0, 10):
            finalx = startx + (45.5 * j)

            totalR = 0
            totalG = 0
            totalB = 0
            for x in range(-4, 4):
                for y in range(-4, 4):
                    col = px[finalx + x, finaly + y]
                    totalR += col[0]
                    totalG += col[1]
                    totalB += col[2]

            totalR = round(totalR / 81)
            totalG = round(totalG / 81)
            totalB = round(totalB / 81)
            color = (totalR, totalG, totalB)

            if color[0] > 65 and color[0] < 105 and color[2] > 100:
                line += ("1")
            elif color[0] == 229 or color[0] == 215:
                line += ("E")
            elif color[0] >= 100 and color[0] < 160 and color[1] < 130:
                line += "4"
            elif color[0] >= 85 and color[0] < 150 and color[1] < 145:
                line += "2"
            elif color[1] > 140 and color[2] < 100:
                line += "G"
            elif color[0] > 160 and color[0] < 180 and color[2] < 110:
                line += "3"
            else:
                line += ("U")
        data.append(list(line))
    return data


def cycle(values):
    for a in range(len(values)):
        for b in range(len(values[a])):
            location = values[a][b]
            try:
                location = int(location)
                total = 0
                shape = []
                for c in range(-1, 2):
                    row = []
                    for d in range(-1, 2):
                        try:
                            data = values[a + c][b + d]
                            row.append(data)
                            if c == 0 and d == 0:
                                pass
                            else:
                                if data == "G" or data == "F":
                                    total += 1
                        except:

                            pass
                    shape.append(row)
                # print("****")
                # print(shape)
                # print(location,total)
                if location == total:
                    # print("POG")
                    for c in range(-1, 2):
                        for d in range(-1, 2):
                            try:
                                data = values[a + c][b + d]
                                if data == "G":
                                    values[a + c][b + d] = "F"
                                    # print("CRINGE")
                            except:
                                pass
            except:
                pass

    for a in range(len(values)):
        for b in range(len(values[a])):
            location = values[a][b]
            try:
                location = int(location)
                # print("value:",location,"is an interger")
                total = 0
                shape = []
                for c in range(-1, 2):
                    row = []
                    for d in range(-1, 2):
                        try:
                            data = values[a + c][b + d]
                            # print(a+c,",",b+d, location)
                            row.append(data)
                            if c == 0 and d == 0:
                                pass
                            else:
                                if data == "F":
                                    total += 1
                        except:

                            pass
                    shape.append(row)
                # print("****")
                # print(shape)
                # print(location,total)
                if location == total:
                    # print("POG")
                    for c in range(-1, 2):
                        for d in range(-1, 2):
                            try:
                                x = math.sqrt(a + c) + math.sqrt(b + d)
                                data = values[a + c][b + d]
                                if data == "G":
                                    values[a + c][b + d] = "C"
                                    startx = 266
                                    starty = 448
                                    ypos = starty + 46.325 * (a + c)
                                    xpos = startx + 45.5 * (b + d)
                                    pyautogui.moveTo(xpos, ypos)
                                    pyautogui.click()
                                # print("CRINGE")
                            except:
                                pass
            except:
                pass
    return values


NoGreen = False
# 467 691
while True:
    NoGreen = False

    while not NoGreen:
        values = check()
        # print("*"*20)
        # for c in values:
        #    print(c)
        # input()
        values = cycle(values)
        NoGreen = True
        for t in range(len(values)):
            for s in range(len(values[t])):
                if values[t][s] == "G":
                    NoGreen = False
    print("finished")
    pyautogui.moveTo(467, 691)
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()
