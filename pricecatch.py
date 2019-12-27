#btc price catcher
import requests
import json
import time
import pygame, sys



pygame.init()

white = (255, 255, 255) 
blue = (0, 0, 128) 
black = (0, 0, 0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

currency = "EUR"
oldcurrency = currency
#last = input("which price would you like? f.e. 'last' or 'buy'")


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("BTCPRICE " + currency + " " + "last")
pricesvar = 0

font = pygame.font.Font('freesansbold.ttf', 100)
font1 = pygame.font.SysFont('ubuntu.ttf', 80)
font2 = pygame.font.SysFont('ubuntu.ttf', 40)

screen.fill(white)
oldvalue = 0
color = green
color1 = red
color2 = red
color3 = red
color4 = red
oldtime = time.time() - 60
value = 0


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def drawtext(value, x, y, font, color):
	text = font.render(value, True, color, None) 
	textRect = text.get_rect()
	textRect.center = (x, y)
	screen.blit(text, textRect)


BackGround = Background('gray.png', [0,0])

EURPriceslist = [0,0,0,0,0]

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


	mouse = pygame.mouse.get_pos()

	print(mouse)
	



	#checks if a minute has passed, if it has run the numbers again
	if time.time() - oldtime > 60 or currency != oldcurrency:
		print("its been a minute")
		prices = requests.get("https://blockchain.info/ticker")
		parsed_json= json.loads(prices.text)
		value = float(parsed_json[currency]["last"])
		print(value)
		EURPriceslist.insert(0, value)

		if value > oldvalue:
			color = green
		else:
			color = red



		#Checks if the price is still same, if it is , dont draw anything
		if oldvalue == value:
			print(value)



			
		else:
			screen.fill([0, 0, 0])
			screen.blit(BackGround.image, BackGround.rect)

			drawtext(str(EURPriceslist[0]), 640 * 0.65, 480 * 0.90, font, color)

			drawtext(currency + "/BTC", 640 * 0.15, 480 * 0.90, font2, green)

			drawtext(str(EURPriceslist[1]), 640 * 0.65, 480 * 0.68, font1, color1)

			drawtext(str(EURPriceslist[2]), 640 * 0.65, 480 * 0.54, font1, color2)

			drawtext(str(EURPriceslist[3]), 640 * 0.65, 480 * 0.40, font1, color3)

			



			


		oldtime = time.time()
		oldvalue = value
		color4 = color3
		color3 = color2
		color2 = color1
		color1 = color
		oldcurrency = currency



	if 168 > mouse[0] > 19 and 98 > mouse[1] > 69 and pygame.mouse.get_pressed() == (1, 0, 0):
		pygame.draw.rect(screen, bright_green, (18, 68, 152, 29))
		currency = "USD"
	else:
		pygame.draw.rect(screen, green, (18, 68, 152, 29))
	drawtext("USD", 95, 83, font2, red)


	if 168 > mouse[0] > 19 and 130 > mouse[1] > 99 and pygame.mouse.get_pressed() == (1, 0, 0):
		pygame.draw.rect(screen, bright_green, (18, 100, 152, 29))
		currency = "EUR"
	else:
		pygame.draw.rect(screen, green, (18, 100, 152, 29))
	drawtext("EUR", 95, 117, font2, red)







	pygame.display.update()
		





	









