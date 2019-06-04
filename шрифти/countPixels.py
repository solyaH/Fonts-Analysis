def GeneralBlackPixels(picture):
    black=0
    pixels = list(picture.getdata())
    for pixel in pixels:
        if pixel==(0, 0, 0):
            black+=1
    return (black/25)

def LeftBlackPixels(picture):
    black=0
    pixels = picture.load()
    for i in range(25):
        for j in range(50):
                if pixels[i,j]==(0, 0, 0):
                    black+=1
    return (black/12.5)

def RightBlackPixels(picture):
    black=0
    pixels = picture.load()
    for i in range(25,50):
        for j in range(50):
                if pixels[i,j]==(0, 0, 0):
                    black+=1
    return (black/12.5)

def UpBlackPixels(picture):
    black=0
    pixels = picture.load()
    for i in range(50):
        for j in range(25):
                if pixels[i,j]==(0, 0, 0):
                    black+=1
    return black

def DownBlackPixels(picture):
    black=0
    pixels = picture.load()
    for i in range(50):
        for j in range(25,50):
                if pixels[i,j]==(0, 0, 0):
                    black+=1
    return (black/12.5)
