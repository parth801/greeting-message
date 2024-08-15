import pygame
import time
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("HAPPY BIRTHDAY")
img = pygame.image.load("background1.jpg")
image = pygame.transform.scale(img, (600, 600))
#pygame.display.update()


run = True
while run:
    screen.fill("white")
    screen.blit(image, (0,0))
    font   = pygame.font.SysFont("Arial", 64)
    text = font.render("Happy Birthday", True, ("blue"))
    screen.blit(text, (150, 200))
    pygame.display.update()
    time.sleep(1)


    img2 = pygame.image.load("background2.jpg")
    image2 = pygame.transform.scale(img2, (600, 600))
    screen.fill("white")
    screen.blit(image2, (0,0))
    font2  = pygame.font.SysFont("Arial", 15)
    text2 = font.render("HAVE A GREAT YEAR AHEAD", True, ("red"))
    screen.blit(text2, (20, 50))
    pygame.display.update()
    time.sleep(1)

    img3 = pygame.image.load("background3.jpg")
    image3 = pygame.transform.scale(img3, (600, 600))
    screen.fill("white")
    screen.blit(image3, (0,0))
    pygame.display.update()
    time.sleep(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
pygame.display.update()