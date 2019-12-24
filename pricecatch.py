#btc price catcher
import requests
import json
import time
import pygame, sys



pygame.init()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0)
red = (255, 0, 0)
currency = input("which currency would you like? f.e. 'EUR'")
#last = input("which price would you like? f.e. 'last' or 'buy'")


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("BTCPRICE " + currency + " " + "last")
pricesvar = 0

font = pygame.font.Font('freesansbold.ttf', 100)
font1 = pygame.font.Font('freesansbold.ttf', 80)
font2 = pygame.font.Font('freesansbold.ttf', 60)
font3 = pygame.font.Font('freesansbold.ttf', 40)
screen.fill(white)
oldvalue = 0

color1 = red
color2 = red
color3 = red
color4 = red


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('gray.png', [0,0])

Priceslist = [0,0,0,0,0]

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	prices = requests.get("https://blockchain.info/ticker")
	jsontext = prices.text
	parsed_json= json.loads(jsontext)
	value = float(parsed_json[currency]["last"])
	print(value)



	Priceslist.insert(0, oldvalue)

	if value > oldvalue:
		color = green
	else:
		color = red

	#check if value has changed since last check
	if oldvalue == value:
		print(value)
		time.sleep(30)
	#if value has changed, fill the screen with blue and redraw
	else:
		screen.fill([0, 0, 0])
		screen.blit(BackGround.image, BackGround.rect)
		pricesvar = value

		text = font.render(str(parsed_json[currency]["last"]), True, color, None) 
		textRect = text.get_rect()
		textRect.center = (640 * 0.65, 480 * 0.85)


		text1 = font1.render(str(Priceslist[0]), True, color1, None) 
		text1Rect = text1.get_rect()
		text1Rect.center = (640 * 0.65, 480 * 0.65)



		text2 = font2.render(str(Priceslist[1]), True, color2, None) 
		text2Rect = text2.get_rect()
		text2Rect.center = (640 * 0.65, 480 * 0.53)



		text3 = font3.render(str(Priceslist[2]), True, color3, None) 
		text3Rect = text3.get_rect()
		text3Rect.center = (640 * 0.65, 480 * 0.44)

		"""buytext = font.render(int(parsed_json["EUR"]["buy"]), True, green, None) 
		buytextRect = buytext.get_rect()
		buytextRect.center = (640 * 0.7, 480 * 0.15)

		selltext = font.render(int(parsed_json["EUR"]["sell"]), True, red, None) 
		selltextRect = selltext.get_rect()
		selltextRect.center = (640 * 0.7, 480 * 0.85)"""

		screen.blit(text, textRect)
		"""screen.blit(buytext, buytextRect)
		screen.blit(selltext, selltextRect)"""
		screen.blit(text1, text1Rect)
		screen.blit(text2, text2Rect)
		screen.blit(text3, text3Rect)
		pygame.display.update()
		time.sleep(60)
		#solid blocks
	oldvalue = value 
	color4 = color3
	color3 = color2
	color2 = color1
	color1 = color

	









