import pygame
#############
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Pong")
#############
icon=pygame.image.load('rules.png')
pygame.display.set_icon(icon)
playeric=pygame.image.load('tetris.png')
ciric=pygame.image.load('circle.png')
##################
p1y=170
p1ych=0

p2y=170
p2ych=0

cirx=380
cirxch=2
ciry=180
cirych=-2

sc1=0
sc2=0
#############
def player1(y):
    screen.blit(playeric,(750,y))

def player2(y):
    screen.blit(playeric,(-15,y))

def circle(x,y):
    screen.blit(ciric,(x,y))

def show(s,font,size,rgb,x,y):
    font=pygame.font.Font(font,size)
    text=font.render(s,True,rgb)
    screen.blit(text,(x,y))
    
############
running =1
while running:
    screen.fill((0,0,0))
    show("player one : "+str(sc1)+"                              player two : "+str(sc2),'Destacy.ttf',30,(243,91,220),10,-10)
    show("By : Mohamed Hassan Anwar ","Stayola.ttf",35,(72,244,253),10,350)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1ych=-2
            if event.key == pygame.K_DOWN:
                p1ych=2
            if event.key == pygame.K_w:
                p2ych=-2
            if event.key == pygame.K_s:
                p2ych=2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p1ych=0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                p2ych=0
       



    p1y+=p1ych
    p1y=min(p1y,330)
    p1y=max(10,p1y)
    
    p2y+=p2ych
    p2y=min(p2y,330)
    p2y=max(10,p2y)
    
    player1(p1y+p1ych)
    player2(p2y+p2ych)
    
    if(ciry>370):
        cirych*=-1
    if(ciry<0):
        cirych*=-1
    if(cirx>760):
        sc2+=1
        cirx=380
        ciry=180
        cirxch*=-1
    if(cirx<-19):
        sc1+=1
        cirx=380
        ciry=180
        cirxch*=-1
    if (cirx>=740 and cirx<=750 and ciry>p1y-30  and ciry<p1y+60):
        cirxch*=-1

    if(cirx<=29 and cirx>=20 and  ciry>p2y-30  and ciry<p2y+60 ):
        cirxch*=-1
        
    cirx+=cirxch
    ciry+=cirych
    circle(cirx+cirxch,ciry+cirych)
    
    pygame.display.update()
