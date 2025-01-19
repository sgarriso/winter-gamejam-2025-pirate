import pygame
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, blue, green, black

class Open:
    def __init__(self, display:pygame.display=pygame.display):
        self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = display
        self.display.set_caption("Start the Game")
        self.clock =  pygame.time.Clock()
        self.running = False
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Press A for Alchemy ', True, blue, black)
        self.textRect = self.text.get_rect()
        # set the center of the rectangular object.
        self.textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.screen.fill(black)
        self.logo_image = pygame.image.load('placeholder/logo/title.png')
        self.logo_rect = self.logo_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blits([(self.text, self.textRect),(self.logo_image, self.logo_rect)])
        self.event_type = pygame.KEYDOWN
        self.event_key = pygame.K_a
        self.running = True
    def check(self, events):
        self.running = True
        for event in events:
            if event.type == pygame.KEYDOWN and  event.key == pygame.K_a:
                self.running = False
                return {"alchemy": 100}
        return True