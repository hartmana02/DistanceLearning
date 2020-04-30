import pygame, random, math

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
screen.fill((0, 0, 0))
pygame.display.update()

player_x = 225
player_y = 350
player_width = 30
player_height = 30
player_image = pygame.image.load("game_images/heart.png")
player_vel = 6

enemy_color_list = [(255, 255, 255), (0, 255, 255)]
enemy_color = enemy_color_list[0]
enemy_x_list = []
enemy_y_list = []
enemy_radius = 20
enemy_vel = 7
num_of_enemies = 15
for i in range(num_of_enemies):
    enemy_x_list.append(random.randint(0, 500))

    enemy_y_list.append(random.randint(-1000, -250))

reset_button = pygame.Rect(190, 300, 125, 50)

death_text = pygame.image.load("game_images/you_died.png")

collision = False
running = True
score = 0
font = pygame.font.Font("freesansbold.ttf", 25)

def reset_game():
    global collision, score, num_of_enemies, enemy_vel, enemy_color, player_x, player_y
    screen.fill((0, 0, 0))
    
    collision = False
    score = 0

    enemy_color = enemy_color_list[0]
    enemy_vel = 7
    enemy_x_list.clear()
    enemy_y_list.clear()
    for i in range(num_of_enemies):
        enemy_x_list.append(random.randint(0, 500))

        enemy_y_list.append(random.randint(-1000, -250))

    player_x = 225
    player_y = 350

while running:
    screen.fill((0, 0, 0))

    display_score = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(display_score, (350, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  

            if reset_button.collidepoint(mouse_pos):
                reset_game()

    if score >= 50 and score < 100:
        enemy_vel = 8
        enemy_color = enemy_color_list[1]

    if not collision:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > player_vel:
            player_x -= player_vel
        if keys[pygame.K_RIGHT] and player_x < 500 - player_vel - player_width:
            player_x += player_vel
        if keys[pygame.K_UP] and player_y > player_vel:
            player_y -= player_vel
        if keys[pygame.K_DOWN] and player_y < 500 - player_vel - player_height:
            player_y += player_vel

        screen.blit(player_image, (player_x, player_y))

        for i in range(num_of_enemies):
            if enemy_y_list[i] > 500: 
                enemy_y_list[i] = random.randint(-500, 0)
                enemy_x_list[i] = random.randint(0, 500)
                score += 1

            #hit detection uses the distance formula
            distance = math.sqrt((math.pow(enemy_x_list[i] - (player_x+15), 2)) + (math.pow(enemy_y_list[i] - (player_y+15), 2))) 
            if distance < 40:
                collision = True

            enemy_y_list[i] += enemy_vel
            pygame.draw.circle(screen, enemy_color, (enemy_x_list[i], enemy_y_list[i]), enemy_radius)

    else:
        pygame.draw.rect(screen, [200, 0, 0], reset_button)
        
        screen.blit(death_text, (-15, -100))

        replay_text = font.render("Replay", True, (0, 0, 0))
        screen.blit(replay_text, (210, 315))
        
    pygame.display.update()