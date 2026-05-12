import pygame
#we need random for the enemys' random positions in the screen
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerImg=pygame.image.load('player.png')
playerX=370
playerY=480
playerX_change=0
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
speed=2
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(speed)
    enemyY_change.append(40)
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
win_font=pygame.font.Font('freesansbold.ttf',64)
textX=10
textY=10
# doing all the functions here itself so that its less messy doing the functions one by one and adding the keys pressing stuff in the functions itself
def show_score(x,y):
    score=font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def show_win():
    win_text=win_font.render("YOU WIN!",True,(255,255,255))
    screen.blit(win_text,(220,250))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=((enemyX-bulletX)**2+(enemyY-bulletY)**2)**0.5
    if distance<27:
        return True
    else:
        return False
#doing the game loop and the events for when the buttons are pressed(this event handling was mostly copilot)
running=True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletX=playerX
                    bulletY=480
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    enemies_left=0
    for i in range(num_of_enemies):
        #skip deleted enemies
        if enemyY[i]==-100:
            continue
        enemies_left+=1
        #move enemy only left and right
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=4
        elif enemyX[i]>=736:
            enemyX_change[i]=-4
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=480
            bullet_state="ready"
            score_value+=1
            #delete enemy
            enemyX[i]=-100
            enemyY[i]=-100
        enemy(enemyX[i],enemyY[i],i)
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if enemies_left==0:
        show_win()
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
    #no matter how much I decrease the speed of the enemies, i dont get why they just keep increasing their speed:(