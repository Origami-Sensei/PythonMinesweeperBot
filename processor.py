from PIL import ImageGrab


def getImage():
    px = ImageGrab.grab().load()
    return px


def ProcessImage(pixels):
    TopLeft = (23, 251)

    size = (16, 30)
    grid = []
    row = []
    for x in range(size[0]):
        for y in range(size[1]):

            pixel = pixels[TopLeft[0] + (20 * y), TopLeft[1] + (20 * x)]

            pixelAvg = round((pixel[0] + pixel[1] + pixel[2]) / 3)

            if pixelAvg == 23:
                row.append(9)
            elif pixelAvg == 189:
                upperPixel = pixels[TopLeft[0] + (20 * y) - 9, TopLeft[1] + (20 * x)]
                if upperPixel[0] == 255:
                    row.append(9)
                else:
                    row.append(0)
            elif pixelAvg == 85 and pixel[0] < pixel[2]:
                row.append(1)
            elif pixelAvg == 58 or pixelAvg ==54:
                row.append(2)
            elif pixelAvg == 85 and pixel[0] > pixel[2]:
                row.append(3)
            elif pixelAvg == 41 and pixel[0] < pixel[2]:
                row.append(4)
            elif pixelAvg == 41 and pixel[0] > pixel[2]:
                row.append(5)
            elif pixelAvg == 82:
                row.append(6)
            else:
                row.append(pixelAvg)
        grid.append(row)
        row = []

    return grid



