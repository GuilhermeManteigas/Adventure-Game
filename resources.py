import pygame


class Resources:
    def __init__(self):
        self.images = [None] * 700
        self.player = [None] * 3
        self.load_images()

    def load_images(self):

        images = self.images
        player = self.player

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
        images[4] = [pygame.image.load('images/Blocks/snow/snow1.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow2.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow3.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow4.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow5.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow6.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow7.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow8.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow9.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow10.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow11.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow12.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow13.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow14.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow15.png').convert(),
                     pygame.image.load('images/Blocks/snow/snow16.png').convert()]

        ############### Entities ##############################
        images[200] = [pygame.image.load('images/Entities/tree/tree1.png').convert_alpha(),
                       pygame.image.load('images/Entities/tree/tree2.png').convert_alpha(),
                       pygame.image.load('images/Entities/tree/tree3.png').convert_alpha(),
                       pygame.image.load('images/Entities/tree/tree4.png').convert_alpha()]

        images[201] = [pygame.image.load('images/Entities/cactus/cactus1.png').convert_alpha(),
                       pygame.image.load('images/Entities/cactus/cactus2.png').convert_alpha(),
                       pygame.image.load('images/Entities/cactus/cactus3.png').convert_alpha(),
                       pygame.image.load('images/Entities/cactus/cactus4.png').convert_alpha()]

        images[202] = [pygame.image.load('images/Entities/snowtree/tree1.png').convert_alpha(),
                       pygame.image.load('images/Entities/snowtree/tree2.png').convert_alpha(),
                       pygame.image.load('images/Entities/snowtree/tree3.png').convert_alpha(),
                       pygame.image.load('images/Entities/snowtree/tree4.png').convert_alpha()]

        ############### Drops ##############################
        images[400] = [pygame.image.load('images/Drops/wood/wood1.png').convert_alpha(),
                       pygame.image.load('images/Drops/wood/wood2.png').convert_alpha(),
                       pygame.image.load('images/Drops/wood/wood3.png').convert_alpha(),
                       pygame.image.load('images/Drops/wood/wood4.png').convert_alpha()]

        ############### Extra ##############################
        images[600] = [pygame.image.load('images/Other/light.png').convert_alpha()]
        images[601] = [pygame.image.load('images/Other/marker.png').convert_alpha()]




        ############### Player ##############################
        player[0] = [pygame.image.load('images/Player/Minotaur_01_Idle_000.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_001.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_002.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_003.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_004.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_005.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_006.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_007.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_008.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_009.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_010.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Idle_011.png').convert_alpha()]

        player[1] = [pygame.image.load('images/Player/Minotaur_01_Walking_000.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_000.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_001.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_001.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_002.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_002.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_003.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_003.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_004.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_004.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_005.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_005.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_006.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_006.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_007.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_007.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_008.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_008.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_009.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_009.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_010.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_010.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_011.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_011.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_012.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_012.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_013.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_013.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_014.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_014.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_015.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_015.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_016.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_016.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_017.png').convert_alpha(),
                     pygame.image.load('images/Player/Minotaur_01_Walking_017.png').convert_alpha()]


    def get_images(self):
        return self.images

    def get_player(self):
        return self.player
