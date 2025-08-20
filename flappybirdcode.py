import pygame

pygame.init()

WIDTH=800
HEIGHT=600

fps=50
x=0

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
    def update(self):
        self.index+=1
        if self.index>2:
            self.index=0
        self.image=self.images[self.index]


bird_group=pygame.sprite.Group()

flappy1=bird(150,300)
bird_group.add(flappy1)





clock=pygame.time.Clock()
run=True
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    screen.blit(ground,(x,500))
    x-=10
    if x<-100:
        x=0

    bird_group.draw(screen)
    bird_group.update()

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
    pygame.display.update()
