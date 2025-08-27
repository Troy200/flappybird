import pygame

pygame.init()

WIDTH=800
HEIGHT=600

fps=60
x=0
gameover=False

screen= pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("pro game devloper/flappy bird/images/bg.png")
ground=pygame.image.load("pro game devloper/flappy bird/images/ground.png")

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
            

        self.velocity+=0.2
        self.rect.y+=self.velocity
        if self.rect.y>480:
            self.rect.y=480
            gameover=True
        if pygame.mouse.get_pressed()[0]==1 and self.click==False:  
            self.velocity= -5
            self.click=True
        if pygame.mouse.get_pressed()[0]==0:
            self.click=False



bird_group=pygame.sprite.Group()

flappy1=bird(150,300)
bird_group.add(flappy1)





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

    bird_group.draw(screen)
    bird_group.update()

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
    pygame.display.update()
