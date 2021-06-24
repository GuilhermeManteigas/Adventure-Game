import pygame


class Resources:
    def __init__(self):
        self.images = [None] * 700
        self.load_images()

    def load_images(self):

        images = self.images

        ############### Blocks ##############################
        images[1] = [pygame.image.load('images/Blocks/grass/grass1.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass2.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass3.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass4.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass5.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass6.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass7.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass8.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass9.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass10.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass11.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass12.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass13.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass14.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass15.png').convert(),
                     pygame.image.load('images/Blocks/grass/grass16.png').convert()]
        images[2] = [pygame.image.load('images/Blocks/sand/sand1.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand2.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand3.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand4.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand5.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand6.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand7.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand8.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand9.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand10.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand11.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand12.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand13.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand14.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand15.png').convert(),
                     pygame.image.load('images/Blocks/sand/sand16.png').convert()]
        images[3] = [pygame.image.load('images/Blocks/water/water1.png').convert_alpha(),
                     pygame.image.load('images/Blocks/water/water2.png').convert_alpha()]

        ############### Entities ##############################
        images[200] = [pygame.image.load('images/Entities/tree/tree1.png').convert_alpha(),
                       pygame.image.load('images/Entities/tree/tree2.png').convert_alpha(),
                       pygame.image.load('images/Entities/tree/tree3.png').convert_alpha(),
                       pygame.image.load('images/Entities/tree/tree4.png').convert_alpha()]

        ############### Drops ##############################
        images[400] = [pygame.image.load('images/Drops/wood/wood1.png').convert_alpha(),
                       pygame.image.load('images/Drops/wood/wood2.png').convert_alpha(),
                       pygame.image.load('images/Drops/wood/wood3.png').convert_alpha(),
                       pygame.image.load('images/Drops/wood/wood4.png').convert_alpha()]


    def get_images(self):
        return self.images