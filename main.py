import pygame
import time
import random
import pygame_menu

# initialise pygame
pygame.init()

# set colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (82, 82, 82)

# window and image varables
font_size = 56
font = pygame.font.SysFont('georgia', font_size)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_img = pygame.image.load('Images/bg1.png')
bg_img = pygame.transform.scale(bg_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
sword_pic = pygame.image.load('Images/sword.png')
sword_pic = pygame.transform.scale(sword_pic,(50, 50))
charactur_pic = pygame.image.load('Images/charactur.png')
charactur_pic = pygame.transform.scale(charactur_pic,(80, 80))
pygame.display.set_caption('Toby Typing')
input_rect = pygame.Rect(250, 300, 340, 30)

mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.title_background_color=(0, 0, 0)
menu = pygame_menu.Menu('MENU', 400, 300, theme=mytheme)

#Game Function
def the_game():
    # set variables
    level_counter = 0
    wrong_counter = 0
    level = 1
    game_over = False
    words = ['the', 'she', 'her', 'it', 'his', 'they', 'grey', 'new', 'old', 'first']
    words2 = ['brown', 'smelly', 'snot', 'poop', 'tree', 'funny', 'lost', 'sick', 'green', 'sticky']
    words3 = ['lump', 'feet', 'horse', 'gnome', 'fish', 'wee', 'cheese', 'blob', 'butt', 'bogie']
    words4 = ['sausage', 'weiner', 'ghost', 'alien', 'sweet', 'balls', 'lemon', 'hump', 'wart', 'snot']
    answer = True
    wrong_counter = 0
    play_again = True
    level = 1
    between_screen = ''
    between_text = ''
    input_rect = pygame.Rect(250, 300, 340, 31)
    user_text = ''
    active = False
    next_answer = False
    word = ''
    word_helper = ''
    letter = False
    score = 0
    random_num = random.randint(0, 9)
    req_input = words[random_num]
    random_num2 = random.randint(0, 9)
    random_num3 = random.randint(0, 9)
    random_num4 = random.randint(0, 9)
    level_counter = 0
    wrong_counter = 0
    game_over = False
    start_time = time.time()
    end_time = 0
    game_time = 0
    word_per_min = 0
    charactur_size = 80
    sword_size = 50
    charactur_pos = [620, 450]
    sword_pos = [80, 50]
    font_size = 56
    font = pygame.font.SysFont('georgia', font_size)
    
    # Load and play background music
    pygame.mixer.music.load('sounds/bg_music.wav')
    pygame.mixer.music.play(-1)
    
    # set over top sounds
    fart_sound = pygame.mixer.Sound("sounds/fart.wav")
    winer_sound = pygame.mixer.Sound("sounds/winner.wav")
    
    # game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
        
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    
                    elif event.key == 13:
                        next_answer = True
                        
                        if user_text == req_input:
                            answer = True
                            score += 1
                        if user_text != req_input:
                            answer = False
                        
                        if user_text == '':
                            answer = False
                        user_text = ''
                        level_counter += 1
                        
                    else:
                        user_text += event.unicode
        
        #charactur and sword move
        if answer == False:
            pygame.mixer.Sound.play(fart_sound)
            wrong_counter += 1
            charactur_pos[0] -= 90
            sword_pos[1] += 67
            answer = True
        
        # level 1
        if level == 1 and level_counter <= 5 and next_answer == True:
            random_num = random.randint(0, 9)
            req_input = words[random_num]
            next_answer = False

        # level 2
        if level == 2 and level_counter > 6 and level_counter <= 15 and next_answer == True:
            random_num = random.randint(0, 9)
            random_num2 = random.randint(0, 9)
            req_input = (words[random_num] + ' ' + words2[random_num2])
            next_answer = False

        # level 3
        if level == 3 and level_counter > 16  and level_counter <= 25 and next_answer == True:
            random_num = random.randint(0, 9)
            random_num2 = random.randint(0, 9)
            random_num3 = random.randint(0, 9)
            req_input = (words[random_num] + ' ' + words2[random_num2] + ' ' + words3[random_num3])
            next_answer = False

        # level 4
        if level == 4 and level_counter > 26  and level_counter <= 39 and next_answer == True:
            random_num = random.randint(0, 9)
            random_num2 = random.randint(0, 9)
            random_num3 = random.randint(0, 9)
            random_num4 = random.randint(0, 9)
            req_input = (words[random_num] + ' ' + words2[random_num2] + ' ' + words3[random_num3] + ' ' + words4[random_num4])
            next_answer = False
            
        # next level pages
        if (level_counter == 6 and wrong_counter != 6) or (level_counter == 16 and wrong_counter != 6) or (level_counter == 26 and wrong_counter != 6):
            req_input = ''
            between = True
            between_screen = 'Next Level'
            font_size = 100
            font = pygame.font.SysFont('georgia', font_size)
            window.blit(bg_img, (0, 0))
            between_text = font.render(between_screen, True, BLACK)
            window.blit(between_text, (155, 130))
            pygame.display.update()
            time.sleep(1.5)
            between_screen =''
            level +=1
            level_counter +=1
            font_size = 50
            font = pygame.font.SysFont('georgia', font_size)
            
        # End of the game page
        if wrong_counter == 6:
            end_time = time.time()
            game_time = end_time - start_time
            word_per_min = score / (game_time / 60)
            word_per_min = int(word_per_min)
            game_time = int(game_time)
            window.blit(bg_img, (0, 0))
            font_size = 120
            font = pygame.font.SysFont('georgia', font_size)
            Dead_text = font.render('YOU DIED', True, RED)
            window.blit(Dead_text, (130, 160))
            font_size = 35
            font = pygame.font.SysFont('georgia', font_size)
            end_text2 = font.render('Score: ' + str(score), True, BLACK)
            window.blit(end_text2, (240, 320))
            end_text3 = font.render('Time: ' + str(game_time), True, BLACK)
            window.blit(end_text3, (480, 320))
            end_text4 = font.render('Words per min: ' + str(word_per_min), True, BLACK)
            window.blit(end_text4, (240, 370))
            pygame.display.update()
            time.sleep(5)
            game_over = True

        # end of game you win page
        if level_counter == 40:
            end_time = time.time()
            game_time = end_time - start_time
            word_per_min = score / (game_time / 60)
            word_per_min = int(word_per_min)
            game_time = int(game_time)
            pygame.mixer.Sound.play(fart_sound)
            font_size = 120
            font = pygame.font.SysFont('georgia', font_size)
            window.blit(bg_img, (0, 0))
            end_text = font.render('You Win!', True, RED)
            window.blit(end_text, (130, 160))
            font_size = 35
            font = pygame.font.SysFont('georgia', font_size)
            end_text2 = font.render('Score: ' + str(score), True, BLACK)
            window.blit(end_text2, (240, 320))
            end_text3 = font.render('Time: ' + str(game_time), True, BLACK)
            window.blit(end_text3, (480, 320))
            end_text4 = font.render('Words per min: ' + str(word_per_min), True, BLACK)
            window.blit(end_text4, (240, 370))
            pygame.display.update()
            time.sleep(5)
            game_over = True

        # Game display
        window.blit(bg_img, (0, 0))
        window.blit(charactur_pic, (charactur_pos[0], charactur_pos[1]))
        window.blit(sword_pic, (sword_pos[0], sword_pos[1]))
        font_size = 38
        font = pygame.font.SysFont('georgia', font_size)
        level1_text = font.render(req_input, True, BLACK)
        window.blit(level1_text, (230, 150))
        font_size = 30
        font = pygame.font.SysFont('georgia', font_size)
        score_text = font.render('Score: ' + str(score), True, BLACK)
        window.blit(score_text, (620, 10))
        pygame.draw.rect(window, GREY, input_rect)
        font_size = 25
        font = pygame.font.SysFont('georgia', font_size)
        text_surface = font.render(user_text, True, WHITE)
        window.blit(text_surface, (input_rect.x+3, input_rect.y))
        pygame.display.update()
        
    pygame.mixer.music.stop()
    pass

#Welcome screen
window.blit(bg_img, (0, 0))
welcome_text = font.render('Welcome To Toby Typing!', True, BLACK)
window.blit(welcome_text, (80, 200))
pygame.display.update()
time.sleep(5)

# Instructions screen
window.blit(bg_img, (0, 0))
instructiontitle_text = font.render('Instructions', True, BLACK)
window.blit(instructiontitle_text, (240, 90))
font_size = 26
font = pygame.font.SysFont('georgia', font_size)
instruction_text = font.render('Type the words on screen and press enter', True, BLACK)
instruction2_text = font.render('Accuracy and speed of typing are important', True, BLACK)
instruction3_text = font.render('The character and knife move for incorrect answers', True, BLACK)
instruction4_text = font.render('If the sword hits the character, YOU DIE!', True, BLACK)
art_text = font.render('Artwork By Chloe B', True, BLACK)
window.blit(art_text, (20, 430))
window.blit(instruction3_text, (140, 260))
window.blit(instruction4_text, (140, 300))
window.blit(instruction_text, (140, 180))
window.blit(instruction2_text, (140, 220))
pygame.display.update()
time.sleep(5)

# The Game Menu
menu.add.button('Play', the_game)
menu.add.button('High Scores', the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(window)
