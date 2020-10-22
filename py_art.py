import sys, pygame, math, time
import base_converter
import pi_calculator
from decimal import Decimal as D
pygame.init()

size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0
current_col = pygame.Color("#000000")
current_col.hsva = (0, 100, 100, 100)

vals = "05033005141512410524"
base = 6
spacing = 10


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


screen.fill(black)

def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    return s

# print("***", 16*math.atan(1/5)-4*math.atan(1/239))
# print(math.pi-3, 6))

pi_calc = pi_calculator.PiCalculator()


current_pos = width/2, height/2

# for digit in vals:
pi_calc.get_next_digit()
pi_calc.get_next_digit()
i = 2
while True:
    print(pi_calc.get_next_digit())
    digit = int(pi_calc.get_next_digit()[i])%base
    # pi_val = base_converter.base(pi_calc.get_next_digit(),10)
    # print(i,pi_val)
    # digit = str(pi_val)[i]
    i += 1

    last_pos = current_pos

    rotation = int(digit)*2*math.pi/base

    current_pos = current_pos[0]+math.sin(rotation)*spacing, current_pos[1]+math.cos(rotation)*spacing,
    pygame.draw.line(screen, current_col, last_pos, current_pos, 3)

    pygame.display.flip()

    h,s,v,a = current_col.hsva
    h = (h+1)%360
    current_col.hsva = h,s,v,a
    print(current_col)


    clock.tick(30)


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