import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Cubes Game")

walkright = [pygame.image.load('right_1.png'),pygame.image.load('right_2.png'), pygame.image.load('right_3.png'), pygame.image.load('right_4.png'), pygame.image.load('right_5.png'), pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'), pygame.image.load('left_3.png'), pygame.image.load('left_4.png'), pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]

bg = pygame.image.load('bg.jpg')

playerStand = pygame.image.load('idle.png')

clock=pygame.time.Clock()

x=50
y=425
width=60
height=71
speed=8

isJump=False
JumpCount=10

left=False
right=False
animCount=0

def drawWindow ():
    global animCount
    win.blit(bg,(0,0))
    if animCount +1>=30:
        animCount=0
    if left:
        win.blit(walkLeft[animCount//5],(x,y))
        animCount+=1
    elif right:
        win.blit(walkright[animCount//5],(x,y))
        animCount+=1
    else:
        win.blit(playerStand,(x,y))

    pygame.display.update()

run=True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
        left=True
        right=False
    elif  keys[pygame.K_RIGHT] and x<500-width-5:
        x+=speed
        left=False
        right=True
    else:
        right=False
        left=False
        animCount=0
    if not (isJump):
        if keys [pygame.K_SPACE]:
            isJump=True
    else:
        if JumpCount>=-10:
            if JumpCount<0:
                y+=(JumpCount**2)/3
            else:
                y-=(JumpCount**2)/3
            JumpCount-=1
        else:
            isJump=False
            JumpCount=10
    drawWindow ()
