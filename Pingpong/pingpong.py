import pygame,sys, random
from settings import *
from configurations import *

def ball_animation():
	global ball_speed_x, ball_speed_y, player_score,opponent_score, score_time

	ball.x +=ball_speed_x
	ball.y +=ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1

	if ball.left <= 0: 
		player_score += 1
		score_time = pygame.time.get_ticks()

	if ball.right >= screen_width:
		opponent_score += 1
		score_time = pygame.time.get_ticks()

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x*=-1

def player_animation():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opponent_animation():

	if opponent.top < ball.y:
		opponent.y += opponent_speed

	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0

	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_start():

	global ball_speed_x, ball_speed_y, score_time

	current_time = pygame.time.get_ticks()
	ball.center =(screen_width/2,screen_height/2)

	if current_time - score_time < 700:
		number_three = game_font.render("3", False, light_red)
		screen.blit(number_three, (screen_width/2 -10, screen_height/2 +20))
	
	if 700<current_time - score_time < 1200:
		number_two = game_font.render("2", False, light_red)
		screen.blit(number_two, (screen_width/2 -10, screen_height/2 +20))

	if 700<current_time - score_time < 1400:
		number_one = game_font.render("1", False, light_red)
		screen.blit(number_one, (screen_width/2 -10, screen_height/2 +20))		

	if current_time - score_time < 2100:
		ball_speed_x , ball_speed_y = 0,0
	else:
		ball_speed_x = 7 * random.choice((1,-1))
		ball_speed_y = 7 * random.choice ((1,-1))
		score_time = None



def colors():
	global bg_color, bg_color1, bg_color2
	bg_color=pygame.Color("white")
	bg_color1=pygame.Color("red")
	bg_color2=pygame.Color("blue")
	bg_color3=pygame.Color("black")


def music():
	pygame.mixer.music.load('musicaepica.mp3')
	pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
	pygame.mixer.music.play()
    



pygame.init()
clock=pygame.time.Clock()
music()

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(Title)

#game rectangles

ball=pygame.Rect(screen_width/2-15, screen_height/2-15,30,30)
player=pygame.Rect(screen_width-20,screen_height/2-70,10,140)
opponent=pygame.Rect(10,screen_height/2-70,10,140)

ball_speed_x= 7 * random.choice((1,-1))
ball_speed_y= 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7


game_font= pygame.font.Font(font, size)

#score timer

score_time = True


while True:
#handign input
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed += 6
			if event.key == pygame.K_DOWN:
				player_speed -= 6

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed -= 6
			if event.key == pygame.K_DOWN:
				player_speed += 6

	ball_animation()
	player_animation()
	opponent_animation()
	colors()
	

#visuals
	screen.fill(bg_color)
	pygame.draw.rect(screen,light_blue,player)
	pygame.draw.rect(screen,light_blue,opponent)
	pygame.draw.ellipse(screen,light_red,ball)
	pygame.draw.aaline(screen,light_black,(screen_width/2,0),(screen_width/2,screen_height))

	if score_time:
		ball_start()

	player_text=game_font.render(f"{player_score}",False,light_black)
	screen.blit(player_text, (440,170))

	opponent_text=game_font.render(f"{opponent_score}",False,light_black)
	screen.blit(opponent_text, (500,170))


#updating the window
	pygame.display.update()
	clock.tick(60)
