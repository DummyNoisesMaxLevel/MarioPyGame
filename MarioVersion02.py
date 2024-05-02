'''These lines are at the top of our main project'''
import pygame
import sys
from pygame import mixer  # Load the popular external library

mixer.init()

global death
death = False

playMainMusic = False
playJumpingSound = False
playCoinSound = False
playDeathSound = False

if playMainMusic:
    mainMusic = pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
if playJumpingSound:
    jumpingSound = pygame.mixer.Sound("jump.mp3")
if playCoinSound:
    coinSound = pygame.mixer.Sound("coin.mp3")

def playDeathSoundFunction():
    if playDeathSound:
        pygame.mixer.music.load("death.mp3")
        pygame.mixer.music.play()

def onDeath():
    global death
    playDeathSoundFunction()
    death = True
    

pygame.init()


screenWidth = 1920
screenHeight = 1080
global groundHeight
groundHeight = screenHeight - 64*3
global marioX
marioX = 512
global marioY
marioY = groundHeight - 64
global offsetX
offsetX = 0
global offsetY
offsetY = 0
global realMarioX
realMarioX = marioX

window = pygame.display.set_mode([screenWidth, screenHeight])
window.fill((100, 149, 237))
pygame.display.set_caption("Mario Remake") # Comment out this line if you are using TechSmart
pygame.display.flip()




pygame.display.flip()

global blockPositions
blockPositions = []


global brickMap
brickMap = [[512+64 * 11, groundHeight - 64*4, [False, 0, 0], 4], [512+64 * 13, groundHeight - 64*4, [False, 0, 0], 4], [512+64 * 15, groundHeight - 64*4, [False, 0, 0], 4],
           [960 + 64 * 44,  groundHeight - 64 * 5, [False, 0, 0], 4], [960 + 64 * 45,  groundHeight - 64 * 5, [False, 0, 0], 4], [512+64 * 63, groundHeight - 64*3, [False, 0, 0], 4],
           [512+64 * 64, groundHeight - 64*3, [False, 0, 0], 4], [512+64 * 65, groundHeight - 64*3, [False, 0, 0], 4], [512+64 * 68, groundHeight - 64*6, [False, 0, 0], 4],
           [512+64 * 69, groundHeight - 64*6, [False, 0, 0], 4], [512+64 * 70, groundHeight - 64*6, [False, 0, 0], 4], [512+64 * 65, groundHeight - 64*9, [False, 0, 0], 4],
           [512+64 * 64, groundHeight - 64*9, [False, 0, 0], 4], [512+64 * 63, groundHeight - 64*9, [False, 0, 0], 4], [512+64 * 62, groundHeight - 64*9, [False, 0, 0], 4],
           [512+64 * 61, groundHeight - 64*9, [False, 0, 0], 4], [512+64 * 60, groundHeight - 64*9, [False, 0, 0], 4], [512+64 * 59, groundHeight - 64*9, [False, 0, 0], 4], [512+ 64*58, groundHeight - 64*9, [False, 0, 0], 4], [512+ 64*58, groundHeight - 64*10, [False, 0, 0], 4],
           [512+64 * 59, groundHeight - 64*13, [False, 0, 0], 4], [512+64 * 61, groundHeight - 64*13, [False, 0, 0], 4], [512+64 * 63, groundHeight - 64*13, [False, 0, 0], 4],
           [512+64 * 65, groundHeight - 64*13, [False, 0, 0], 4]]
'''b'''
global luckyBlockMap
luckyBlockMap = [[512+64 * 7, groundHeight - 64*4, [False, 0, 0], 4], [512+64 * 12, groundHeight - 64*4, [False, 0, 0], 4], [512+64 * 14, groundHeight - 64*4, [False, 0, 0], 4],
                [512+64 * 13, groundHeight - 64*8, [False, 0, 0], 4], [512+64 * 50, groundHeight - 64*5, [False, 0, 0], 4], [512+64 * 53, groundHeight - 64*5, [False, 0, 0], 4],
                [960 + 64 * 31,  groundHeight - 64 * 7, [False, 0, 0], 4], [512+64 * 60, groundHeight - 64*13, [False, 0, 0], 4], [512+64 * 62, groundHeight - 64*13, [False, 0, 0], 4],
                [512+64 * 64, groundHeight - 64*13, [False, 0, 0], 4]]
'''lb'''
global hitLuckyBlockMap
hitLuckyBlockMap = []
'''hlb'''
global goombaMap
goombaMap = [[960 + 64 * 30,  groundHeight - 64 * 1], [960 + 64 * 32,  groundHeight - 64 * 1], [512+64 * 60, groundHeight - 64*10], [512+64 * 63, groundHeight - 64*10], [512+64 * 69, groundHeight - 64*7]]
'''g'''
global coinMap
coinMap = []
'''c'''
global stairsBlockMap
stairsBlockMap = [[960 + 64 * 26,  groundHeight - 64 * 1], [960 + 64 * 27,  groundHeight - 64 * 1], [960 + 64 * 28,  groundHeight - 64 * 1],
                 [960 + 64 * 29,  groundHeight - 64 * 1], [960 + 64 * 29,  groundHeight - 64 * 2], [960 + 64 * 28,  groundHeight - 64 * 2],
                 [960 + 64 * 27,  groundHeight - 64 * 2], [960 + 64 * 28,  groundHeight - 64 * 3], [960 + 64 * 29,  groundHeight - 64 * 3],
                 [960 + 64 * 29,  groundHeight - 64 * 4], [960 + 64 * 33,  groundHeight - 64 * 4], [960 + 64 * 33,  groundHeight - 64 * 3],
                 [960 + 64 * 34,  groundHeight - 64 * 3], [960 + 64 * 33,  groundHeight - 64 * 2], [960 + 64 * 34,  groundHeight - 64 * 2],
                 [960 + 64 * 35,  groundHeight - 64 * 2], [960 + 64 * 33,  groundHeight - 64 * 1], [960 + 64 * 34,  groundHeight - 64 * 1],
                 [960 + 64 * 35,  groundHeight - 64 * 1], [960 + 64 * 36,  groundHeight - 64 * 1], [960 + 64 * 43,  groundHeight - 64 * 1],
                 [960 + 64 * 44,  groundHeight - 64 * 1], [960 + 64 * 45,  groundHeight - 64 * 1], [960 + 64 * 46,  groundHeight - 64 * 1],
                 ]

'''sb'''
def drawArrayIntoSurface(data, multiplier=4, stack=1):
    surface = pygame.Surface((len(data[0])*multiplier, len(data)*multiplier*stack))
    def drawPixel(surface, horizontalNum, verticalNum, color):
        pixelWidth = multiplier
        middle = 8 * pixelWidth
        
        if horizontalNum <= 7:
            x = int( middle - (8 - horizontalNum) * pixelWidth)
        else:
            x = int( middle + (horizontalNum - 8) * pixelWidth)
        if verticalNum <= 7:
            y = int( middle - (8 - verticalNum) * pixelWidth)
        else:
            y = int( middle + (verticalNum - 8) * pixelWidth)
        for i in range(stack):    
            pixel = pygame.Rect(x, y, pixelWidth, pixelWidth)
            pygame.draw.rect(surface, color, pixel)
            y += 16 * multiplier
    
    colorMap = {"0":(255,255,255),"1":(0,0,0),"2":(255,255,0),"3":(100, 149, 237),"4":(255,204,0),"5":(218,165,32),"6":(184,134,11),"7":(245,222,179),"8":(128,70,27),"9":(205,127,50),"10":(128,128,0),"11":(220,20,60),"12":(255, 200, 195)}
    for i in range(len(data)):
        for j in range(len(data[i])):
            rawColor = data[i][j]
            color = colorMap[str(rawColor)]
            drawPixel(surface, j, i, color)
    return surface
#Initialize
global stairsBlockSurface
stairsBlockSurface = drawArrayIntoSurface([
            [8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1],
            [12, 8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1, 1],
            [12, 12, 8, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1, 1, 1],
            [12, 12, 12, 8, 12, 12, 12, 12, 12, 12, 12, 12, 1, 1, 1, 1],
            [12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1],
            [12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1],
            [12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1],
            [12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1],
            [12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1],
            [12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1],
            [12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1],
            [12, 12, 12, 12, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1],
            [12, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
            [12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1],
            [12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8]        
])

global luckyBlockSurface
luckyBlockSurface = drawArrayIntoSurface([
            [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1],
            [4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [4, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [4, 2, 2, 2, 2, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 1],
            [4, 2, 2, 2, 4, 4, 1, 1, 1, 4, 4, 2, 2, 2, 2, 1],
            [4, 2, 2, 2, 4, 4, 1, 2, 2, 4, 4, 1, 2, 2, 2, 1],
            [4, 2, 2, 2, 4, 4, 1, 2, 2, 4, 4, 1, 2, 2, 2, 1],
            [4, 2, 2, 2, 2, 1, 1, 2, 4, 4, 4, 1, 2, 2, 2, 1],
            [4, 2, 2, 2, 2, 2, 2, 4, 4, 1, 1, 1, 2, 2, 2, 1],
            [4, 2, 2, 2, 2, 2, 2, 4, 4, 1, 2, 2, 2, 2, 2, 1],
            [4, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1],
            [4, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 1],
            [4, 2, 2, 2, 2, 2, 2, 4, 4, 1, 2, 2, 2, 2, 2, 1],
            [4, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1],
            [4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])


pygame.display.flip()
global hitLuckyBlockSurface
hitLuckyBlockSurface = drawArrayIntoSurface([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 8, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 1],
            [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]        
])




pygame.display.flip()
global goombaSurface1
goombaSurface1 = drawArrayIntoSurface([
            [3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 3, 3, 3, 3],
            [3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 3, 3],
            [3, 3, 8, 1, 1, 8, 8, 8, 8, 8, 8, 1, 1, 8, 3, 3],
            [3, 8, 8, 8, 7, 1, 8, 8, 8, 8, 1, 7, 8, 8, 8, 3],
            [3, 8, 8, 8, 7, 1, 8, 8, 8, 8, 1, 7, 8, 8, 8, 3],
            [8, 8, 8, 8, 7, 1, 7, 8, 8, 7, 1, 7, 8, 8, 8, 8],
            [8, 8, 8, 8, 7, 7, 7, 8, 8, 7, 7, 7, 8, 8, 8, 8],
            [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
            [3, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 3],
            [3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 3, 3, 3, 3],
            [3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 3, 3],
            [3, 3, 3, 1, 1, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 3],
            [3, 3, 3, 1, 1, 1, 7, 3, 3, 1, 1, 1, 1, 1, 1, 3],
            [3, 3, 3, 3, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 3, 3]      
])

pygame.display.flip()
global goombaSurface2
goombaSurface2 = drawArrayIntoSurface([
            [3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 3, 3, 3, 3],
            [3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 3, 3],
            [3, 3, 8, 1, 1, 8, 8, 8, 8, 8, 8, 1, 1, 8, 3, 3],
            [3, 8, 8, 8, 7, 1, 8, 8, 8, 8, 1, 7, 8, 8, 8, 3],
            [3, 8, 8, 8, 7, 1, 8, 8, 8, 8, 1, 7, 8, 8, 8, 3],
            [8, 8, 8, 8, 7, 1, 7, 8, 8, 7, 1, 7, 8, 8, 8, 8],
            [8, 8, 8, 8, 7, 7, 7, 8, 8, 7, 7, 7, 8, 8, 8, 8],
            [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
            [3, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 3],
            [3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 3, 3, 3, 3],
            [3, 3, 1, 1, 7, 7, 7, 7, 7, 7, 7, 7, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 7, 7, 7, 7, 7, 1, 1, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 3, 3, 7, 1, 1, 1, 3, 3, 3],
            [3, 3, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 3, 3, 3, 3]      
])


pygame.display.flip()

global groundBrickSurface
groundBrickSurface = drawArrayIntoSurface(data=[
            [9, 7, 7, 7, 7, 7, 7, 7, 7, 1, 9, 7, 7, 7, 7, 9],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 1],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 1],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 1],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 7, 1, 9, 9, 9, 1],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 1, 1, 1, 1, 9],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 7, 7, 7, 7, 7, 1],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 1],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 1],
            [7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 1],
            [1, 1, 9, 9, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 9, 1],
            [7, 7, 1, 1, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 9, 1],
            [7, 9, 7, 7, 1, 1, 1, 1, 7, 9, 9, 9, 9, 9, 9, 1],
            [7, 9, 9, 9, 7, 7, 7, 1, 7, 9, 9, 9, 9, 9, 9, 1],
            [7, 9, 9, 9, 9, 9, 9, 1, 7, 9, 9, 9, 9, 9, 1, 1],
            [9, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 9]         
], stack=3)


pygame.display.flip()
global brickSurface
brickSurface = drawArrayIntoSurface([
            [8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1],
            [8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1],
            [8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8],
            [8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8],
            [8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1],
            [8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1],
            [8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8],
            [8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8],
            [8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  
])
pygame.display.flip()
global deadMarioSurface
deadMarioSurface = drawArrayIntoSurface([
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3,11,11,11,11, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 4, 3,11,11,11,11,11,11, 3, 4, 3, 3, 3],
            [3, 4, 4, 4,10, 4,10, 4, 4,10, 4,10, 4, 4, 4, 3],
            [3, 4, 4,10,10, 4,10, 4, 4,10, 4,10,10, 4, 4, 3],
            [3, 4, 4,10,10,10, 4, 4, 4, 4,10,10,10, 4, 4, 3],
            [3, 3, 3,10,10,10,10, 4, 4,10,10,10,10, 3, 3, 3],
            [3, 3, 3, 3,10, 4,10,10,10,10, 4,10, 3, 3, 3, 3],
            [3, 3, 3, 3,10, 4, 4, 4, 4, 4, 4,10, 3, 3, 3, 3],
            [3, 3, 3,11,11,11, 4, 4, 4, 4,11,11,11, 3, 3, 3],
            [3, 3,10,10,11,11,10,10,10,10,11,11,10,10, 3, 3],
            [3, 3,10,10,10,11,11,10,10,11,11,10,10,10, 3, 3],
            [3, 3,10,10,10,11, 4,11,11, 4,11,10,10,10, 3, 3],
            [3, 3,10,10,10,11,11,11,11,11,11,10,10,10, 3, 3],
            [3, 3, 3, 3,10,11,11,11,11,11,11,10, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]         
])

pygame.display.flip()
global marioSurface
marioData = [
            [3, 3, 3, 3, 3,11,11,11,11,11, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3,11,11,11,11,11,11,11,11,11, 3, 3, 3],
            [3, 3, 3, 3,10,10,10, 4, 4,10, 4, 3, 3, 3, 3, 3],
            [3, 3, 3,10, 4,10, 4, 4, 4,10, 4, 4, 4, 3, 3, 3],
            [3, 3, 3,10, 4,10,10, 4, 4, 4,10, 4, 4, 4, 3, 3],
            [3, 3, 3,10,10, 4, 4, 4, 4,10,10,10, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3],
            [3, 3, 3, 3,10,10,11,10,10,10, 3, 3, 3, 3, 3, 3],
            [3, 3, 3,10,10,10,11,10,10,11,10,10,10, 3, 3, 3],
            [3, 3,10,10,10,10,11,11,11,11,10,10,10,10, 3, 3],
            [3, 3, 4, 4,10,11, 4,11,11, 4,11,10, 4, 4, 3, 3],
            [3, 3, 4, 4, 4,11,11,11,11,11,11, 4, 4, 4, 3, 3],
            [3, 3, 4, 4,11,11,11, 3, 3,11,11,11, 4, 4, 3, 3],
            [3, 3, 3, 3,11,11,11, 3, 3,11,11,11, 3, 3, 3, 3],
            [3, 3, 3,10,10,10, 3, 3, 3, 3,10,10,10, 3, 3, 3],
            [3, 3,10,10,10,10, 3, 3, 3, 3,10,10,10,10, 3, 3]         
]
marioSurface = drawArrayIntoSurface(marioData)
global backwardsMarioSurface
backwardsMarioData = []
for row in marioData:
    backwardsMarioData.append(row[::-1])
backwardsMarioSurface = drawArrayIntoSurface(backwardsMarioData)

global runningMario1Surface
runningMario1Data = [
            [3, 3, 3, 3, 3,11,11,11,11,11, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3,11,11,11,11,11,11,11,11,11, 3, 3, 3],
            [3, 3, 3, 3,10,10,10, 4, 4,10, 4, 3, 3, 3, 3, 3],
            [3, 3, 3,10, 4,10, 4, 4, 4,10, 4, 4, 4, 3, 3, 3],
            [3, 3, 3,10, 4,10,10, 4, 4, 4,10, 4, 4, 4, 3, 3],
            [3, 3, 3,10,10, 4, 4, 4, 4,10,10,10,10, 3, 3, 3],
            [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3,10,10,11,11,10, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3,10,10,10,10,11,10, 4, 4, 3, 3, 3],
            [3, 3, 3, 4, 4,10,10,10,10,10,10, 4, 4, 4, 3, 3],
            [3, 3, 4, 4, 4,11,10,10,10,10,10, 4, 4, 3, 3, 3],
            [3, 3, 3,10,10,11,11,11,11,11,11,11, 3, 3, 3, 3],
            [3, 3, 3,10,11,11,11,11,11,11,11,11, 3, 3, 3, 3],
            [3, 3,10,10,11,11, 3, 3,11,11,11, 3, 3, 3, 3, 3],
            [3, 3,10, 3, 3, 3, 3,10,10,10, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3,10,10,10, 3, 3, 3, 3, 3]         
] 
runningMario1Surface = drawArrayIntoSurface(runningMario1Data)
global backwardsRunningMario1Surface
backwardsRunningMario1Data = []
for row in runningMario1Data:
    backwardsRunningMario1Data.append(row[::-1])
backwardsRunningMario1Surface = drawArrayIntoSurface(backwardsRunningMario1Data)

global runningMario2Surface
runningMario2Data = [
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3,11,11,11,11,11, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3,11,11,11,11,11,11,11,11,11, 3, 3, 3, 3],
            [3, 3, 3,10,10,10, 4, 4,10, 4, 3, 3, 3, 3, 3, 3],
            [3, 3,10, 4,10, 4, 4, 4,10, 4, 4, 4, 3, 3, 3, 3],
            [3, 3,10, 4,10,10, 4, 4, 4,10, 4, 4, 4, 3, 3, 3],
            [3, 3,10,10, 4, 4, 4, 4,10,10,10,10, 3, 3, 3, 3],
            [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3],
            [3, 3, 3,10,10,10,11,10,10, 3, 3, 3, 3, 3, 3, 3],
            [3, 3,10,10,10,10,11,11,10,10, 3, 3, 3, 3, 3, 3],
            [3, 3,10,10,10,11,11, 4,11,11, 3, 3, 3, 3, 3, 3],
            [3, 3,10,10,10,10,11,11,11,11, 3, 3, 3, 3, 3, 3],
            [3, 3,11,10,10, 4, 4,11,11,11, 3, 3, 3, 3, 3, 3],
            [3, 3, 3,11,10, 4, 4,11,11, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3,11,11,11,10,10,10, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3,10,10,10,10, 3, 3, 3, 3, 3, 3, 3, 3]         
] 
runningMario2Surface = drawArrayIntoSurface(runningMario2Data)
global backwardsRunningMario2Surface
backwardsRunningMario2Data = []
for row in runningMario2Data:
    backwardsRunningMario2Data.append(row[::-1])
backwardsRunningMario2Surface = drawArrayIntoSurface(backwardsRunningMario2Data)

global runningMario3Surface
runningMario3Data = [
            [3, 3, 3, 3, 3,11,11,11,11,11, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3,11,11,11,11,11,11,11,11,11, 3, 3, 3],
            [3, 3, 3, 3,10,10,10, 4, 4,10, 4, 3, 3, 3, 3, 3],
            [3, 3, 3,10, 4,10, 4, 4, 4,10, 4, 4, 4, 3, 3, 3],
            [3, 3, 3,10, 4,10,10, 4, 4, 4,10, 4, 4, 4, 3, 3],
            [3, 3, 3,10,10, 4, 4, 4, 4,10,10,10,10, 3, 3, 3],
            [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3],
            [3, 3,10,10,10,10,11,10,10,10,11, 3, 3, 3, 3, 3],
            [4, 4,10,10,10,10,11,11,10,10,10,11,10, 4, 4, 4],
            [4, 4, 4, 3,10,10,11,11,11,11,11,11,10,10, 4, 4],
            [4, 4, 3, 3,11,11,11, 4,11,11,11, 4, 3, 3,10, 3],
            [3, 3, 3,11,11,11,11,11,11,11,11,11,11,10,10, 3],
            [3, 3,11,11,11,11,11,11,11,11,11,11,11,10,10, 3],
            [3,10,10,11,11,11, 3, 3, 3, 3,11,11,11,10,10, 3],
            [3,10,10,10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3,10,10,10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]         
]
runningMario3Surface = drawArrayIntoSurface(runningMario3Data)
global backwardsRunningMario3Surface
backwardsRunningMario3Data = []
for row in runningMario3Data:
    backwardsRunningMario3Data.append(row[::-1])
backwardsRunningMario3Surface = drawArrayIntoSurface(backwardsRunningMario3Data)


global jumpingMarioSurface
jumpingMarioData = [
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4],
            [3, 3, 3, 3, 3, 3,11,11,11,11,11, 3, 3, 4, 4, 4],
            [3, 3, 3, 3, 3,11,11,11,11,11,11,11,11,11, 4, 4],
            [3, 3, 3, 3, 3,10,10,10, 4, 4,10, 4, 3,10,10,10],
            [3, 3, 3, 3,10, 4,10, 4, 4, 4,10, 4, 4,10,10,10],
            [3, 3, 3, 3,10, 4,10,10, 4, 4, 4,10, 4, 4, 4,10],
            [3, 3, 3, 3,10,10, 4, 4, 4, 4,10,10,10,10,10, 3],
            [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,10, 3, 3],
            [3, 3,10,10,10,10,10,11,10,10,10,11, 3, 3, 3, 3],
            [3,10,10,10,10,10,10,10,11,10,10,10,11, 3, 3,10],
            [4, 4,10,10,10,10,10,10,11,11,11,11,11, 3, 3,10],
            [4, 4, 4, 3,11,11,10,11,11, 4,11,11, 4,11,10,10],
            [3, 4, 3,10,11,11,11,11,11,11,11,11,11,11,10,10],
            [3, 3,10,10,10,11,11,11,11,11,11,11,11,11,10,10],
            [3,10,10,10,11,11,11,11,11,11,11, 3, 3, 3, 3, 3],
            [3,10, 3, 3,11,11,11,11, 3, 3, 3, 3, 3, 3, 3, 3]         
]
jumpingMarioSurface = drawArrayIntoSurface(jumpingMarioData)
global backwardsJumpingMarioSurface
backwardsJumpingMarioData = []
for row in jumpingMarioData:
    backwardsJumpingMarioData.append(row[::-1])
backwardsJumpingMarioSurface = drawArrayIntoSurface(backwardsJumpingMarioData)

pygame.display.flip()
global coinSurface1
coinSurface1 = drawArrayIntoSurface([
            [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 1, 0, 0, 0, 0, 1, 1, 3, 3, 3, 3],
            [3, 3, 3, 1, 0, 0, 4, 4, 4, 4, 4, 6, 1, 3, 3, 3],
            [3, 3, 3, 1, 0, 4, 2, 0, 0, 2, 4, 6, 1, 3, 3, 3],
            [3, 3, 1, 0, 4, 2, 0, 2, 4, 1, 2, 4, 5, 1, 3, 3],
            [3, 3, 1, 0, 4, 2, 0, 2, 4, 1, 2, 4, 5, 1, 3, 3],
            [3, 3, 1, 0, 4, 2, 0, 2, 4, 1, 2, 4, 5, 1, 3, 3],
            [3, 3, 1, 0, 4, 2, 0, 2, 4, 1, 2, 4, 5, 1, 3, 3],
            [3, 3, 1, 0, 4, 2, 0, 2, 4, 1, 2, 4, 5, 1, 3, 3],
            [3, 3, 1, 0, 4, 2, 0, 2, 4, 1, 2, 4, 5, 1, 3, 3],
            [3, 3, 1, 0, 4, 2, 0, 4, 4, 1, 2, 4, 5, 1, 3, 3],
            [3, 3, 1, 0, 4, 2, 0, 4, 4, 1, 2, 4, 5, 1, 3, 3],
            [3, 3, 3, 1, 4, 2, 2, 1, 1, 2, 4, 6, 1, 3, 3, 3],
            [3, 3, 3, 1, 4, 4, 4, 4, 4, 4, 6, 6, 1, 3, 3, 3],
            [3, 3, 3, 3, 1, 1, 5, 5, 5, 5, 1, 1, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3]         
], 2)
 
pygame.display.flip()
global coinSurface2
coinSurface2 = drawArrayIntoSurface([
            [3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 0, 0, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 4, 4, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 2, 2, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 2, 2, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 4, 4, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 6, 6, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3]         
], 2)
 
pygame.display.flip()
global coinSurface3
coinSurface3 = drawArrayIntoSurface([
            [3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 0, 0, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 4, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 0, 2, 2, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 0, 4, 0, 1, 4, 6, 1, 3, 3, 3, 3],   
            [3, 3, 3, 3, 1, 0, 4, 0, 1, 4, 6, 1, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 0, 4, 0, 1, 4, 6, 1, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 0, 4, 0, 1, 4, 6, 1, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 0, 4, 0, 1, 4, 6, 1, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 0, 4, 0, 1, 4, 6, 1, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 0, 4, 0, 1, 4, 6, 1, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 0, 4, 0, 1, 4, 6, 1, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 4, 2, 2, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 1, 4, 4, 4, 6, 1, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 1, 6, 6, 1, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3]         
], 2)

class sprites():

    
    def drawLuckyBlockInClass(self, window, x, y):
        window.blit(luckyBlockSurface, (x + offsetX, y))
        
    def drawHitLuckyBlockInClass(self, window, x, y):
        window.blit(hitLuckyBlockSurface, (x + offsetX, y))
        
    def drawGoomba1InClass(self, window, x, y):
        window.blit(goombaSurface1, (x + offsetX, y))
        
    def drawGoomba2InClass(self, window, x, y):
        window.blit(goombaSurface2, (x + offsetX, y))
        
    def drawGroundBrickInClass(self, window, x, y):   
        window.blit(groundBrickSurface, (x, y))
        
    def drawBrickInClass(self, window, x, y):
        window.blit(brickSurface, (x + offsetX, y))
        
    def drawMarioInClass(self, window, x, y):
        window.blit(marioSurface, (x, y))

    def drawBackwardsMarioInClass(self, window, x, y):
        window.blit(backwardsMarioSurface, (x, y))

    def drawJumpingMarioInClass(self, window, x, y):
        window.blit(jumpingMarioSurface, (x, y))

    def drawBackwardsJumpingMarioInClass(self, window, x, y):
        window.blit(backwardsJumpingMarioSurface, (x, y))
    
    def drawRunningMario1InClass(self, window, x, y):
        window.blit(runningMario1Surface, (x, y))

    def drawBackwardsRunningMario1InClass(self, window, x, y):
        window.blit(backwardsRunningMario1Surface, (x, y))

    def drawRunningMario2InClass(self, window, x, y):
        window.blit(runningMario2Surface, (x, y))

    def drawBackwardsRunningMario2InClass(self, window, x, y):
        window.blit(backwardsRunningMario2Surface, (x, y))

    def drawRunningMario3InClass(self, window, x, y):
        window.blit(runningMario3Surface, (x, y))

    def drawBackwardsRunningMario3InClass(self, window, x, y):
        window.blit(backwardsRunningMario3Surface, (x, y))

    def drawStairsBlockInClass(self, window, x, y):
        window.blit(stairsBlockSurface, (x + offsetX, y))

    def drawDeadMarioInClass(self, window, x, y):
        window.blit(deadMarioSurface, (x, y))

    def drawCoin1InClass(self, window, x, y):
        window.blit(coinSurface1, (x + offsetX, y))
        
    def drawCoin2InClass(self, window, x, y):
        window.blit(coinSurface2, (x + offsetX, y))
        
    def drawCoin3InClass(self, window, x, y):
        window.blit(coinSurface3, (x + offsetX, y))
        
drawSprite = sprites()
def drawMario(direction, isJumping, isFalling, moving, ticks):
    if isJumping == True or isFalling == True:
        if direction == "right":
            drawSprite.drawJumpingMarioInClass(window, marioX, marioY)
        else:
            drawSprite.drawBackwardsJumpingMarioInClass(window, marioX, marioY)
    else:
        if moving == "right":
            singularModulus = (ticks/3)%3
            if singularModulus >= 0 and singularModulus < 1:
                drawSprite.drawRunningMario1InClass(window, marioX, marioY)
            elif singularModulus >= 1 and singularModulus < 2:
                drawSprite.drawRunningMario2InClass(window, marioX, marioY)
            else:
                drawSprite.drawRunningMario3InClass(window, marioX, marioY)
        elif moving == "left":
            singularModulus = (ticks/3)%3
            if singularModulus >= 0 and singularModulus < 1:
                drawSprite.drawBackwardsRunningMario1InClass(window, marioX, marioY)
            elif singularModulus >= 1 and singularModulus < 2:
                drawSprite.drawBackwardsRunningMario2InClass(window, marioX, marioY)
            else:
                drawSprite.drawBackwardsRunningMario3InClass(window, marioX, marioY)
        else:
            if direction == "right":
                drawSprite.drawMarioInClass(window, marioX, marioY)
            else:
                drawSprite.drawBackwardsMarioInClass(window, marioX, marioY)



 
running = True
fps = 32
lastKeyPressed = "none"
marioDirection = "right"
runTicks = -1

global totalFrames
totalFrames = 0

frames = [0 for i in range(100)]
badTicks = 0
cursor = 0
totalFrameTime = 0

global gravity
gravity = 2
global startVelocity
startVelocity = 16 * gravity


global marioVelocity
marioVelocity = 0

global jumping
jumping = False
global falling
falling = False
global goombaAnimationCounter
goombaAnimationCounter = 0
global goombaAnimationController
goombaAnimationController = 1


global endJump
endJump = pygame.time.get_ticks() - 500

def pointInRange(pointCord, rangeStart, rangeEnd):
    if pointCord >= rangeStart and pointCord <= rangeEnd:
        return True
    return False

def twoRangeOverlapOrTouch(start1, end1, start2, end2):
    smallestRight = min(end1, end2)
    largestLeft = max(start1, start2)
    if largestLeft <= smallestRight:
        return True
    return False
def twoRangeActuallyOverlap(start1, end1, start2, end2):
    smallestRight = min(end1, end2)
    largestLeft = max(start1, start2)
    if largestLeft < smallestRight:
        return True
    return False

def adjustAdditiveY(additiveY):
    global death
    global jumping
    global endJump
    global marioVelocity
    global falling
    global blockPositions
    global brickMap
    

    if twoRangeActuallyOverlap(marioY + 64, marioY + 64 + additiveY, groundHeight, groundHeight + 64):
        #Touching the ground
        distanceTravelable = groundHeight - marioY - 64
        additiveY = distanceTravelable
        jumping = False
        falling = False
        endJump = pygame.time.get_ticks()
        marioVelocity = 0

    elif additiveY > 0:
        #Moving Down
        for blockObject in blockPositions:
            blockX = blockObject[0]
            blockY = blockObject[1]
            blockType = blockObject[2]
            if (twoRangeOverlapOrTouch(marioY + 64, marioY + 64 + additiveY, blockY, blockY + 64)) and (twoRangeActuallyOverlap(realMarioX, realMarioX + 64, blockX, blockX + 64)):
                if blockType == "c":
                    pass
                else:
                    distanceTravelable = blockY - marioY - 64
                    additiveY = distanceTravelable
                    jumping = False
                    falling = False
                    endJump = pygame.time.get_ticks()
                    marioVelocity = 0
                    if blockType == "g":
                        marioVelocity = 10
                        falling = False
                        jumping = True
                        ### Play Sound Kill Goomba
                        blockPositions.remove(blockObject)
                        goombaMap.remove([blockX, blockY])  
    elif additiveY < 0:
        #Jumping
        for blockObject in blockPositions:
            blockX = blockObject[0]
            blockY = blockObject[1]
            blockType = blockObject[2]
            if (twoRangeOverlapOrTouch(marioY + additiveY, marioY, blockY, blockY + 64)) and (twoRangeActuallyOverlap(realMarioX, realMarioX + 64, blockX, blockX + 64)):
                if blockType == "c":
                    pass
                else:   
                    distanceTravelable = marioY - (blockY + 64)
                    additiveY = distanceTravelable
                    jumping = False
                    marioVelocity = 0
                    falling = True
                    if blockType == "lb":
                        #Make the coin appear above the Hit Lucky Block
                        blockPositions.append([blockX + 16, blockY + 16, "c"])
                        coinMap.append([blockX + 16, blockY + 16, [False, 0, 0], 16, 0])
                        if playCoinSound == True:
                            coinSound.play()
                        #Turn Lucky Block into a Hit Lucky Block
                        
                        blockPositions[blockPositions.index(blockObject)] = [blockX, blockY, "hlb"]
                        luckyBlockMap.remove([blockX, blockY, [False, 0, 0], 4])
                        hitLuckyBlockMap.append([blockX, blockY, [True, blockX, blockY], 4])
                    elif blockType == "g":
                        onDeath()
                    elif blockType == "b":
                        brickMap.remove([blockX, blockY, [False, 0, 0], 4])
                        brickMap.append([blockX, blockY, [True, blockX, blockY], 4])

    else:
        #Standing still, we need to check if they walk off a block
        for blockObject in blockPositions:
            blockX = blockObject[0]
            blockY = blockObject[1]
            blockType = blockObject[2]
            if (twoRangeOverlapOrTouch(marioY + 64, marioY + 64 + additiveY, blockY, blockY + 64)) and (twoRangeActuallyOverlap(realMarioX, realMarioX + 64, blockX, blockX + 64)) or twoRangeOverlapOrTouch(marioY + 64, marioY + 64 + additiveY, groundHeight, groundHeight + 64):
                break
        else:
            falling = True

    return additiveY

def adjustAdditiveX(additiveX):
    global death
    if marioAdditiveX > 0:
        #Moving Right 
        for blockObject in blockPositions:
            blockX = blockObject[0]
            blockY = blockObject[1]
            blockType = blockObject[2]
            if (twoRangeOverlapOrTouch(realMarioX + 64, realMarioX + 64 + additiveX, blockX, blockX + 64)) and (twoRangeActuallyOverlap(marioY, marioY + 64, blockY, blockY + 64)):
                if blockType == "c":
                    pass
                else:
                    distanceTravelable = blockX - realMarioX - 64
                    additiveX = distanceTravelable
                    if blockType == "g":    
                        onDeath()
    elif additiveX < 0:
        #Moving Left
        for blockObject in blockPositions:
            blockX = blockObject[0]
            blockY = blockObject[1]
            blockType = blockObject[2]
            if (twoRangeOverlapOrTouch(realMarioX + additiveX, realMarioX, blockX, blockX + 64)) and (twoRangeActuallyOverlap(marioY, marioY + 64, blockY, blockY + 64)):
                if blockType == "c":
                    pass
                else:  
                    distanceTravelable = blockX - realMarioX + 64
                    additiveX = distanceTravelable
                    if blockType == "g":
                        onDeath()

    return additiveX
            
    
def drawMap():
    global blockPositions
    global coinMap
    def drawGround():
        groundOffset = offsetX % 64
        for j in range(int(screenWidth/64 + 2)):
            x = -64 + groundOffset + j * 64
            y = screenHeight - 64*3
            drawSprite.drawGroundBrickInClass(window, x, y)
    def drawBlocks():
        global goombaAnimationCounter
        global goombaAnimationController
        for luckyBlock in luckyBlockMap:
            drawSprite.drawLuckyBlockInClass(window, luckyBlock[0], luckyBlock[1])
            blockPositions.append([luckyBlock[0], luckyBlock[1], "lb"])
        for brick in brickMap:
            drawSprite.drawBrickInClass(window, brick[0], brick[1])
            blockPositions.append([brick[0], brick[1], "b"])
        for stairsBlock in stairsBlockMap:
            drawSprite.drawStairsBlockInClass(window, stairsBlock[0], stairsBlock[1])
            blockPositions.append([stairsBlock[0], stairsBlock[1], "sb"])
        for i in range(len(coinMap)):
            if coinMap[i][4] >= 10:
                coinMap[i][4] = 1
            if coinMap[i][4] >= 7:
                drawSprite.drawCoin1InClass(window, coinMap[i][0], coinMap[i][1])
                coinMap[i][4] += 1
            elif coinMap[i][4] >= 4:
                drawSprite.drawCoin2InClass(window, coinMap[i][0], coinMap[i][1])
                coinMap[i][4] += 1
            elif coinMap[i][4] >= 1:
                drawSprite.drawCoin3InClass(window, coinMap[i][0], coinMap[i][1])
                coinMap[i][4] += 1
                
            blockPositions.append([coinMap[i][0], coinMap[i][1], "c"])

            
        for hitLuckyBlock in hitLuckyBlockMap:
            drawSprite.drawHitLuckyBlockInClass(window, hitLuckyBlock[0], hitLuckyBlock[1])
            blockPositions.append([hitLuckyBlock[0], hitLuckyBlock[1], "hlb"])
        for goomba in goombaMap:
            if goombaAnimationCounter == 5:
                goombaAnimationController *= -1
                goombaAnimationCounter = 0
            if goombaAnimationController == 1:
                drawSprite.drawGoomba1InClass(window, goomba[0], goomba[1])
                blockPositions.append([goomba[0], goomba[1], "g"])
            if goombaAnimationController == -1:
                drawSprite.drawGoomba2InClass(window, goomba[0], goomba[1])
                blockPositions.append([goomba[0], goomba[1], "g"])
  
    drawGround()
    drawBlocks()

while running:
    if death:
        print("You died")
        break
    goombaAnimationCounter += 1
    blockPositions = []
    marioAdditiveX = 0
    marioAdditiveY = 0
    totalFrames += 1
    startRender = pygame.time.get_ticks()
    window.fill((100, 149, 237))
    drawMap()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                lastKeyPressed = "right"
            elif event.key == pygame.K_LEFT:
                lastKeyPressed = "left"
            if event.key == pygame.K_UP:
                if startRender > endJump + 100 and jumping == False and falling == False:
                    if playJumpingSound == True:
                        jumpingSound.play()
                    jumping = True
                    marioVelocity = startVelocity
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and lastKeyPressed == "right":
                lastKeyPressed = "none"
                runTicks = -1
            elif event.key == pygame.K_LEFT and lastKeyPressed == "left":
                lastKeyPressed = "none"  
                runTicks = -1
    if lastKeyPressed == "right":
        marioDirection = "right"
        marioAdditiveX += 512/fps
        runTicks += 1
    elif lastKeyPressed == "left":
        marioDirection = "left"
        marioAdditiveX -= 512/fps
        runTicks += 1
    for i in range(0, len(brickMap)):
        if brickMap[i][2][0] == True:
            brickMap[i][1] -= brickMap[i][3]
            brickMap[i][2][2] -= brickMap[i][3]
            brickMap[i][3] -= 1
            if brickMap[i][3] < -4:
                brickMap[i][3] = 4
                brickMap[i][2] = [False, 0, 0]

    for i in range(0, len(hitLuckyBlockMap)):
        if hitLuckyBlockMap[i][2][0] == True:
            hitLuckyBlockMap[i][1] -= hitLuckyBlockMap[i][3]
            hitLuckyBlockMap[i][2][2] -= hitLuckyBlockMap[i][3]
            hitLuckyBlockMap[i][3] -= 1
            if hitLuckyBlockMap[i][3] < -4:
                hitLuckyBlockMap[i][3] = 4
                hitLuckyBlockMap[i][2][0] = False
                coinMap[coinMap.index([hitLuckyBlockMap[i][0] + 16, hitLuckyBlockMap[i][1] + 16, [False, 0, 0], 16, 0])] = [hitLuckyBlockMap[i][0] + 16, hitLuckyBlockMap[i][1] + 16, [True, hitLuckyBlockMap[i][2][1] + 16, hitLuckyBlockMap[i][2][2] + 16], 16, 1]
                hitLuckyBlockMap[i][2] = [False, 0, 0]
    for i in range(0, len(coinMap)):
        if coinMap[i][2][0] == True:
            coinMap[i][1] -= coinMap[i][3]
            coinMap[i][2][2] -= coinMap[i][3]
            coinMap[i][3] -= 1
            if coinMap[i][3] < -16:
                coinMap[i][3] = 16
                coinMap[i][2] = [False, 0, 0]

    if jumping == True:
        marioAdditiveY -= marioVelocity
        marioVelocity -= gravity
        if marioVelocity == 0:
            jumping = False
            falling = True
    if falling == True:
        marioAdditiveY += marioVelocity
        marioVelocity += gravity
            

    marioAdditiveY = adjustAdditiveY(marioAdditiveY)
    marioY += marioAdditiveY
    marioAdditiveX = adjustAdditiveX(marioAdditiveX)
    if marioX + marioAdditiveX <= screenWidth/2 - 64 and marioX + marioAdditiveX >= 256:
        marioX += marioAdditiveX
    else:
        offsetX -= marioAdditiveX
    realMarioX += marioAdditiveX
    
    
    drawMario(marioDirection, jumping, falling, lastKeyPressed, runTicks)
    
    endRender = pygame.time.get_ticks()
    renderTime = endRender - startRender

    totalFrameTime -= frames[cursor]
    frames[cursor] = renderTime
    totalFrameTime += renderTime
    cursor = (cursor + 1) % 100

    pygame.display.flip()
    
    timeToWait = int(1000/fps - renderTime)
    if ( timeToWait > 0 ):
        pygame.time.wait(timeToWait)
    else:
        badTicks += 1
        print("A bad tick just happened")
    if totalFrames % 100 == 0:
        print("The last 100 frames took an average of " + str(totalFrameTime / 100) + " ms to render")
        print("There have been " + str(badTicks) + " bad ticks so far")

deadMarioVelocity = 16
window.fill((100, 149, 237))
drawSprite.drawDeadMarioInClass(window, marioX, marioY)
pygame.time.wait(300)
while True:
    pygame.time.wait(30)
    window.fill((100, 149, 237))
    if marioY >= screenHeight + 100000:
        pygame.time.wait(100)
        break
    drawSprite.drawDeadMarioInClass(window, marioX, marioY)
    marioY -= deadMarioVelocity
    deadMarioVelocity -= gravity
    pygame.display.flip()
pygame.quit()
