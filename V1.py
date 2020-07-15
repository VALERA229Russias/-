import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("CsGo2")

walkRight = [pygame.image.load('right_1.png'),
pygame.image.load('right_2.png'), pygame.image.load('right_3.png'),
pygame.image.load('right_4.png'), pygame.image.load('right_5.png'),
pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'),
pygame.image.load('left_2.png'), pygame.image.load('left_3.png'),
pygame.image.load('left_4.png'), pygame.image.load('left_5.png'),
pygame.image.load('left_6.png')]

playerStand = pygame.image.load('idle.jpg')

clock = pygame.time.Clock()

x = 50
y = 540
width = 60
height = 71
speed = 10

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

def drawWindow():
    global  animCount

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    win.blit(bg, (0, 0))
    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 10:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1210:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_UP] and y > 10:
            y -= speed
        if keys[pygame.K_DOWN] and y < 630:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 3
            else:
                y -= (jumpCount ** 2) / 3
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()
