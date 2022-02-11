from numpy import character
import pygame 

pygame.init() #초기화

#회면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#회면 타이틀 설정
pygame.display.set_caption("Nado Game")

#배경이미지 불러오기
background = pygame.image.load("/Users/iwonbin/Desktop/python/first-pygame/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/iwonbin/Desktop/python/first-pygame/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0] #가로크기
character_height = character_size[1] #세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((0, 0, 255)) #색으로만 채우기
    screen.blit(background, (0, 0))
    
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면을 다시 그리기
    
pygame.quit()

