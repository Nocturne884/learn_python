import pygame

pygame.init()
screen = pygame.display.set_mode( (800, 600))
player_x = 400
player_y = 300
player_speed= 0.2
 
running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
             running = False
             
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
            player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
                
    player_x =max(0,  min(player_x, 800 - 50) )
    player_y =max(0,  min(player_y, 600 - 50) )
               
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0),(player_x,player_y,50,50))
    pygame.display.flip()
pygame.quit()
