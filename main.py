# import pygame module in this program  
import pygame 
import pygame_gui
import time
import random

# activate the pygame library.    
pygame.init() 
pygame.font.init()

##### INSTANTIATING OBJECTS #####

screen = pygame.display.set_mode((1280, 720)) #create game window
manager = pygame_gui.UIManager((1280, 720))

#all backgrounds
title = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\title_screen.png").convert(), (1280, 720))
menu = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\plain_menu.png").convert(), (1280, 720))
start_game = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\start_game.png").convert(), (1280, 720))
options = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\options.png").convert(), (1280, 720))
quit_game = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\quit_game.png").convert(), (1280, 720))

safe_mid = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\safe_mid.png").convert_alpha(), (1280, 720))
safe_right = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\safe_right.png").convert_alpha(), (1280, 720))
safe_left = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\safe_left.png").convert_alpha(), (1280, 720))
med_center = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\med_center.png").convert_alpha(), (1280, 720))
med_furniture_only = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\med_furniture_only.PNG").convert_alpha(), (1280, 720))

conflict_right = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\conflict_right.PNG").convert_alpha(), (1280, 720))
conflict_left = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\conflict_left.PNG").convert_alpha(), (1280, 720))
conflict_mid = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\conflict_mid.PNG").convert_alpha(), (1280, 720))
greenhouse = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\MAP\\greenhouse.JPEG").convert_alpha(), (1280, 720))

angry_room = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\angry_room.JPEG").convert_alpha(), (1280, 720))
computer_login = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\computer_login.JPEG").convert_alpha(), (1280, 720))
computer_screen = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\computer_screen.JPEG").convert_alpha(), (1280, 720))
farm_valley_loading = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\farm_valley_loading.JPEG").convert_alpha(), (1280, 720))
farm_valley_virus_detected = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\farm_valley_virus_detected.JPEG").convert_alpha(), (1280, 720))
happy_room = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\happy_room.JPEG").convert_alpha(), (1280, 720))

#all sprite graphics
MC_down = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\MC\\MC_down.PNG").convert_alpha(), (75, 150))
MC_up = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\MC\\MC_up.PNG").convert_alpha(), (75, 150))
MC_left = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\MC\\MC_left.PNG").convert_alpha(), (75, 150))
MC_right = pygame.transform.flip(pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\MC\\MC_left.PNG").convert_alpha(), (75, 150)), True, False)

MC_down_walk = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\MC\\MC_down_walk.PNG").convert_alpha(), (75, 150))
MC_up_walk = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\MC\\MC_up_walk.PNG").convert_alpha(), (75, 150))
MC_left_walk = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\MC\\MC_left_walk.PNG").convert_alpha(), (75, 150))
MC_right_walk = pygame.transform.flip(pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\MC\\MC_left_walk.PNG").convert_alpha(), (75, 150)), True, False)

dantes_sitting = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\NPC\\dantes_sitting.PNG").convert_alpha(), (742//7, 1039//7))
dantes_standing = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\NPC\\dantes_standing.PNG").convert_alpha(), (749//7, 1048//7))
edmund_normal = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\NPC\\edmund_normal.PNG").convert_alpha(), (670//7, 1074//7))
edmund_talking = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\NPC\\edmund_talking.PNG").convert_alpha(), (679//7, 1048//7))

victoria_blacksmith = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\NPC\\victoria_the_blacksmith.PNG").convert_alpha(), (644, 895))

evil_rock = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\ENEMIES\\evil_rock.PNG").convert_alpha(), (545, 623))
evil_venus_flytrap = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\ENEMIES\\evil_venus_flytrap.PNG").convert_alpha(), (1331//7, 1431//7))
infected_shepherd = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\ENEMIES\\infected_shepherd.PNG").convert_alpha(), (1285//7, 1158//7))

#all items and other graphics
respawn_anchor = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\respawn_anchor.PNG").convert_alpha(), (1035, 933))
arrow_right = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\arrow.PNG").convert_alpha(), (1069, 835))
arrow_left = pygame.transform.flip(pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\arrow.PNG").convert_alpha(), (1069, 835)), True, False)
arrow_down = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\arrow.PNG").convert_alpha(), (835, 1069)), 270)
arrow_up = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\arrow.PNG").convert_alpha(), (835, 1069)), 90)
sparkle = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\sparkle.PNG").convert_alpha(), (1357, 1559))

a_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\_a_.PNG").convert_alpha(), (100, 100))
d_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\_d_.PNG").convert_alpha(), (100, 100))
e_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\_e_.PNG").convert_alpha(), (100, 100))
i_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\_i_.PNG").convert_alpha(), (100, 100))
s_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\_s_.PNG").convert_alpha(), (100, 100))
w_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\_w_.PNG").convert_alpha(), (100, 100))

close_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\close_x.PNG").convert_alpha(), (207, 112))
quests_tab = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\quests_tab.PNG").convert_alpha(), (162, 76))
guide_book = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\book_pages.PNG").convert_alpha(), (2234, 1298))

recipes_tab = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\recipes_tab.PNG").convert_alpha(), (160, 77))
continue_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\continue_button.PNG").convert_alpha(), (2082, 158))
open_guide_book_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\open_guide_book_button.PNG").convert_alpha(), (2083, 179))
quit_game_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\quit_game_button.PNG").convert_alpha(), (2079, 181))
pause_button = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\pause_button.PNG").convert_alpha(), (2060, 177))
system_message = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\system_message.PNG").convert_alpha(), (2284, 1248))
dialogue = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\dialogue.PNG").convert_alpha(), (1280, 720))

bow = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\ITEMS\\bow.PNG").convert_alpha(), (871, 1129))
staff = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\ITEMS\\staff.PNG").convert_alpha(), (395, 1086))
sword = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\SPRITES\\ITEMS\\sword.PNG").convert_alpha(), (344, 758)) 

attack_down = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\attack_down.PNG").convert_alpha(), (2076, 180))
attack_up = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\attack_up.PNG").convert_alpha(), (2072, 278))
defend_down = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\defend_down.PNG").convert_alpha(), (2082, 179))
defend_up = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\defend_up.PNG").convert_alpha(), (2082, 179))
pause_game = pygame.transform.scale(pygame.image.load("C:\\Users\\weide\\Downloads\\WELCHIA\\images\\UI\\pause_symbol.png").convert_alpha(), (256, 256))

donnie = pygame.image.load("C:\\Users\\weide\\apcsa\\pixLab\\images\\smallDonnie.jpg").convert()

pygame.display.set_caption("WELCHIA") # set the pygame window name  

class Element(pygame.sprite.Sprite): #defining the element class
    def __init__(self, x, y, width, height, surface, image):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def set_opacity(self, alpha_value):
        self.image.set_alpha(alpha_value)
    
class Item(Element): #defining the item class
    def __init__(self, x, y, width, height, surface, image, name, cost, desc):
        super().__init__(x, y, width, height, surface, image)
        self.name = name
        self.cost = cost
        self.desc = desc

class Player(Element): #defining the player class as a subclass of element
    def __init__(self, x, y, width, height, surface, image, name, inv: list, direction, is_moving):
        super().__init__(x, y, width, height, surface, image)
        self.name = name 
        self.lvl = 0
        self.MAX_HP = 10
        self.hp = 10
        self.MAX_EXP = 10
        self.exp = 0
        self.BASE_ATK = 5
        self.BASE_DEF = 5
        self.DEF = 5
        self.ATK = 5
        self.atk_bonus = 0
        self.def_bonus = 0
        self.SPD = 7
        self.inv = inv
        self.direction = direction
        self.is_moving = is_moving
    def lvl_up(self): #level up function
            if(self.lvl == 0):
                self.lvl = 1
                self.MAX_HP = 15
                self.hp = 15
                self.MAX_EXP = 20
                self.exp = 0
                self.BASE_DEF = 7
                self.BASE_ATK = 7
                self.ATK = self.BASE_ATK + self.atk_bonus
                self.DEF = self.BASE_DEF + self.def_bonus
                self.SPD = 6
            if(self.lvl == 1):
                self.lvl = 2
                self.MAX_HP = 20
                self.hp = 20
                self.MAX_EXP = 35
                self.exp = 0
                self.BASE_DEF = 10
                self.BASE_ATK = 10
                self.ATK = self.BASE_ATK + self.atk_bonus
                self.DEF = self.BASE_DEF + self.def_bonus
                self.SPD = 5
            if(self.lvl == 2):
                self.lvl = 3
                self.MAX_HP = 25
                self.hp = 25
                self.MAX_EXP = 45
                self.exp = 0
                self.BASE_DEF = 15
                self.BASE_ATK = 15
                self.ATK = self.BASE_ATK + self.atk_bonus
                self.DEF = self.BASE_DEF + self.def_bonus
                self.SPD = 4
            if(self.lvl == 3):
                self.lvl = 4
                self.MAX_HP = 30
                self.hp = 30
                self.MAX_EXP = 60
                self.exp = 0
                self.BASE_DEF = 20
                self.BASE_ATK = 20
                self.ATK = self.BASE_ATK + self.atk_bonus
                self.DEF = self.BASE_DEF + self.def_bonus
                self.SPD = 3
            if(self.lvl == 4):
                self.lvl = 5
                self.MAX_HP = 40
                self.hp = 40
                self.MAX_EXP = 75
                self.exp = 0
                self.BASE_DEF = 25
                self.BASE_ATK = 25
                self.ATK = self.BASE_ATK + self.atk_bonus
                self.DEF = self.BASE_DEF + self.def_bonus
                self.SPD = 2
    def check_exp(self): #checking if the player is ready to level up
        if self.exp == self.MAX_EXP:
            self.lvl_up()
        elif self.exp > self.MAX_EXP:
            x = self.MAX_EXP - self.exp
            self.lvl_up()
            self.exp += x
    def main_hand_attack(self, opp):
        opp.hp -= self.ATK + self.atk_bonus
        ##add visual, text rect for dmg number
    def special_attack(self, opp):
        pass ##dictionary for special attacks? name + multiplier?
    def use_item(self, item: Item):
        self.inv.remove(item)

    def gain_xp(self, exp):
        self.exp += exp
        self.check_exp()
    def reposition(self):
        if self.is_moving:
            if self.direction == "down":
                self.image = MC_down_walk
            elif self.direction == "up":
                self.image = MC_up_walk
            elif self.direction == "left":
                self.image = MC_left_walk
            elif self.direction == "right":
                self.image = MC_right_walk
        else:
            if self.direction == "down":
                self.image = MC_down
            elif self.direction == "up":
                self.image = MC_up
            elif self.direction == "left":
                self.image = MC_left
            elif self.direction == "right":
                self.image = MC_right

class Gear(Item):
    def __init__(self, x, y, width, height, surface, image, name, icon, cost, desc, ATK, DEF, HP, SPD):
        super().__init__(x, y, width, height, surface, image, name, icon, cost, desc)
        self.ATK = ATK
        self.DEF = DEF
        self.HP = HP
        self.SPD = SPD

class Consumables(Item):
    def __init__(self, x, y, width, height, surface, image, name, icon, cost, desc, ATK, DEF, HP, SPD, duration, count):
        super().__init__(x, y, width, height, surface, image, name, icon, cost, desc)
        self.ATK = ATK
        self.DEF = DEF
        self.HP = HP
        self.SPD = SPD
        self.duration = duration
        self.count = count
    def consume(self, player: Player):
        while self.duration > 0:
            player.atk_bonus = self.ATK
            player.def_bonus = self.DEF
            
            clock.tick(1000)
            self.duration-=1
            

        


class Enemies(Element):
     def __init__(self, x, y, width, height, surface, image, name, hp, MAX_HP, exp, ATK, DEF):
         super().__init__(x, y, width, height, surface, image)
         self.name = name
         self.hp = hp
         self.MAX_HP = MAX_HP
         self.exp = exp
         self. ATK = ATK
         self.DEF = DEF

class NPC(Element):
     def __init__(self, x, y, width, height, surface, image, name):
         super().__init__(x, y, width, height, surface, image)
         self.name = name
         self.image = image

    
## CREATE OBJECTS ##
inventory = []
player = Player(700, 100, 75, 150, screen, MC_down,"", inventory, "down", False)

rock = Enemies(250, 700, 545//5, 623//5, screen, evil_rock, "Evil Rock", 5, 5, 5, 1, 1)
shep = Enemies(725, 200, 1285//7, 1158//7, screen, infected_shepherd, "Infected Shepherd", 10, 10, 10, 5, 5)


safe_respawn = Element(600, 200, 1035//8, 933//8, screen, respawn_anchor)
safe_mid_arrow1 = Element(10, 600, 1069//8, 835//8, screen, arrow_left)
safe_mid_arrow1.set_opacity(200)
safe_mid_arrow2 = Element(1100, 600, 1069//8, 835//8, screen, arrow_right)
safe_mid_arrow2.set_opacity(200)
safe_left_arrow = Element(1100, 600, 1069//8, 835//8, screen, arrow_right)
safe_left_arrow.set_opacity(200)
safe_right_arrow = Element(10, 600, 1069//8, 835//8, screen, arrow_left)
safe_right_arrow.set_opacity(200)
safe_exit_arrow = Element(600, 600, 1069//8, 835//10, screen, arrow_down)
safe_exit_arrow.set_opacity(200)

conflict_respawn = Element(600, 200, 1035//8, 933//8, screen, respawn_anchor)
conflict_mid_arrow1 = Element(10, 600, 1069//8, 835//8, screen, arrow_left)
conflict_mid_arrow1.set_opacity(200)
conflict_mid_arrow2 = Element(1100, 600, 1069//8, 835//8, screen, arrow_right)
conflict_mid_arrow2.set_opacity(200)
conflict_left_arrow = Element(1100, 600, 1069//8, 835//8, screen, arrow_right)
conflict_left_arrow.set_opacity(200)
conflict_right_arrow = Element(10, 600, 1069//8, 835//8, screen, arrow_left)
conflict_right_arrow.set_opacity(200)
conflict_up_arrow = Element(500, 15, 835//8, 1069//8, screen, arrow_up)
conflict_exit_arrow = Element(600, 600, 1069//8, 835//10, screen, arrow_down)
conflict_exit_arrow.set_opacity(200)

a = Element(150, 150, 50, 50, screen, a_button)
dantes_fr = NPC(1050, 350, 742//7, 1039//7, screen, dantes_sitting, "Old Man Dantes")
dantes_dlg = Element(25, 350, 749, 1048, screen, dantes_standing)
edmund_fr = NPC(200, 350, 670//7, 1074//7, screen, edmund_normal, "Edmund the Medic")
edmund_dlg = Element(25, 300, 679, 1048, screen, edmund_talking)
victoria = NPC(900, 50, 644, 895, screen, victoria_blacksmith, "Victoria the Blacksmith")

atk_down = Element(20, 400, attack_up.width//7, attack_up.height//7, screen, attack_down)
atk_up = Element(20, 400, attack_up.width//7, attack_up.height//7, screen, attack_up)

spark = Element(500, 600, 50, 50, screen, sparkle)

visible_sprites = pygame.sprite.Group()

## TEXT OBJECTS ##
copperplate = pygame.font.Font("C:\\Users\\weide\\Downloads\\WELCHIA\\texts_and_fonts\\Copperplate.ttf", 50)
test_text = copperplate.render("What's your name?", True, (255,255,255))
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((110, 310), (1060, 50)), manager=manager, object_id='#main_text_entry')
win_text = copperplate.render("YOU WIN!", True, (0,0,0))
over = copperplate.render("You have completed the demo! \nFull version will be released when \njesus returns in the form of a shark", True, (255, 255, 255))
opt = copperplate.render("nothing here yet", True, (255, 255, 255))

##### FUNCTIONS ######

def battle(opp: Enemies, click, keys):
    battle = True
    screen.fill((150,200,150))
    player.rect.x = 200
    player.rect.y = 250
    opp.rect.x = 1000
    opp.rect.y = 640-(opp.height//2)
    damage_done = 0
    dmg_txt = copperplate.render(f"-{damage_done} hp", True, (0,0,0))
    
    while battle:
        screen.fill((150,200,150))  
        for event in events: 
            # if event object type is QUIT then quit the program   
            if event.type == pygame.QUIT: 
                pygame.quit()
        
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        if click == pygame.MOUSEBUTTONDOWN:
            damage_done = player.ATK - opp.DEF
            opp.hp -= damage_done
            screen.blit(dmg_txt, (450, 15))

        if player.hp <= 0:
            battle = False
            return "LOSE"
        
        if opp.hp <= 0:
            battle = False
            return "WIN"
    pygame.display.update()
    visible_sprites.draw(screen)

        
  
def check_key(key_pressed): # check user input function
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_s] or key_pressed[pygame.K_a] or key_pressed[pygame.K_d]:
        player.is_moving = True
        if key_pressed[pygame.K_w] and player.rect.y >= 0:
                player.direction = "up"
                player.rect.y -= 10
        if key_pressed[pygame.K_s] and player.rect.y <= 720-player.height:
                player.direction = "down"
                player.rect.y += 10
        if key_pressed[pygame.K_a] and player.rect.x >= 0:
                player.direction = "left"
                player.rect.x -= 10
        if key_pressed[pygame.K_d] and player.rect.x <= 1280-player.width:
                player.direction = "right"
                player.rect.x += 10
    else: 
        player.is_moving = False

def get_user_name():
    screen.blit(test_text, (250, 200))
    got_name = False
    while not got_name:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                got_name = True
                return event.text
            
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        manager.draw_ui(screen)

        pygame.display.update()

def inbounds(x_upper, x_lower, y_upper, y_lower):
    #pygame.draw.rect(screen, (255,255,255),(x_lower, y_upper, x_upper-x_lower, y_lower-y_upper))
    if pygame.mouse.get_pos()[0] <= x_upper:
        if pygame.mouse.get_pos()[0] >= x_lower:
            if pygame.mouse.get_pos()[1] <= y_lower:
                if pygame.mouse.get_pos()[1] >= y_upper:
                    return True
    else:
        return False
    
def obstacle(p, o):
    # Calculate the overlap on each side
    overlap_x = min(p.rect.right - o.rect.left, o.rect.right - p.rect.left)
    overlap_y = min(p.rect.bottom - o.rect.top, o.rect.bottom - p.rect.top)
    if p.rect.colliderect(o):
        if overlap_x < overlap_y:  
            if p.rect.x < o.rect.x:
                p.rect.x -= overlap_x
            else:
                p.rect.x += overlap_x
        else: 
            if p.rect.y < o.rect.y:
                p.rect.y -= overlap_y
            else:
                p.rect.y += overlap_y

run = True # Indicates pygame is running 
current_scene = "START"

screen.blit(title, (0, 0))

yes_name = False

battle = True

##### GAME LOOP #####
while run: 
    clock = pygame.time.Clock()
    clock.tick(60) #max fps is 60
    events = pygame.event.get()
    
    for event in events: 
            
            # if event object type is QUIT then quit the program   
            if event.type == pygame.QUIT: 
                run = False
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_ESCAPE]:
        run = False 
      
    if current_scene == "START": # iterate over the list of Event objects that was returned by pygame.event.get() method.   
        for event in events: 
            if event.type == pygame.MOUSEBUTTONDOWN and inbounds(1040,240,320,400):
                screen.blit(menu, (0,0))
                current_scene = "MENU"

    if current_scene == "MENU": #using the same type of iteration but specifc to the "MENU" scene
        if inbounds(400,52,152,192):
            screen.blit(start_game, (0,0))
        elif inbounds(300,52,256,296):
            screen.blit(options, (0,0))
        elif inbounds(360,52,360,400):
            screen.blit(quit_game, (0,0))
        else:
            screen.blit(menu, (0,0))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and inbounds(400,52,152,192):
                current_scene = "BEDROOM"
            if event.type == pygame.MOUSEBUTTONDOWN and inbounds(300,52,256,296):
                current_scene = "OPTIONS"
            if event.type == pygame.MOUSEBUTTONDOWN and inbounds(360,52,360,400):
                run = False
    
    if current_scene == "BEDROOM":
        if not yes_name:
            screen.fill((193, 73, 1))
            player.name = get_user_name()
            yes_name = True

        name = copperplate.render(f"Hello {player.name}, \npress SPACE to run through dialogue", True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(name, (10,400))
        if keys[pygame.K_SPACE]:
            current_scene = "CUT1"
    
    if current_scene == "OPTIONS":
        screen.fill ((0,0,0))
        screen.blit(opt, (350, 50))
        screen.blit(donnie, (200, 150))
        if keys[pygame.K_SPACE]:
            current_scene = "MENU"
    
    if current_scene == "CUT1":
        screen.blit(happy_room, (0,0))
        if keys[pygame.K_LEFT]:
            current_scene = "CUT2"

    if current_scene == "CUT2":
        screen.blit(computer_login, (0,0))
        if keys[pygame.K_SPACE]:
            current_scene = "CUT3"

    if current_scene == "CUT3":
        screen.blit(computer_screen, (0,0))
        if keys[pygame.K_LEFT]:
            current_scene = "CUT4"

    if current_scene == "CUT4":
        screen.blit(farm_valley_loading, (0,0))
        if keys[pygame.K_SPACE]:
            current_scene = "CUT5"
    
    if current_scene == "CUT5":
        screen.blit(angry_room, (0,0))
        if keys[pygame.K_LEFT]:
            current_scene = "CUT6"
    
    if current_scene == "CUT6":
        screen.blit(farm_valley_virus_detected, (0,0))
        if keys[pygame.K_SPACE]:
            current_scene = "SAFE MID"

    if current_scene == "SAFE MID":
        visible_sprites.add(safe_mid_arrow1)
        visible_sprites.add(safe_exit_arrow)
        visible_sprites.add(safe_mid_arrow2)
        visible_sprites.add(spark)
        spark.rect.x = 300
        spark.rect.y = 600
        if not visible_sprites.has(player):
            visible_sprites.add(player)
        screen.blit(safe_mid, (0,0))
        player.reposition()
        check_key(keys)
        if keys[pygame.K_e] and player.rect.colliderect(spark.rect):  
            battle = True
            screen.fill((150,200,150))
            title = copperplate.render(f"{player.name} vs. {rock.name}", True, (0,0,0))
            visible_sprites.remove(spark)
            visible_sprites.add(rock)
            visible_sprites.add(atk_up)
            visible_sprites.remove(safe_mid_arrow1)
            visible_sprites.remove(safe_exit_arrow)
            visible_sprites.remove(safe_mid_arrow2)
            player.rect.x = 200
            player.rect.y = 250
            rock.rect.x = 1000
            rock.rect.y = 640-(rock.height)
            damage_done = 0
            
            while battle:
                screen.fill((150,200,150))
                screen.blit(title, (200, 30))
                morekeys = pygame.key.get_pressed()
                clock.tick(30)  
                bigevent = pygame.event.get()
                red = random.randint(1,255)
                green = random.randint(1,255)
                blue = random.randint(1,255)

                dmg_txt = copperplate.render(f"-{damage_done} hp", True, (red,green,blue))
                rock_hp = copperplate.render(f"Rock health: {rock.hp}/{rock.MAX_HP}", True, (0,0,0))
                screen.blit(rock_hp, (850, 150))  

                if damage_done > 0:
                    screen.blit(dmg_txt, (750, 550))

                if player.hp <= 0:
                    battle = False
                
                if rock.hp <= 0:
                    visible_sprites.remove(rock)
                    visible_sprites.remove(atk_up)
                    visible_sprites.remove(atk_down)
                    visible_sprites.remove(spark)
                    battle = False

                if morekeys[pygame.K_n]:
                    visible_sprites.remove(atk_up)
                    visible_sprites.remove(atk_down)
                    battle = False
                
                if player.rect.colliderect(atk_up.rect):
                    visible_sprites.remove(player)
                    visible_sprites.add(atk_down)
                    visible_sprites.add(player)
                    if player.rect.colliderect(atk_down.rect) and morekeys[pygame.K_e]:
                        damage_done = 1 #player.ATK - rock.DEF
                        rock.hp -= damage_done
                        player.rect.y = 200
                else:
                    visible_sprites.remove(atk_down)

                player.reposition()
                check_key(morekeys)
                visible_sprites.draw(screen)
                pygame.display.update()

        if keys[pygame.K_e]:
            if player.rect.colliderect(safe_mid_arrow1.rect):
                current_scene = "SAFE LEFT"
                visible_sprites.remove(safe_mid_arrow1)
                visible_sprites.remove(safe_exit_arrow)
                visible_sprites.remove(safe_mid_arrow2)
                visible_sprites.remove(spark)
                player.rect.x = 1000
            elif player.rect.colliderect(safe_exit_arrow.rect):
                current_scene = "CONFLICT MID"
                visible_sprites.remove(safe_mid_arrow1)
                visible_sprites.remove(safe_exit_arrow)
                visible_sprites.remove(safe_mid_arrow2)
                player.rect.x = 600
                player.rect.y = player.height + 15
                visible_sprites.remove(spark)
            elif player.rect.colliderect(safe_mid_arrow2.rect):
                current_scene = "SAFE RIGHT"
                visible_sprites.remove(safe_mid_arrow1)
                visible_sprites.remove(safe_exit_arrow)
                visible_sprites.remove(safe_mid_arrow2)
                visible_sprites.remove(spark)
                player.rect.x = 200

    if current_scene == "SAFE LEFT":
        visible_sprites.add(safe_left_arrow)
        screen.blit(safe_left, (0,0))   
        player.reposition()
        check_key(keys) 
        if keys[pygame.K_e]:
            if player.rect.colliderect(safe_left_arrow.rect):
                current_scene = "SAFE MID"
                visible_sprites.remove(safe_left_arrow)
                player.rect.x = 200
                

    if current_scene == "SAFE RIGHT":
        visible_sprites.add(safe_right_arrow)
        visible_sprites.add(spark)
        spark.rect.x = 310
        spark.rect.y = 350
        screen.blit(safe_right, (0,0))
        player.reposition()
        check_key(keys)
        if keys[pygame.K_e]:
            if player.rect.colliderect(safe_right_arrow.rect):
                current_scene = "SAFE MID"
                visible_sprites.remove(safe_right_arrow)
                visible_sprites.remove(spark)
                player.rect.x = 1000
            if player.rect.colliderect(spark):
                current_scene = "MED CENTER"
                visible_sprites.remove(safe_right_arrow)
                visible_sprites.remove(spark)
                player.rect.x = 850
                player.rect.y = 700 - player.height

    if current_scene == "MED CENTER":
        visible_sprites.add(spark)
        visible_sprites.add(dantes_fr)
        visible_sprites.add(edmund_fr)
        spark.rect.x = 1000
        spark.rect.y = 650
        screen.blit(med_center, (0,0))
        player.reposition()
        check_key(keys)  
        if keys[pygame.K_e]:   
            if player.rect.colliderect(spark):
                current_scene = "SAFE RIGHT"
                visible_sprites.remove(spark)
                visible_sprites.remove(dantes_fr)
                visible_sprites.remove(edmund_fr)
                visible_sprites
                player.rect.x = 900
                player.rect.y = 400

    if current_scene == "CONFLICT MID":
        visible_sprites.add(conflict_mid_arrow1)
        visible_sprites.add(conflict_exit_arrow)
        visible_sprites.add(conflict_mid_arrow2)
        visible_sprites.add(conflict_up_arrow)
        screen.blit(conflict_mid, (0,0))
        player.reposition()
        check_key(keys)
        if keys[pygame.K_e]:
            if player.rect.colliderect(conflict_mid_arrow1.rect):
                current_scene = "CONFLICT LEFT"
                visible_sprites.remove(conflict_mid_arrow1)
                visible_sprites.remove(conflict_exit_arrow)
                visible_sprites.remove(conflict_mid_arrow2)
                visible_sprites.remove(conflict_up_arrow)
                player.rect.x = 1000
                
            if player.rect.colliderect(conflict_exit_arrow.rect):
                current_scene = "END OF DEMO"
                visible_sprites.remove(conflict_mid_arrow1)
                visible_sprites.remove(conflict_exit_arrow)
                visible_sprites.remove(conflict_mid_arrow2)
                visible_sprites.remove(conflict_up_arrow)
                player.rect.x = 600
                player.rect.y = player.height + 15
                
            if player.rect.colliderect(conflict_mid_arrow2.rect):
                current_scene = "CONFLICT RIGHT"
                visible_sprites.remove(conflict_mid_arrow1)
                visible_sprites.remove(conflict_exit_arrow)
                visible_sprites.remove(conflict_mid_arrow2)
                visible_sprites.remove(conflict_up_arrow)
                player.rect.x = 200
            
            if player.rect.colliderect(conflict_up_arrow):
                current_scene = "SAFE MID"
                visible_sprites.remove(conflict_mid_arrow1)
                visible_sprites.remove(conflict_exit_arrow)
                visible_sprites.remove(conflict_mid_arrow2)
                visible_sprites.remove(conflict_up_arrow)
                player.rect.x = 600
                player.rect.y = player.height + 20
                    

    if current_scene == "CONFLICT LEFT":
        win = False
        visible_sprites.add(conflict_left_arrow)
        screen.blit(conflict_left, (0,0))   
        if not win:
            visible_sprites.add(shep)
        else:
            visible_sprites.remove(shep)
        player.reposition()
        check_key(keys) 
        if keys[pygame.K_e] and player.rect.colliderect(shep.rect):  
            battle = True
            screen.fill((150,200,150))
            title = copperplate.render(f"{player.name} vs. {shep.name}", True, (0,0,0))
            visible_sprites.remove(spark)
            visible_sprites.add(shep)
            visible_sprites.add(atk_up)
            visible_sprites.remove(safe_mid_arrow1)
            visible_sprites.remove(safe_exit_arrow)
            visible_sprites.remove(safe_mid_arrow2)
            player.rect.x = 200
            player.rect.y = 250
            shep.rect.x = 1000
            shep.rect.y = 640-(shep.height)
            damage_done = 0
            
            while battle:
                screen.fill((150,200,150))
                screen.blit(title, (200, 30))
                morekeys = pygame.key.get_pressed()
                clock.tick(30)  
                bigevent = pygame.event.get()
                red = random.randint(1,255)
                green = random.randint(1,255)
                blue = random.randint(1,255)
                shep.rect.x = 850
                shep.rect.y = 400

                dmg_txt = copperplate.render(f"-{damage_done} hp", True, (red,green,blue))
                shep_hp = copperplate.render(f"Shepherd health: {shep.hp}/{shep.MAX_HP}", True, (0,0,0))
                screen.blit(shep_hp, (400, 150))  

                if damage_done > 0:
                    screen.blit(dmg_txt, (750, 550))

                if player.hp <= 0:
                    battle = False
                
                if shep.hp <= 0:
                    screen.blit(win_text, (600, 25))
                    visible_sprites.remove(shep)
                    visible_sprites.remove(atk_up)
                    visible_sprites.remove(atk_down)
                    visible_sprites.remove(spark)
                    win = True
                    battle = False

                if morekeys[pygame.K_n]:
                    visible_sprites.remove(atk_up)
                    visible_sprites.remove(atk_down)
                    battle = False
                
                if player.rect.colliderect(atk_up.rect):
                    visible_sprites.remove(player)
                    visible_sprites.add(atk_down)
                    visible_sprites.add(player)
                    if player.rect.colliderect(atk_down.rect) and morekeys[pygame.K_e]:
                        damage_done = 1 #player.ATK - rock.DEF
                        shep.hp -= damage_done
                        player.rect.y = 200
                else:
                    visible_sprites.remove(atk_down)

                player.reposition()
                check_key(morekeys)
                visible_sprites.draw(screen)
                pygame.display.update()
        if keys[pygame.K_e]:
            if player.rect.colliderect(conflict_left_arrow.rect):
                current_scene = "CONFLICT MID"
                visible_sprites.remove(conflict_left_arrow)
                player.rect.x = 200

    if current_scene == "CONFLICT RIGHT":
        visible_sprites.add(conflict_right_arrow)
        visible_sprites.add(spark)
        spark.rect.x = 740
        spark.rect.y = 400
        screen.blit(conflict_right, (0,0))
        player.reposition()
        check_key(keys)
        if keys[pygame.K_e]:
            if player.rect.colliderect(conflict_right_arrow.rect):
                current_scene = "CONFLICT MID"
                visible_sprites.remove(spark)
                visible_sprites.remove(conflict_right_arrow)
                visible_sprites.remove(shep)
                player.rect.x = 800
            if player.rect.colliderect(spark.rect):
                current_scene = "GREENHOUSE"
                visible_sprites.remove(spark)
                visible_sprites.remove(conflict_right_arrow)
                visible_sprites.remove(shep)

    if current_scene == "GREENHOUSE":
        visible_sprites.add(spark)
        spark.rect.x = 40
        spark.rect.y = 300
        screen.blit(greenhouse, (0,0))
        player.reposition()
        check_key(keys)
        if keys[pygame.K_e]:
            if player.rect.colliderect(spark.rect):
                current_scene = "CONFLICT RIGHT"
                visible_sprites.remove(spark)


    if current_scene == "END OF DEMO":
        screen.fill((0,0,0))
        screen.blit(over, (10, 500))

      
    # refreshes the window 
    visible_sprites.draw(screen)
    pygame.display.update()  
  
# closes the pygame window  
pygame.quit() 

