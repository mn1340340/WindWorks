##
# windworks!
#
# @author Melissa Ning
# @course ICS3UC
#
# Based on Pygame base template MVC version
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
##
## Pygame setup
import pygame
import random
pygame.init()

class Boat(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        # Attributes
        self.image = pygame.image.load(filename).convert()
        #color key to create transperency 
        self.bgcolor = WHITE
        self.pos = [50, 230]       # Default position
        self.speed = [0, 0]
        #create rect based on image
        self.rect = self.image.get_rect(topleft=(self.pos[0], self.pos[1]))        

    # Draw the boat
    def draw(self):
        self.image.set_colorkey(self.bgcolor) 
        screen.blit(self.image, [int(self.pos[0]), int(self.pos[1])])

    # Move the boat
    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        #restrict to water
        if self.pos[0] + self.speed[0] > 950:
            self.pos[0] = 50
            
        if self.pos[1] + self.speed[1] < 200:
            self.pos[1] = 200

        if self.pos[1] + self.speed[1] > 570:
            self.pos[1] = 570

    ##change wind speed based on proximity
        #check proximity between boat and obstacle
        radius_x = self.pos[0] - x
        radius_y = self.pos[1] - y

        #change speed for x axis
        if radius_x> 50 and radius_x<100:
            self.speed[0] = 1.2
        elif radius_x >100 and radius_x <120:
            self.speed[0] = 1.1
        else:
            self.speed[0] = 0

        #change speed for y axis
        if 50< radius_y < 100:
            self.speed[1]= 1.2
        elif 100< radius_y < 120:
            self.speed[1] = 1.1
        elif -100< radius_y < -50:
            self.speed[1] = -1.2
        elif -120 < radius_y <-100:
            self.speed[1] = 1.1
        else:
            self.speed[1] = 0
        #update rect
        self.rect.topleft = (self.pos[0], self.pos[1])
            
class obstacles(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        # Attributes
        self.image = pygame.image.load(filename).convert()
        #color key to create transperency 
        self.bgcolor = BLACK
        self.pos = [50, 230]       # Default position
        self.speed = [0, 0]
        #create rect based on image
        self.rect = self.image.get_rect(topleft=(self.pos[0], self.pos[1]))

    #draw the obstacles
    def draw(self):
        self.image.set_colorkey(self.bgcolor) 
        screen.blit(self.image, [int(self.pos[0]), int(self.pos[1])])

    #move the obstacles
    def move(self):
        self.pos[0] += self.speed[0]
        #update rect 
        self.rect.topleft = (self.pos[0], self.pos[1])   

##to enable ability to reset variables if played again
def set():
    #create sprite group for coins
    coin_list = pygame.sprite.Group()
    #create sprite group for obstacles(croc/log)
    all = pygame.sprite.Group()
    
    #game stats
    life = 5
    coins_collected = 0
    score = 1000

    # Our boat
    boat = Boat("boat.png")
    boat.pos = [50, 230]       # Default position
    boat.speed = [0, 0]

    #varying speed for sprites to move at
    speed_list = [-1, -1.1, -1.2, -1.3]

    #create crocodile sprites at random location
    for i in range(30):
        croc = obstacles("crocodile.png")
        croc.pos = [random.randrange(100, 10000), random.randrange(200, 550)]
        croc.speed[0] = random.choice(speed_list)
        all.add(croc)

    #create log sprites at random location
    for i in range(30):
        mylog = obstacles("log.png")
        mylog.pos = [random.randrange(100, 10000), random.randrange(200, 550)]
        mylog.speed[0] = random.choice(speed_list)
        all.add(mylog)
        

    #create coin sprites at random location
    for i in range(15):
        coin = obstacles("coin.png")
        coin.pos = [random.randrange(100, 10000), random.randrange(200, 550)]
        coin.speed[0] = random.choice(speed_list)
        coin_list.add(coin)

    #start framecounter and seconds before main loop
    frames = 0
    second = 60
    return coin_list, all, life, coins_collected, score, boat, croc, mylog, coin, frames, second

size = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("windworks!")

## MODEL - Data use in system

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (99, 173, 230)

#load screen while not playing(blurred treetop, treebottom, and water)
notplaying = pygame.image.load("notplaying.png").convert()

#load land bg imgs
treetop = pygame.image.load("treetop.png").convert()
treebottom = pygame.image.load("treebottom.png").convert()

#load cloud img
cloud = pygame.image.load("cloud.png").convert()
cloud.set_colorkey(BLACK)

#load heart img
heart = pygame.image.load("heart.png").convert()
heart.set_colorkey(BLACK)

#small sized font
font_small = pygame.font.Font('pixelfont.ttf', 25)

#large sized font
font_big = pygame.font.Font('pixelfont.ttf', 120)

#medium sized font 
font_mid = pygame.font.Font('pixelfont.ttf', 60)

#slighty smaller medium sized font
font_mid1 = pygame.font.Font('pixelfont.ttf', 40)

my_coin_list, all_list, lives, coin_score, score, woodBoat, my_croc, my_log, my_coin, framecounter, seconds = set() 

highscore = 0
score_msg = (f"highscore: {highscore}")
# Loop until the user clicks the close button.
done = False
gameover = False
start = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## Main Program Loop
while not done:
        # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not start:
        screen.blit(notplaying, [0, 0])
        text_title = font_big.render("WINDWORKS!", True, BLACK) 
        screen.blit(text_title, [220, 200])
        text_blurb = font_mid1.render("power your boat using a sustainbale energy source, ", True, BLACK) 
        text_blurb1=font_mid1.render("wind, to reach your destination safely!", True, BLACK)
        screen.blit(text_blurb, [120, 320])
        screen.blit(text_blurb1, [230, 340])

        text_presstoplay = font_mid.render("press any key to start", True, BLACK)
        screen.blit(text_presstoplay, [260, 370])
        text_inst1 = font_mid1.render("1. Use your mouse and hover around the boat to control the wind.", True, BLACK)
        screen.blit(text_inst1, [30, 440])
        text_inst2 = font_mid1.render("2. Avoid logs and crocodiles or lose lives and points!", True, BLACK)
        screen.blit(text_inst2, [150, 470])
        text_inst3 = font_mid1.render("3. Collect coins for points!", True, BLACK)
        screen.blit(text_inst3, [300, 500])

        #start game if player presses a key
        if event.type == pygame.KEYUP:
            start = True

    #start game 
    if not gameover and start:
    ## CONTROL
        #check mouse position
        mousePos = pygame.mouse.get_pos() 
        x = mousePos[0]-20
        y = mousePos[1]-20

        # Game logic 
        #move obstacles
        for z in all_list: 
            z.move()

        #move coins
        for movecoin in my_coin_list:
            movecoin.move()
        #move boat
        woodBoat.move()

        #croc and log collisions
        bad_hit_list = pygame.sprite.spritecollide(woodBoat, all_list, True)
        #take away a life and subtract from score
        for hit in bad_hit_list:
            lives -= 1
            score -= 100

        #coin collisions
        good_hit_list = pygame.sprite.spritecollide(woodBoat, my_coin_list, True)

        #add to score and coinscore
        for good_hit in good_hit_list:
            coin_score += 1
            score += 50

        #count each frame
        framecounter += 1
        #60 fps
        if framecounter % 60 == 0:
            seconds -= 1 
        
        #end game if no more lives
        if lives == 0:
            gameover = True
            end_msg = "GAME OVER"   
            end_rgb = RED
        #player wins if they don't die within 60 sec or colect all coins
        if seconds == 0 or coin_score == 10:
            gameover = True
            end_msg = "YOU WON!" 
            end_rgb = BLACK

        ## VIEW
        # Clear screen
        screen.fill(GREEN)

        #land bg
        screen.blit(treetop, [0, 0])
        screen.blit(treebottom, [0, 600])

        # water
        pygame.draw.rect(screen, BLUE, [0, 200, 1000, 400])
    
        # Draw boat
        woodBoat.draw()

        #draw obstacles(croc/log)
        for all in all_list:
            all.draw()

        #draw coins
        for a in my_coin_list:
            a.draw()

        #draw cloud following cursor
        screen.blit(cloud, [x, y])  

        #draw hearts(lives)
        x_offset = 0
        for b in range(lives):
            screen.blit(heart, [20+x_offset, 20])
            x_offset += 60
        text = font_small.render(f"{lives}/5", True ,BLACK)
        screen.blit(text, [310, 30])

        #draw coin score
        screen.blit(my_coin.image, [40, 70])
        text_coin = font_small.render(f"{coin_score}x", True, BLACK)
        screen.blit(text_coin, [20, 80])
        
        #draw score
        text_score = font_small.render(f"score: {score}", True, BLACK)
        screen.blit(text_score, [850, 5])
        text_highscore = font_small.render(f"highscore: {highscore}", True, BLACK)
        screen.blit(text_highscore, [870, 600])

        #draw timer
        text_timer = font_small.render(str(seconds), True, BLACK)
        screen.blit(text_timer, [500, 30])
        
    elif gameover:
        screen.blit(notplaying, [0, 0])
        text_gameover = font_big.render(end_msg, True, end_rgb)
        screen.blit(text_gameover, [280, 250])
        text_playagain = font_mid.render("to play again, press any key", True, end_rgb)
        screen.blit(text_playagain, [200, 400])

        #set new highscore + "new!"
        if score > highscore:
            highscore = score
            score_msg = (f"new highscore!: {highscore}")
        text_go_highscore = font_mid.render(score_msg, True, end_rgb)
        screen.blit(text_go_highscore, [350, 450])

        #play again if a key is pressed
        if event.type == pygame.KEYUP:
            gameover = False
            #reset sprite groups, score, and position of sprites(croc/log/coins)
            my_coin_list, all_list, lives, coin_score, score, woodBoat, my_croc, my_log, my_coin, framecounter, seconds = set() 

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()  