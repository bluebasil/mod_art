import pygame, sys, math

class Display():

    def __init__(self, size=(1920, 1080), background=(0, 0, 0)):
        self.set_size(size)
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.overlay = self.screen.copy()
        #pygame.transform.scale(self.overlay, 10*self.size)
        self.screen.blit(pygame.transform.scale(self.overlay, size), (0, 0))
        self.screen.fill(background)


    def get_drawing_surface(self):
        return self.overlay

    def set_size(self,size):
        self.size = size
        self.w, self.h = self.size
        self.scale = 1
        self.offset = self.w/2, self.h/2

    def scale_size(self,multiplier):
        self.w *= multiplier
        self.h *= multiplier
        self.scale *= multiplier
        self.size = int(self.w), int(self.h)


    def get_point(self,input_point=(0,0)):
        return (input_point[0]+self.offset[0])*self.scale, (input_point[1]+self.offset[1])*self.scale

    def tick(self):
        updated = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.BUTTON_WHEELUP:
                print("BUTTON_WHEELUP")
            if event.type == pygame.MOUSEBUTTONUP:
                print("MOUSEBUTTONUP")
                print(event)

                #scroll out
                if event.button == 5:
                    self.scale_size(1.1)
                    self.overlay = pygame.transform.scale(self.overlay, self.size)
                if event.button == 4:
                    self.scale_size(0.9)
                    self.overlay = pygame.transform.scale(self.overlay, self.size)

            if event.type == pygame.MOUSEWHEEL:
                print("MOUSEWHEEL")


        self.screen.blit(self.overlay, (0, 0))
        pygame.display.flip()
