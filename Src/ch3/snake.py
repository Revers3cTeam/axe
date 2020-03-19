import math
import random
import pygame
import random
import tkinter as tk
from tkinter import messagebox
from time import sleep
pygame.init()
pygame.font.init()
width = 530
height = 500

cols = 25
rows = 20
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
flag = ['J', 'T', 'H', 'f', '#', 'L', 'Z', '*', 'D', ':', '7', 'W', 'U', 
        ':', '+', 'A', '#', '[', 'E', 'F', '?', 'J', 'J', '"', '?', 'x']



class Cube():
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255,255,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny # "L", "R", "U", "D"
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos  = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
            

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
        


class Snake():
    body = []
    turns = {}
    
    def __init__(self, color, pos):
        #pos is given as coordinates on the grid ex (1,5)
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirny = -1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirny = 1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx,c.dirny)
        
        
    def reset(self,pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
    
    def draw(self, surface):
        for i,c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)



def redrawWindow():
	global win
	global flag
	win.fill((0,0,0))
	drawGrid(width, rows, win)
	s.draw(win)
	snack.draw(win)
	font = pygame.font.SysFont('arial', 40)
	text = font.render("".join(flag), True, green) 
	textRect = text.get_rect()
	win.blit(text, textRect) 
	pygame.display.update()
	pass



def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y +sizeBtwn

        pygame.draw.line(surface, (0,0,0), (x, 0),(x,w))
        pygame.draw.line(surface, (0,0,0), (0, y),(w,y))
    


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(1,rows-1)
        y = random.randrange(1,rows-1)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
               continue
        else:
               break

    return (x,y)


def main():
	try:
		global s, snack, win,heights
		win = pygame.display.set_mode((width,height))
		pygame.display.set_caption('SNEAKY PETE') 

		s = Snake((255,0,0), (10,10))
		s.addCube()
		snack = Cube(randomSnack(rows,s), color=(0,255,0))
		clock = pygame.time.Clock()
		counter = 1
		couback = -1
		global flag
		keys = []
		for i in range(1,27):
			keys.append((19*i)%26)
		while True:
			pygame.time.delay(50)
			clock.tick(10+len(s.body))
			s.move()
			headPos = s.head.pos
			if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
				flag = ['J', 'T', 'H', 'f', '#', 'L', 'Z', '*', 'D', ':', '7', 'W', 'U', 
						':', '+', 'A', '#', '[', 'E', 'F', '?', 'J', 'J', '"', '?', 'x']
				couback = -1
				s.reset((10, 10))

			if s.body[0].pos == snack.pos:
				s.addCube() 
				snack = Cube(randomSnack(rows,s), color=(0,255,0))
				if (19*counter) == len(s.body):   
					if couback == -(len(flag)+1):
						while True:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
									quit()
							clock.tick(15)
					counter += 1 
					flag[couback] = chr(ord(flag[couback]) ^ ((19*(27  + couback))%26 + 5))           
					couback -= 1
			for x in range(len(s.body)):
			    if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
			        flag = ['J', 'T', 'H', 'f', '#', 'L', 'Z', '*', 'D', ':', '7', 'W', 'U', 
	        				':', '+', 'A', '#', '[', 'E', 'F', '?', 'J', 'J', '"', '?', 'x']
	        		couback = -1
			        s.reset((10,10))
			        break
		                
			redrawWindow()
	except:
		pass
main()
    

    