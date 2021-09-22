import pygame

pygame.init()
pygame.display.set_caption("Game TITLE")
screen = pygame.display.set_mode((400,400))

images = []
for i in range(4):
    images.append(pygame.image.load("mole.png"))
    
rects = []
for i in range(4):
    rects.append(images[i].get_rect())

effects = []
for i in range(4):
    effects.append(pygame.mixer.Sound("m"+str(i)+".mp3"))

points = [(25, 30), (25, 110), (25, 190), (65, 30), (65, 110), (65, 190)]

FPS = 400
fpsClock = pygame.time.Clock()

w = [255, 255, 255]

quitVar = True
show = True

while quitVar == True:
    screen.fill(w)

    for i in range(4):
        rects[i].center = points[i]
        screen.blit(images[i], rects[i])
    
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            for i in range(4):
                if rects[i].collidepoint(p):
                    effects[i].play()

    pygame.display.update()

    fpsClock.tick(FPS)
pygame.quit()
