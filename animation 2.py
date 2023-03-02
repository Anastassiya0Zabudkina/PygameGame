import pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode([600,424])

ship = pygame.image.load("/Users/stanislavzabudkin/Desktop/IT/ship.jpg").convert()
ship.set_colorkey([255,255,255])
wolni = pygame.image.load("/Users/stanislavzabudkin/Desktop/IT/волны.jpg").convert()
wolni1 = wolni.get_rect(bottomright=(600,424))
window.blit(wolni,wolni1)
solnishko = pygame.image.load("/Users/stanislavzabudkin/Desktop/IT/solnishko.jpg").convert()
solnishko.set_colorkey([255,255,255])
akula = pygame.image.load("/Users/stanislavzabudkin/Desktop/IT/akula.jpg").convert()
akula.set_colorkey([255,255,255])
rainbow = pygame.image.load("/Users/stanislavzabudkin/Desktop/IT/rainbow.jpg").convert()
rainbow.set_colorkey([255,255,255])
oblako = pygame.image.load("/Users/stanislavzabudkin/Desktop/IT/oblako.jpg").convert()
oblako.set_colorkey([255,255,255])
x = 0
y = 300
x2 = 500
y2 = 80
x3 = 400
y3 = 350
x4 = 300
y4 = 200
x5 = 100
y5 = 80
a1 = 360
a2 = 0
k = 0
jump = False
jump_count = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    wolni = pygame.image.load("/Users/stanislavzabudkin/Desktop/IT/волны.jpg").convert()
    wolni1 = wolni.get_rect(bottomright=(600,424))
    window.blit(wolni,wolni1)

    oblako1 = pygame.transform.rotate(oblako,a2)
    rect1 = oblako1.get_rect(center=(x5,y5))
    if a2 < 360:
        a2 += 15
    else:
        a2 = 0
    window.blit(oblako1,rect1)

    if k < 10 :
        rainbow1 = pygame.transform.scale(rainbow,(rainbow.get_width()//10,rainbow.get_height()//10))
        rect2 = rainbow1.get_rect(center=(x4,y4))
        window.blit(rainbow1,rect2)
        k+=1
    else:
        rainbow1=pygame.transform.scale(rainbow,(rainbow.get_width()//2,rainbow.get_height()//2))
        rect2 = rainbow1.get_rect(center=(x4,y4))
        window.blit(rainbow1,rect2)
        k-=1



    akula1 = pygame.transform.scale(akula,(akula.get_width()//1,akula.get_height()//1))
    rect3 = akula1.get_rect(center=(x3,y3))
    window.blit(akula1,rect3)
    if x3 >- 300:
        x3 -= 10
    else:
        x3 = 600


    solnishko1 = pygame.transform.rotate(solnishko,a1)
    rect4 = solnishko1.get_rect(center=(x2,y2))
    window.blit(solnishko1,rect4)
    if a1 > 0:
        a1 -= 5
    else:
        a1 = 360


    rect5 = ship.get_rect(center=(x,y))
    window.blit(ship,rect5)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x<680:
        x += 5
    elif x == 680:
        x = 0
    elif keys[pygame.K_LEFT] and x >0:
        x-=5
    if not ( jump ) :
        if keys [pygame.K_SPACE] :
            jump=True
    else:
        if jump_count >= -10:
            if jump_count<0:
                y += (jump_count**2)/2
            else:
                y -= (jump_count**2)/2
            jump_count -= 1
        else:
            jump = False
            jump_count = 10

    pygame.display.flip()
    clock.tick(15)


pygame.quit()


