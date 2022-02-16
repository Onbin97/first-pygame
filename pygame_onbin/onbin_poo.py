from random import*
import pygame 
###################################################
# 기본 초기화
pygame.init() 

#회면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#회면 타이틀 설정
pygame.display.set_caption("Onbin Game")

#FPS
clock = pygame.time.Clock()
###################################################

# 1. 사용자 게임 초기화 (배경회면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("/Users/iwonbin/Desktop/python/first-pygame/pygame_onbin/onbin_game_image/background.png")

character = pygame.image.load("/Users/iwonbin/Desktop/python/first-pygame/pygame_onbin/onbin_game_image/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

character_speed = 0.6

to_x = 0
to_y = 0

poo = pygame.image.load("/Users/iwonbin/Desktop/python/first-pygame/pygame_onbin/onbin_game_image/poo.png")
poo_size = poo.get_rect().size
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_x_pos = randrange(0, screen_width - poo_width)
poo_y_pos = 0

running = True
while running:                                                  
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
           
        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0    

    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width -character_width

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poo_rect =  poo.get_rect()
    poo_rect.left = poo_x_pos
    poo_rect.top = poo_y_pos

    poo_y_pos += 1 * dt 
    
    if poo_y_pos > screen_height:
        poo_y_pos = 0
        poo_x_pos = randrange(0, screen_width - poo_width)

    if character_rect.colliderect(poo_rect):
        running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    
    screen.blit(background,(0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(poo, (poo_x_pos, poo_y_pos))

    pygame.display.update() #게임화면을 다시 그리기
    
    

pygame.time.delay(1000)

pygame.quit()

