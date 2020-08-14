import pygame
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((1500,800))
pygame.display.set_caption("Bubble Trouble")

walkRight = [pygame.transform.scale(pygame.image.load('images/R1.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/R2.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/R3.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/R4.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/R5.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/R6.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/R7.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/R8.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/R9.png'),(100,100))]
walkLeft = [pygame.transform.scale(pygame.image.load('images/L1.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/L2.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/L3.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/L4.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/L5.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/L6.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/L7.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/L8.png'),(100,100)),pygame.transform.scale(pygame.image.load('images/L9.png'),(100,100))]
bg = pygame.image.load('images/bg.jpg') 
bg = pygame.transform.scale(bg,(1500,800))
char = pygame.transform.scale(pygame.image.load('images/standing.png'),(100,100))
clock = pygame.time.Clock()
ball = pygame.image.load('images/ball.png')
bubbles=[ball,pygame.transform.scale(ball,(100,100)),pygame.transform.scale(ball,(75,75)),pygame.transform.scale(ball,(50,50))]

hitsound=pygame.mixer.Sound('music/hit.mp3')
music=pygame.mixer.music.load('music/music.mp3')
pygame.mixer.music.play(1)

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
	self.hitbox = (self.x + 50,self.y,60,100)
	self.health = 10
	self.visible = True
    	self.flag = 0
    def draw(self, win):
	if self.visible:        
		if self.walkCount + 1 >= 27:
		    self.walkCount = 0

		if not(self.standing):
		    if self.left:
		        win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
		        self.walkCount += 1
		    elif self.right:
		        win.blit(walkRight[self.walkCount//3], (self.x,self.y))
		        self.walkCount +=1
		else:
		    if self.right:
		        win.blit(walkRight[0], (self.x, self.y))
		    else:
		        win.blit(walkLeft[0], (self.x, self.y))
		pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
		pygame.draw.rect(win,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,50 - (5 * (10-int(self.health))),10))
		self.hitbox = (self.x + 23,self.y + 20,45,80)
		pygame.draw.rect(win ,(255,0,0) ,self.hitbox , 2)

    def hit(self):
	if(self.health>0):
		self.health -= 1
	else:
		font=pygame.font.SysFont("Comic Sans Ms",30)
		msg=font.render("You lose",False,(255,0,0))
		win.blit(msg,(675,550))
		pygame.time.delay(100)
		run=0

class projectile(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 20 
    def draw(self,win):
    		pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
class enemy(object): 
	def __init__(self,x,y,radius,colour):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = colour
		self.xend = 1450
		self.yend = 660
		self.ypath = [self.y,self.yend]
		self.xpath = [0,self.xend]	
		self.yvel = 1
		self.xvel = 4		
		self.walkcount =0	
		self.hitbox = ((self.x+self.radius + 10,self.y+self.radius + 10),self.radius + 10)
		self.flag=1		
		self.index=len(pballs)-1
		self.pballs=0
		self.ball = [bubbles[4 - (self.radius//20)]]
	def draw(self,win):
		self.ymove()
		self.xmove()
		if self.flag==1:
			 for bullet in bullets:
				if (bullet.y - bullet.radius < self.hitbox[0][1] +self.hitbox[1] and bullet.y + bullet.radius > self.hitbox[0][1]):
					if(bullet.x + bullet.radius > self.hitbox[0][0] - self.hitbox[1] and bullet.x - bullet.radius < self.hitbox[0][0] + balls[self.index].hitbox[1] - 10):
						balls[self.index].hit(self.index,self.x,self.y,self.radius)
    						del bullets[0]
			 if self.walkcount + 1 >=1:
				self.walkcount=0
			 if self.yvel>0:
				win.blit(self.ball[self.walkcount//4], (self.x,self.y))
				self.walkcount += 1
		 	 else:
				win.blit(self.ball[self.walkcount//4], (self.x,self.y))
				self.walkcount += 1
			 self.hitbox = ((self.x+self.radius + 10,self.y+self.radius + 10),self.radius + 10)	  
    			 if balls[self.index].y - balls[self.index].radius < man.hitbox[1] + man.hitbox[3] and balls[self.index].y + balls[self.index].radius > man.hitbox[1]:
			 	if balls[self.index].x + balls[self.index].radius > man.hitbox[0] - 35 and balls[self.index].x - balls[self.index].radius < man.hitbox[0] - man.hitbox[2] - 30:		
			 		man.hit()  
			 for bullet in bullets:
			  	if (bullet.y - bullet.radius < balls[self.index].hitbox[0][1] + balls[self.index].hitbox[1] and bullet.y + bullet.radius > balls[self.index].hitbox[0][1]):
					if(bullet.x + bullet.radius > balls[self.index].hitbox[0][0] - balls[self.index].hitbox[1] and bullet.x - bullet.radius < balls[self.index].hitbox[0][0] + balls[self.index].hitbox[1] - 10):
						balls[self.index].hit(self.index,balls[self.index].x,balls[self.index].y,balls[self.index].radius)
    						bullets.pop(bullets.index(bullet))
			 #pygame.draw.circle(win,self.colour,(self.x+66,self.y+70),56,2)
	def ymove(self):
		if self.yvel>=0:
			if self.y + self.radius < self.ypath[1]:
				self.y +=self.yvel 
            			self.yvel = self.yvel + 2 * self.walkcount
			else:										
				self.yvel=self.yvel*-1
		else:
			if self.y > self.ypath[0]:
				self.y +=self.yvel 
            			self.yvel = self.yvel + 2 * self.walkcount	
			else:		
				self.yvel=-2				
				self.yvel=self.yvel*-1
	def xmove(self):
		if self.xvel>0:
			if self.x + 120 < self.xpath[1]:
				self.x += self.xvel
			
			else:
				self.xvel=self.xvel*-1
				self.walkcount=0
		else:
			if self.x > self.xpath[0]:
				self.x += self.xvel
			else:
				self.xvel=self.xvel*-1
				self.walkcount=0
	def hit(self,i,x,y,r):
		balls[i].flag=0
		print('hit')
		if balls[i].radius>20:
			createballs(i,x,y,r)


pballs=[]
pballs.append(1)
balls=list()
balls.append(enemy(200,150,80,(0,0,0)))

def createballs(i,x,y,r):
	
        pballs.append(1)
	balls.append(enemy(x,y,r-20,(0,0,0)))
	pballs.append(1)
	balls.append(enemy(x,y,r-20,(0,0,0)))
	j=len(pballs)
	balls[j-1].pballs=balls[j-1].pballs+1
	balls[j-2].pballs=balls[j-2].pballs+1
	balls[j-1].xvel=-1*(balls[j-2].xvel)
	
def gameintro():
	intro = True
	while intro:
		for event in pygame.event.get():
			print(event)
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

	gameDisplat.fill((0,0,255))
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects("Bubble TROUBLE", largeText)
	TextRect.center = ((display_500/2), (display_360/2))
	gamedisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	clock.tick(15)
	
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    for i in balls:
	i.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()

bullets=[]
#mainloop
man = player(200, 600, 64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y < 800 and bullet.y > 0:	            
		bullet.y -= bullet.vel
        else:
        	if len(bullets)!=0:
			del bullets[0]
	
  
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 1:
             bullets.append(projectile(int(man.x) + int(man.width)//2,int(man.y) + int(man.height)//2, 6, (0,0,0)))
    
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1450 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()


pygame.quit()


