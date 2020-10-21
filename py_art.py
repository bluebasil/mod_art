import sys, pygame
pygame.init()

size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0
current_col = pygame.Color("#000000")
current_col.hsva = (0, 100, 100, 100)


screen = pygame.display.set_mode(size)


screen.fill(black)
pygame.draw.line(screen, current_col, (0, 0), (100, 100), 5)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()
#
#
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.draw.line(screen,current_col,(0,0),(100,100),5)
#     pygame.display.flip()