import pygame
import random

pygame.init()
win_size = 720
offset = 300
win = pygame.display.set_mode(((win_size + offset) * 2 - 14, win_size))
pygame.display.set_caption("Codenames")
clock = pygame.time.Clock()

logo = pygame.image.load('codenames-13.png')
xx = pygame.image.load('x.png')

sqW = win_size/5 - 6
sqG = 3
show_all = False
font_name = pygame.font.match_font('arial')

def topleft_text(surf, text, size, x, y, colour):
		font = pygame.font.Font(font_name, size)
		text_surface = font.render(text, True, (colour))
		text_rect = text_surface.get_rect()
		text_rect.topleft = (x, y)
		surf.blit(text_surface, text_rect)

def draw():
		pygame.draw.rect(win, (0, 0, 0), (0,0,(win_size + offset) * 2,win_size))
		
		#draw codeguesser grid
		printX = 0
		printY = 0
		for row in color_grid:
			for sq in row:
				pygame.draw.rect(win, (255,255,255), (printX * win_size/5 + sqG, printY * win_size/5 + sqG, sqW, sqW))
				if shown_grid[printY][printX] == 1:
					if sq == 0:
						pygame.draw.rect(win, (255, 222, 173), (printX * win_size/5 + sqG, printY * win_size/5 + sqG, sqW, sqW))
					if sq == 1:
						pygame.draw.rect(win, (100, 100, 255), (printX * win_size/5 + sqG, printY * win_size/5 + sqG, sqW, sqW))
					if sq == 2:
						pygame.draw.rect(win, (255, 100, 100), (printX * win_size/5 + sqG, printY * win_size/5 + sqG, sqW, sqW))
					if sq == 3:
						pygame.draw.rect(win, (100, 100, 100), (printX * win_size/5 + sqG, printY * win_size/5 + sqG, sqW, sqW))

				topleft_text(win, (word_grid[printY][printX]), 20, printX * win_size/5 + sqG + 2, printY * win_size/5 + sqG + 2, (0, 0, 0))
					
				printX += 1
			printY += 1
			printX = 0

		pygame.draw.rect(win, (255, 255, 255), (win_size + sqG,sqG,offset - 20, win_size - sqG * 2))
		win.blit(logo, (win_size + offset - 130, 0))

		counted = 10
		for i in range(red_left):
			pygame.draw.rect(win, (255, 100, 100), (win_size + 10, counted, 40, 40))
			counted += 50

		counted = 10
		for i in range(blue_left):
			pygame.draw.rect(win, (100, 100, 255), (win_size + 10 + 50, counted, 40, 40))
			counted += 50

		counted = 10
		for i in range(yellow_left):
			pygame.draw.rect(win, (255, 222, 173), (win_size + 10 + 100, counted, 40, 40))
			counted += 50

		#draw codemaker grid
		printX = 0
		printY = 0
		for row in color_grid:
			for sq in row:
				if sq == 0:
					pygame.draw.rect(win, (255, 222, 173), (printX * win_size/5 + sqG + win_size + offset, printY * win_size/5 + sqG, sqW, sqW))
				if sq == 1:
					pygame.draw.rect(win, (100, 100, 255), (printX * win_size/5 + sqG + win_size + offset, printY * win_size/5 + sqG, sqW, sqW))
				if sq == 2:
					pygame.draw.rect(win, (255, 100, 100), (printX * win_size/5 + sqG + win_size + offset, printY * win_size/5 + sqG, sqW, sqW))
				if sq == 3:
					pygame.draw.rect(win, (100, 100, 100), (printX * win_size/5 + sqG + win_size + offset, printY * win_size/5 + sqG, sqW, sqW))

				if shown_grid[printY][printX] == 1:
					#pygame.draw.rect(win, (0, 0, 0), (printX * win_size/5 + sqG + win_size + offset + 90, printY * win_size/5 + sqG + 90, sqW - 100, sqW - 100))
					win.blit(xx,(printX * win_size/5 + sqG + win_size + offset +32, printY * win_size/5 + sqG + 15))
				
				topleft_text(win, (word_grid[printY][printX]), 20, printX * win_size/5 + sqG + 2 + win_size + offset, printY * win_size/5 + sqG + 2, (0, 0, 0))

				printX += 1
			printY += 1
			printX = 0

		pygame.draw.rect(win, (255, 255, 255), (win_size + sqG + win_size + offset,sqG,offset - 20, win_size - sqG * 2))
		win.blit(logo, (win_size * 2 + offset * 2 - 130, 0))

		counted = 10
		for i in range(red_left):
			pygame.draw.rect(win, (255, 100, 100), (win_size + 10 + win_size + offset, counted, 40, 40))
			counted += 50

		counted = 10
		for i in range(blue_left):
			pygame.draw.rect(win, (100, 100, 255), (win_size + 10 + 50 + win_size + offset, counted, 40, 40))
			counted += 50

		counted = 10
		for i in range(yellow_left):
			pygame.draw.rect(win, (255, 222, 173), (win_size + 10 + 100 + win_size + offset, counted, 40, 40))
			counted += 50



		pygame.display.update()

while True:
	#generate word grid
	word_list = ["Hollywood","Well","Foot","New","York","Spring","Court","Tube","Point","Tablet","Slip","Date","Drill","Lemon","Bell","Screen","Fair","Torch","State","Match","Iron","Block","France","Australia","Limousine","Stream","Glove","Nurse","Leprechaun","Play","Tooth","Arm","Bermuda","Diamond","Whale","Comic","Mammoth","Green","Pass","Missile","Paste","Drop","Pheonix","Marble","Staff","Figure","Park","Centaur","Shadow","Fish","Cotton","Egypt","Theater","Scale","Fall","Track","Force","Dinosaur","Bill","Mine","Turkey","March","Contract","Bridge","Robin","Line","Plate","Band","Fire","Bank","Boom","Cat","Shot","Suit","Chocolate","Roulette","Mercury","Moon","Net","Lawyer","Satellite","Angel","Spider","Germany","Fork","Pitch","King","Crane","Trip","Dog","Conductor","Part","Bugle","Witch","Ketchup","Press","Spine","Worm","Alps","Bond","Pan","Beijing","Racket","Cross","Seal","Aztec","Maple","Parachute","Hotel","Berry","Soldier","Ray","Post","Greece","Square","Mass","Bat","Wave","Car","Smuggler","England","Crash","Tail","Card","Horn","Capital","Fence","Deck","Buffalo","Microscope","Jet","Duck","Ring","Train","Field","Gold","Tick","Check","Queen","Strike","Kangaroo","Spike","Scientist","Engine","Shakespeare","Wind","Kid","Embassy","Robot","Note","Ground","Draft","Ham","War","Mouse","Center","Chick","China","Bolt","Spot","Piano","Pupil","Plot","Lion","Police","Head","Litter","Concert","Mug","Vacuum","Atlantis","Straw","Switch","Skyscraper","Laser","Scuba","Diver","Africa","Plastic","Dwarf","Lap","Life","Honey","Horseshoe","Unicorn","Spy","Pants","Wall","Paper","Sound","Ice","Tag","Web","Fan","Orange","Temple","Canada","Scorpion","Undertaker","Mail","Europe","Soul","Apple","Pole","Tap","Mouth","Ambulance","Dress","Ice","Cream","Rabbit","Buck","Agent","Sock","Nut","Boot","Ghost","Oil","Superhero","Code","Kiwi","Hospital","Saturn","Film","Button","Snowman","Helicopter","Loch","Ness","Log","Princess","Time","Cook","Revolution","Shoe","Mole","Spell","Grass","Washer","Game","Beat","Hole","Horse","Pirate","Link","Dance","Fly","Pit","Server","School","Lock","Brush","Pool","Star","Jam","Organ","Berlin","Face","Luck","Amazon","Cast","Gas","Club","Sink","Water","Chair","Shark","Jupiter","Copper","Jack","Platypus","Stick","Olive","Grace","Bear","Glass","Row","Pistol","London","Rock","Van","Vet","Beach","Charge","Port","Disease","Palm","Moscow","Pin","Washington","Pyramid","Opera","Casino","Pilot","String","Night","Chest","Yard","Teacher","Pumpkin","Thief","Bark","Bug","Mint","Cycle","Telescope","Calf","Air","Box","Mount","Thumb","Antarctica","Trunk","Snow","Penguin","Root","Bar","File","Hawk","Battery","Compound","Slug","Octopus","Whip","America","Ivory","Pound","Sub","Cliff","Lab","Eagle","Genius","Ship","Dice","Hood","Heart","Novel","Pipe","Himalayas","Crown","Round","India","Needle","Shop","Watch","Lead","Tie","Table","Cell","Cover","Czech","Back","Bomb","Ruler","Forest","Bottle","Space","Hook","Doctor","Ball","Bow","Degree","Rome","Plane","Giant","Nail","Dragon","Stadium","Flute","Carrot","Wake","Fighter","Model","Tokyo","Eye","Mexico","Hand","Swing","Key","Alien","Tower","Poison","Cricket","Cold","Knife","Church","Board","Cloak","Ninja","Olympus","Belt","Light","Death","Stock","Millionaire","Day","Knight","Pie","Bed","Circle","Rose","Change","Cap","Triangle"]
	word_list2 = ["Acne","Acre","Addendum","Advertise","Aircraft","Aisle","Alligator","Alphabetize","America","Ankle","Apathy","Applause","Applesauc","Application","Archaeologist","Aristocrat","Arm","Armada","Asleep","Astronaut","Athlete","Atlantis","Aunt","Avocado","Baby-Sitter","Backbone","Bag","Baguette","Bald","Balloon","Banana","Banister","Baseball","Baseboards","Basketball","Bat","Battery","Beach","Beanstalk","Bedbug","Beer","Beethoven","Belt","Bib","Bicycle","Big","Bike","Billboard","Bird","Birthday","Bite","Blacksmith","Blanket","Bleach","Blimp","Blossom","Blueprint","Blunt","Blur","Boa","Boat","Bob","Bobsled","Body","Bomb","Bonnet","Book","Booth","Bowtie","Box","Boy","Brainstorm","Brand","Brave","Bride","Bridge","Broccoli","Broken","Broom","Bruise","Brunette","Bubble","Buddy","Buffalo","Bulb","Bunny","Bus","Buy","Cabin","Cafeteria","Cake","Calculator","Campsite","Can","Canada","Candle","Candy","Cape","Capitalism","Car","Cardboard","Cartography","Cat","Cd","Ceiling","Cell","Century","Chair","Chalk","Champion","Charger","Cheerleader","Chef","Chess","Chew","Chicken","Chime","China","Chocolate","Church","Circus","Clay","Cliff","Cloak","Clockwork","Clown","Clue","Coach","Coal","Coaster","Cog","Cold","College","Comfort","Computer","Cone","Constrictor","Continuum","Conversation","Cook","Coop","Cord","Corduroy","Cot","Cough","Cow","Cowboy","Crayon","Cream","Crisp","Criticize","Crow","Cruise","Crumb","Crust","Cuff","Curtain","Cuticle","Czar","Dad","Dart","Dawn","Day","Deep","Defect","Dent","Dentist","Desk","Dictionary","Dimple","Dirty","Dismantle","Ditch","Diver","Doctor","Dog","Doghouse","Doll","Dominoes","Door","Dot","Drain","Draw","Dream","Dress","Drink","Drip","Drums","Dryer","Duck","Dump","Dunk","Dust","Ear","Eat","Ebony","Elbow","Electricity","Elephant","Elevator","Elf","Elm","Engine","England","Ergonomic","Escalator","Eureka","Europe","Evolution","Extension","Eyebrow","Fan","Fancy","Fast","Feast","Fence","Feudalism","Fiddle","Figment","Finger","Fire","First","Fishing","Fix","Fizz","Flagpole","Flannel","Flashlight","Flock","Flotsam","Flower","Flu","Flush","Flutter","Fog","Foil","Football","Forehead","Forever","Fortnight","France","Freckle","Freight","Fringe","Frog","Frown","Gallop","Game","Garbage","Garden","Gasoline","Gem","Ginger","Gingerbread","Girl","Glasses","Goblin","Gold","Goodbye","Grandpa","Grape","Grass","Gratitude","Gray","Green","Guitar","Gum","Gumball","Hair","Half","Handle","Handwriting","Hang","Happy","Hat","Hatch","Headache","Heart","Hedge","Helicopter","Hem","Hide","Hill","Hockey","Homework","Honk","Hopscotch","Horse","Hose","Hot","House","Houseboat","Hug","Humidifier","Hungry","Hurdle","Hurt","Hut","Ice","Implode","Inn","Inquisition","Intern","Internet","Invitation","Ironic","Ivory","Ivy","Jade","Japan","Jeans","Jelly","Jet","Jig","Jog","Journal","Jump","Key","Killer","Kilogram","King","Kitchen","Kite","Knee","Kneel","Knife","Knight","Koala","Lace","Ladder","Ladybug","Lag","Landfill","Lap","Laugh","Laundry","Law","Lawn","Lawnmower","Leak","Leg","Letter","Level","Lifestyle","Ligament","Light","Lightsaber","Lime","Lion","Lizard","Log","Loiterer","Lollipop","Loveseat","Loyalty","Lunch","Lunchbox","Lyrics","Machine","Macho","Mailbox","Mammoth","Mark","Mars","Mascot","Mast","Matchstick","Mate","Mattress","Mess","Mexico","Midsummer","Mine","Mistake","Modern","Mold","Mom","Monday","Money","Monitor","Monster","Mooch","Moon","Mop","Moth","Motorcycle","Mountain","Mouse","Mower","Mud","Music","Mute","Nature","Negotiate","Neighbor","Nest","Neutron","Niece","Night","Nightmare","Nose","Oar","Observatory","Office","Oil","Old","Olympian","Opaque","Opener","Orbit","Organ","Organize","Outer","Outside","Ovation","Overture","Pail","Paint","Pajamas","Palace","Pants","Paper","Paper","Park","Parody","Party","Password","Pastry","Pawn","Pear","Pen","Pencil","Pendulum","Penis","Penny","Pepper","Personal","Philosopher","Phone","Photograph","Piano","Picnic","Pigpen","Pillow","Pilot","Pinch","Ping","Pinwheel","Pirate","Plaid","Plan","Plank","Plate","Platypus","Playground","Plow","Plumber","Pocket","Poem","Point","Pole","Pomp","Pong","Pool","Popsicle","Population","Portfolio","Positive","Post","Princess","Procrastinate","Protestant","Psychologist","Publisher","Punk","Puppet","Puppy","Push","Puzzle","Quarantine","Queen","Quicksand","Quiet","Race","Radio","Raft","Rag","Rainbow","Rainwater","Random","Ray","Recycle","Red","Regret","Reimbursement","Retaliate","Rib","Riddle","Rim","Rink","Roller","Room","Rose","Round","Roundabout","Rung","Runt","Rut","Sad","Safe","Salmon","Salt","Sandbox","Sandcastle","Sandwich","Sash","Satellite","Scar","Scared","School","Scoundrel","Scramble","Scuff","Seashell","Season","Sentence","Sequins","Set","Shaft","Shallow","Shampoo","Shark","Sheep","Sheets","Sheriff","Shipwreck","Shirt","Shoelace","Short","Shower","Shrink","Sick","Siesta","Silhouette","Singer","Sip","Skate","Skating","Ski","Slam","Sleep","Sling","Slow","Slump","Smith","Sneeze","Snow","Snuggle","Song","Space","Spare","Speakers","Spider","Spit","Sponge","Spool","Spoon","Spring","Sprinkler","Spy","Square","Squint","Stairs","Standing","Star","State","Stick","Stockholder","Stoplight","Stout","Stove","Stowaway","Straw","Stream","Streamline","Stripe","Student","Sun","Sunburn","Sushi","Swamp","Swarm","Sweater","Swimming","Swing","Tachometer","Talk","Taxi","Teacher","Teapot","Teenager","Telephone","Ten","Tennis","Thief","Think","Throne","Through","Thunder","Tide","Tiger","Time","Tinting","Tiptoe","Tiptop","Tired","Tissue","Toast","Toilet","Tool","Toothbrush","Tornado","Tournament","Tractor","Train","Trash","Treasure","Tree","Triangle","Trip","Truck","Tub","Tuba","Tutor","Television","Twang","Twig","Twitterpated","Type","Unemployed","Upgrade","Vest","Vision","Wag","Water","Watermelon","Wax","Wedding","Weed","Welder","Whatever","Wheelchair","Whiplash","Whisk","Whistle","White","Wig","Will","Windmill","Winter","Wish","Wolf","Wool","World","Worm","Wristwatch","Yardstick","Zamboni","Zen","Zero","Zipper","Zone","Zoo"]
	generated_row = []
	word_grid = []
	for i in range(5):
		for i in range(5):
			while True:
				use = True
				word = random.choice(word_list)
				for _list in word_grid:
					if word in _list:
						use = False
				if word in generated_row:
					use = False
				if use:
					generated_row.append(word)
					break
		word_grid.append(generated_row)
		generated_row = []

	#generate color grid
	color_grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	BLUE = 1
	RED = 2
	DEATH = 3
	for i in range(9):
		while True:
			x = random.randint(0,4)
			y = random.randint(0,4)
			if color_grid[y][x] == 0:
				color_grid[y][x] = RED
				break
	for i in range(8):
		while True:
			x = random.randint(0,4)
			y = random.randint(0,4)
			if color_grid[y][x] == 0:
				color_grid[y][x] = BLUE
				break
	for i in range(1):
		while True:
			x = random.randint(0,4)
			y = random.randint(0,4)
			if color_grid[y][x] == 0:
				color_grid[y][x] = DEATH
				break

	#generate shown grid
	shown_grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

	yellow_left = 7
	red_left = 9
	blue_left = 8

	while True:
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = pygame.mouse.get_pos()
				mouseX /= win_size/5
				mouseX = int(mouseX)
				mouseY /= win_size/5
				mouseY = int(mouseY)
				if mouseX <=4:
					shown_grid[mouseY][mouseX] = 1

		printX = 0
		printY = 0

		yellow_left = 0
		red_left = 0
		blue_left = 0

		for row in color_grid:
			for sq in row:
				if shown_grid[printY][printX] == 0:
					if sq == 0:
						yellow_left += 1
					if sq == 1:
						blue_left += 1
					if sq == 2:
						red_left += 1

				printX += 1
			printY += 1
			printX = 0

		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			break
		draw()
