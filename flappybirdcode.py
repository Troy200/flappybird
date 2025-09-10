import pygame,random

pygame.init()

WIDTH=800
HEIGHT=600

fps=60
x=0
score = 0
font=pygame.font.SysFont("Arial",70)
frequency=1000
lastpipe=0


gameover=False
gamestart=False

screen= pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("pro game devloper/flappy bird/images/bg.png")
ground=pygame.image.load("pro game devloper/flappy bird/images/ground.png")
restartbutton=pygame.image.load("pro game devloper/flappy bird/images/restart.png")


class bird(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        for bird in range (1,4):
            img=pygame.image.load(f"pro game devloper/flappy bird/images/bird{bird}.png")
            
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.counter=0
        self.velocity=0
        self.click=False
    def update(self):
        global gameover
        if gameover==False:
            self.counter+=1
            if self.counter>5:
                self.counter=0
                self.index+=1
                if self.index>2:
                    self.index=0
                self.image=self.images[self.index]
            
        if gamestart==True:
                self.velocity+=0.2
                self.rect.y+=self.velocity
                if self.rect.y>480:
                    self.rect.y=480
                    gameover=True
                if gameover==False:
                    if pygame.mouse.get_pressed()[0]==1 and self.click==False:  
                        self.velocity= -5
                        self.click=True
                    if pygame.mouse.get_pressed()[0]==0:
                        self.click=False
                    if gameover==False:
                        self.image=pygame.transform.rotate(self.images[self.index],self.velocity*-5)



class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.image.load("pro game devloper/flappy bird/images/pipe.png")
        self.rect=self.image.get_rect()
        self.past=False
        if direction==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y]
        if direction==-1:
            self.rect.topleft=[x,y]

    def update(self):
        self.rect.x-=10
        if self.rect.right==0:
            self.kill()




bird_group=pygame.sprite.Group()

flappy1=bird(150,300)
bird_group.add(flappy1)

pipe_group=pygame.sprite.Group()







clock=pygame.time.Clock()
run=True
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    screen.blit(ground,(x,500))
    if gameover==False:
        x-=3
        if x<-100:
            x=0
    if gamestart==True and gameover==False:
        time_now= pygame.time.get_ticks()
        if time_now-lastpipe>frequency:
            pipegap= random.randint(50,200)
            top_pipe=pipe(800,300-pipegap,1)
            bottom_pipe=pipe(800,300-pipegap+100,-1)
            pipe_group.add(top_pipe)
            pipe_group.add(bottom_pipe)
            lastpipe= time_now
    
    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False):
        gameover=True
    for i in pipe_group:
        if bird_group.sprites()[0].rect.left>i.rect.right and i.past==False:
            i.past=True
            score+=0.5
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    pipe_group.update()
    score_text = font.render(str(int(score)), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # (10, 10) = top-left corner

    if gameover:
        button=restartbutton.get_rect(topleft=(400,300))
        screen.blit(restartbutton,button)
        if event.type== pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(pygame.mouse.get_pos()):
                score=0
                gamestart=False
                gameover=False
                pipe_group.empty()
                flappy1.rect.center=[150,300]

    

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN:
            gamestart=True

    pygame.display.update()
