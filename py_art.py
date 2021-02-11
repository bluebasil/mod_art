import sys, pygame, math
import pi_calculator, screen_management
import argparse

parser = argparse.ArgumentParser(description='Calculates pi in any base, and makes artistic fractals')
parser.add_argument('base', type=int, default=10, nargs='?',  help='Calculate pi in this base')
parser.add_argument('-l', '--length', type=int, default=math.inf, help='The number of digits to calculate.  ')


args = parser.parse_args()

pygame.init()
characters = list(range(0,10)) + [chr(c) for c in list(range(ord("A"),ord("Z")+1))]

size = width, height = 1920, 1080
current_col = pygame.Color("#000000")

base = args.base
spacing = 10
number_of_digits = args.length
hue_change_speed = 360/number_of_digits if number_of_digits is not math.inf else 0.1
lum_change_speed = 90/number_of_digits if number_of_digits is not math.inf else 0


#screen = pygame.display.set_mode(size,pygame.RESIZABLE)
sm = screen_management.Display()
screen = sm.get_drawing_surface()
#fake_screen = screen.copy()
clock = pygame.time.Clock()
#screen.blit(pygame.transform.scale(fake_screen, size), (0, 0))

#screen.fill(current_col)

pi_calc = pi_calculator.PiCalculator()

current_pos = (0,0)

log_base = math.ceil(math.log(base, 10))+1


print(pi_calc.get_next_digit(base=base), end="")
print(pi_calc.get_next_digit(base=base), end="")
i = 2
current_hue = 0
current_lum = 10 if number_of_digits is not math.inf else 50
current_col.hsla = (current_hue, 100, current_lum, 100)
while i < number_of_digits:


    digit = pi_calc.get_next_digit(base=base)

    # We can only print out PI in base 36 or less.  Otherwise we instead print the number of each character
    if base <= 36:
        print(characters[digit], end="", flush=True)
    else:
        print(f"{digit:{int(log_base)}}", end="", flush=True)

    i += 1
    last_pos = current_pos

    rotation = -digit*2*math.pi/base - math.pi

    current_pos = current_pos[0]+math.sin(rotation)*spacing, current_pos[1]+math.cos(rotation)*spacing
    sm.get_point(last_pos)
    pygame.draw.line(sm.get_drawing_surface(), current_col, sm.get_point(last_pos), sm.get_point(current_pos), 3)
    #pygame.draw.line(sm.get_drawing_surface(), current_col, last_pos, current_pos, 3)
    # 3width*=1.01
    # height*=1.01
    # size=int(width),int(height)
    #screen.blit(pygame.transform.scale(screen, size), (0, 0))
    #pygame.display.flip()

    h,s,l,a = current_col.hsla
    current_hue = (current_hue+hue_change_speed)%360
    current_lum = (current_lum+lum_change_speed)%360
    current_col.hsla = current_hue,s,current_lum,a

    sm.tick()


while True:
    sm.tick()

