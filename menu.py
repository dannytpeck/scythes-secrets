"""
   Scythe's Secrets (Working Title)
   By Danny Peck dannytpeck@gmail.com
   https://github.com/dannytpeck/scythes-secrets

   Main Menu File
"""

import pygame, game
 
# Constants

# Colors
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GRAY	= (  51,  51,  51)
YELLOW  = ( 255, 255, 153)

# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 800


def main():
	""" Main Program """

	# Initialize the Pygame library 
	pygame.init()

	# Set the height and width of the screen
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])	

	# Set the title of the window
	pygame.display.set_caption("Scythe's Secrets")

	# Create the menu object
	menu = Menu(screen)

	display = Display(screen)
	
	clock = pygame.time.Clock()

	done = False	
	
	while not done:
	
		# --- Main event loop
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					menu.change_selection(-1)
				if event.key == pygame.K_DOWN:
					menu.change_selection(1)
				if event.key == pygame.K_RETURN:
					if menu.get_selection() == 0:
						print("Start Game!")
						intro()						
					if menu.get_selection() == 1:
						print("Options!")
						display.dialog_box(["This is a test box. This is a test box. This is a test box.", 
											"This is a test box. This is a test box. This is a test box.",
											"This is a test box. This is a test box. This is a test box.",
											"This is a test box. This is a test box. This is a test box.",
											"This is a test box. This is a test box. This is a test box."], screen)
					if menu.get_selection() == 2:
						done = True
				if event.key == pygame.K_ESCAPE:
					done = True
			
		# --- Game logic should go here
 
		# --- Drawing ---
		screen.fill(WHITE) # Draw white background
		menu.draw() # Draw the menu

		# Limit to 60 fps
		clock.tick(60)		
		
		# --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
 
	pygame.quit()


class Menu():
	""" This class is for the menu """
	item_selection = 0	

	# Initialize the Pygame library 
	pygame.init()	

	font_path = 'kenpixel.ttf'
	font_size = 32
	font = pygame.font.Font(font_path, font_size)
	
	background_color = (51, 51, 51)
	text_color = (255, 255, 153)
	selection_color = (153, 102, 255)
	
	def __init__(self, screen):
		""" Constructor function """
		self.screen = screen
	
	def set_colors(self, text, selection, background):
		""" Change the menu's colors """
		self.background_color = background
		self.text_color = text
		self.selection_color = selection
		
	def set_fontsize(self, font_size):
		""" Change the menu's font """
		self.font_size = font_size

	def get_selection(self):
		return self.item_selection
		
	def change_selection(self, move):
		""" Change selected item on the menu """
		self.item_selection += move
		
		if self.item_selection < 0:
			self.item_selection = 2
			
		if self.item_selection > 2:
			self.item_selection = 0

	def draw(self):
		""" Draw the menu """
		
		# Menu background
		square = pygame.Surface([400, 400])
		square.fill(self.background_color)
		self.screen.blit(square, [200, 225])

		# Menu text
		if self.item_selection == 0: 
			text = self.font.render("Start", True, self.text_color, self.selection_color)
		else:
			text = self.font.render("Start", True, self.text_color)
		self.screen.blit(text, [300, 300])

		if self.item_selection == 1: 
			text = self.font.render("Options", True, self.text_color, self.selection_color)
		else:
			text = self.font.render("Options", True, self.text_color)
		self.screen.blit(text, [300, 400])

		if self.item_selection == 2: 
			text = self.font.render("Quit", True, self.text_color, self.selection_color)
		else:
			text = self.font.render("Quit", True, self.text_color)
		self.screen.blit(text, [300, 500])

		
class Display():
	""" This class is for the HUD stuff """	
	background_color = (0, 0, 0)
	text_color = (255, 255, 255)
	
	def __init__(self, screen):
		""" Constructor function """
		self.screen = screen

	def draw_text(self, text_list, screen):
		font_path = 'coders_crux.ttf'
		font_size = 32

		f = pygame.font.Font(font_path, font_size)

		# save the rendered text
		self.text_overlay = [f.render(i, 1, self.text_color) for i in text_list]		
		
		y = 0
		for text in self.text_overlay:
			screen.blit(text, (self.margin*2, self.margin*2+y))
			y += text.get_height()		
		
	def dialog_box(self, dialog, screen):
		""" Pop up a dialogue box on the screen """
		self.margin = 10
		
		clock = pygame.time.Clock()	
		
		done = False
		
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					done = True 
			
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						done = True					
					if event.key == pygame.K_ESCAPE:
						done = True
					if event.key == pygame.K_a:
						done = True
						
			# Make the box
			square = pygame.Surface([SCREEN_WIDTH - self.margin * 2, 130])
			square.fill(self.background_color)
			screen.blit(square, [self.margin, self.margin])

			self.draw_text(dialog, screen)
			#self.draw_text(["This is line one of the text box", "and this is line two."], screen)
				
			# 60 fps
			clock.tick(60)		
			pygame.display.flip()
			
	
def intro():
	""" Display the scrolling text intro """
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])	

	x = 0
	y = 700	
	
	clock = pygame.time.Clock()

	# Load and set up graphics.
	intro_text_image = pygame.image.load("intro.png").convert()
	intro_text_image.set_colorkey(WHITE)

	done = False
	
	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					done = True
					game.main()
				if event.key == pygame.K_ESCAPE:
					done = True
					game.main()

		screen.fill(WHITE) # Draw white background

		screen.blit(intro_text_image, [x, y])	
		
		# text crawls upward
		y -= 1
		
		# 60 fps
		clock.tick(60)		
		pygame.display.flip()
		
	
if __name__ == "__main__":
    main()
	