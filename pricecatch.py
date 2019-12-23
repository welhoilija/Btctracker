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
currency = "EUR"
last = "last"


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("BTCPRICE" + currency + last)
pricesvar = 0

font = pygame.font.Font('freesansbold.ttf', 100)
screen.fill(white)
oldvalue = 0




class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('Untitled.jpg', [0,0])



while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	prices = requests.get("https://blockchain.info/ticker")
	jsontext = prices.text
	parsed_json= json.loads(jsontext)
	value = str(parsed_json["EUR"]["last"])
	print(value)

	

	#check if value has changed since last check
	if oldvalue == value:
		print(value)
		time.sleep(30)
	#if value has changed, fill the screen with blue and redraw
	else:
		screen.fill([255, 255, 255])
		screen.blit(BackGround.image, BackGround.rect)
		pricesvar = value

		text = font.render(pricesvar, True, black, None) 
		textRect = text.get_rect()
		textRect.center = (640 * 0.7, 480 // 2)

		buytext = font.render(str(parsed_json["EUR"]["buy"]), True, green, None) 
		buytextRect = buytext.get_rect()
		buytextRect.center = (640 * 0.7, 480 * 0.15)

		selltext = font.render(str(parsed_json["EUR"]["sell"]), True, red, None) 
		selltextRect = selltext.get_rect()
		selltextRect.center = (640 * 0.7, 480 * 0.85)

		screen.blit(text, textRect)
		screen.blit(buytext, buytextRect)
		screen.blit(selltext, selltextRect)
		pygame.display.update()
		time.sleep(30)
		#solid blocks

	









