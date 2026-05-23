import pygame   
import random

running = True
pygame.init()
LARGE = 800
HEIGHT = 600
screen = pygame.display.set_mode((LARGE, HEIGHT))
clock = pygame.time.Clock()
MI_EVENTO_SEGUNDO = pygame.USEREVENT + 1
pygame.time.set_timer(MI_EVENTO_SEGUNDO, 1000)
GRAVEDAD = 0.5
FRICCION = 0.85
circulos = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MI_EVENTO_SEGUNDO:
            radio = random.randint(10,25)
            circulos.append({
                "vx":random.randint(-3,3),
                "vy":0,
                "x":random.randint(radio,LARGE-radio),
                "y":random.randint(radio,HEIGHT-radio),
                "color":(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
                "radio":radio
            })
    
    for c in circulos:
        c["vy"] += GRAVEDAD
        c["x"] += c["vx"]
        c["y"] += c["vy"]
    for c in circulos:
        pygame.draw.circle(screen,c["color"],(int(c["x"]),int(c["y"])),int(c["radio"]))
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()