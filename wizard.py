import random
from fpdf import FPDF
import math
import tkinter as tk
import webbrowser
pdf = FPDF()


#window = tk.Tk("400x400")
#window.geometry("500x500")
#label =tk.Label(window, text = "Welcome to the character generator", font = "Garamond",)
#label.pack()
#input = tk.Entry(window, width = 50,)
#input.get()
#input.pack()
#def click():
#    global level
#    level = int(input.get())
#    window.destroy()
#button =tk.Button(window, text="What level is your character?", command = click,)
#button.pack()



window = tk.Tk("400x400")
window.title("Choose the character level")



def button_add(number):
    global level
    level = int(number)
    window.destroy()



#define buttons and add to screen
for x in range(1, 21):
    button = tk.Button(window, text = str(x), padx=40, pady=20, command = lambda:button_add(x))
    row = math.floor(x / 4.1)
    column = (x - 1) % 4

    button.grid(row=row, column=column)

#adds a blank page
pdf.add_page()
pdf.set_font("Arial",size =18)
pdf.image("5ep.png", x=0,y=0,w=210)
window.mainloop()

#page for spells
var = 14
var2 = 58.5

##CLass features
pdf.set_xy(143,134)
pdf.set_font("Arial",size =12)
pdf.multi_cell(w=55, h =5,
txt ='Arcane Recovery- see handbook.  At second level choose a school of magic.  See handbook for details',
border = 1)

# rests size of set_font
pdf.set_font("Arial",size =18)



####Spot to add loot drops in gold, and items
def loot():
    if level in range(0,3):
        gold = random.randint(0,15)
        print(f"Gold dropped: {gold} Gold")
        pdf.text(94,210, txt = (f"{gold} Gold"))
    if level in range(4,6):
        gold = random.randint(20,50)
        item_num = random.randint(1,5)
        if item_num == 1:
            print("Dropped a scroll")
            pdf.text(94,220, txt = "Scroll")
        if item_num == 2:
            print("Dropped a clothing item")
            pdf.text(94,220, txt = "Clothes")
        print(f"Gold dropped: {gold} Gold")
        pdf.text(94,210, txt = (f"{gold} Gold"))
    if level in range(7,12):
        gold = random.randint(60,100)
        item_num = random.randint(1,5)
        if item_num == 1:
            print("Dropped a scroll")
            pdf.text(94,220, txt = "Scroll")
        if item_num == 2:
            print("Dropped a clothing item")
            pdf.text(94,220, txt = "Clothes")
        if item_num ==3:
            print("dropped a magical item")
            pdf.text(94,220, txt = "Magical Item")
        print(f"Gold dropped: {gold} Gold")
        pdf.text(94,210, txt = (f"{gold} Gold"))
    if level in range(13,21):
        gold = random.randint(100,200)
        item_num = random.randint(1,5)
        if item_num == 1:
            print("Dropped a scroll")
            pdf.text(94,220, txt = "Scroll")
        if item_num == 2:
            print("Dropped a clothing item")
            pdf.text(94,220, txt = "Clothes")
        if item_num ==3:
            print("dropped a wondrous item")
            pdf.text(94,220, txt = "Wondrous Item")
        print(f"Gold dropped: {gold} Gold")
        pdf.text(94,210, txt = (f"{gold} Gold"))


##initiative and proficiency******************************************
## check upper bound on all Ranges *************
def stats():

    global spell_bonus

    if level in range(1,6):
        Strength = 8
        Dexterity = 14
        Constitution =13
        Intelligence = 15
        Wisdom = 12
        Charisma = 10
        SavingThrow = Intelligence
        Proficiency = 2


    if level in range(6,11):
        Strength = 9 + (random.randint(-1,1))
        Dexterity = 15 + (random.randint(-1,1))
        Constitution = 14 + (random.randint(-1,1))
        Intelligence = 16 + (random.randint(-1,1))
        Wisdom = 11 + (random.randint(-1,1))
        Charisma = 11 + (random.randint(-1,1))
        SavingThrow = Intelligence
        Proficiency = 3

    if level in range(11,21):
        Strength = 10 + (random.randint(-2,2))
        Dexterity = 16 + (random.randint(-2,2))
        Constitution = 15 + (random.randint(-2,2))
        Intelligence = 17 + (random.randint(-2,2))
        Wisdom = 12 + (random.randint(-2,2))
        Charisma = 12 + (random.randint(-2,2))
        SavingThrow = Intelligence
        Proficiency = 4
    global Imod
    global Dmod
    global Cmod
    global Chmod
    global Wmod
    global Smod
    global spell_save
    Smod = math.trunc((Strength - 10)/2)
    Dmod =  math.trunc((Dexterity - 10)/2)
    Cmod =  math.trunc((Constitution - 10)/2)
    Imod =  math.trunc((Intelligence - 10)/2)
    Wmod =  math.trunc((Wisdom - 10)/2)
    Chmod =  math.trunc((Charisma - 10)/2)
    spell_bonus = (Imod + Proficiency)
    spell_save = (8 + Imod + Proficiency)
    prep_spells = (level + Imod)

    print(f"Strength:{Strength}\nDexterity: {Dexterity}\nConstitution: {Constitution}\nIntelligence: {Intelligence}\nWisdom:{Wisdom}\nCharisma: {Charisma}\nSaving Throw: {Intelligence}")
    pdf.text(16,60, txt=(f"{Strength}"))
    pdf.text(16,84, txt=(f"{Dexterity}"))
    pdf.text(16,108, txt=(f"{Constitution}"))
    pdf.text(16,133, txt=(f"{Intelligence}"))
    pdf.text(16,157, txt=(f"{Wisdom}"))
    pdf.text(16,182, txt=(f"{Charisma}"))
    pdf.set_font("Arial", size = 10)
    pdf.text(18,67.5, txt =(f"{Smod}"))
    pdf.text(18,92, txt =(f"{Dmod}"))
    pdf.text(18,116.75, txt =(f"{Cmod}"))
    pdf.text(18,141.25, txt =(f"{Imod}"))
    pdf.text(18,166.25, txt =(f"{Wmod}"))
    pdf.text(18,191, txt =(f"{Chmod}"))
    pdf.text(36,62, txt =(f"{Proficiency}"))
    ## spot for the prepared spells:
    pdf.text(81,144, txt =(f"Prepares spells:{prep_spells}"))

    #spot for class and Level
    pdf.set_font("Arial", size = 14)
    pdf.text(93, 20, txt =(f"Wizard     {level}"))

#creates an armor class depending on the class, and level split into two groups
def ac():
    pdf.set_font("Arial", size = 18)
    if level in range (0,5):
        int = random.randint(10,12)
        print(f"AC: {int}")
        pdf.text(81, 55, txt = (f"{int}"))
    if level in range (5,11):
        int = random.randint(11,13)
        print(f"AC: {int}")
        pdf.text(81, 55, txt = (f"{int}"))
    if level in range (11,21):
        int = random.randint(13,16)
        print(f"AC: {int}")
        pdf.text(81, 55, txt = (f"{int}"))

#manages hitpoints per level
def hitpoints():
    pdf.set_font("Arial", size = 18)
    int = random.randint(-5, 5)
    hitpoints = level * 6 + int
    print(f"HP:{hitpoints}")
    pdf.text(95,80, txt = f"{hitpoints}")

#prints cantrips per level

#creates a random race
def random_race():
    races = ['Human', 'orc', 'half orc', 'gnome', 'elf', 'half elf', 'tiefling', 'halfling']
    color = ['light red', 'scarlet red', 'dark red', 'burnt dark red']
    race_length = len(races)
    race_color = len(color)
    random_race_num = random.randint(0,race_length-1)
    random_race = races[random_race_num]
    print(f"Race:{random_race}")
    if "tiefling" in random_race:
        random_color_num = random.randint(0,race_color-1)
        random_color = color[random_color_num]
        print(f"Skin tone: {random_color}")
        pdf.text(110, 30,(f"{random_color}"))
    pdf.text(93, 30, (f"{random_race}"))

#gives a random height descriptor
def random_height():
    height = ['average', 'tall', 'short']
    height_length = len(height)
    random_height_num = random.randint(0,height_length-1)
    random_height = height[random_height_num]
    print("Height:{}".format(random_height))
    pdf.text(143, 170, txt = (f"{random_height}"))

#gives a random weight descriptor
def random_weight():
    weight = ['heavy', 'very heavy', 'skinny','underweight', 'average', 'chubby']
    weight_length = len(weight)
    random_weight_num = random.randint(0,weight_length-1)
    random_weight = weight[random_weight_num]
    print(f"Weight:{random_weight}")
    pdf.text(143, 180, txt = (f"{random_weight}"))

def weapons():
    low = {'Dagger':'1d4 Finesse',}
    mid ={'Dagger':'1d4 Finesse',}
    high ={'Dagger':'1d4 Finesse',}
    if level in range(1,6):
        weapon = key, val = random.choice(list(low.items()))
    if level in range(6,14):
        weapon = key, val = random.choice(list(mid.items()))
    if level in range(14,21):
        weapon = key, val = random.choice(list(high.items()))
    print(f"Weapon: {weapon}")
    pdf.set_font('Arial', size = 10)
    pdf.text(80,154, txt =(f"Weapon: {weapon}"))


#combines all the character elements under one function
def random_char():
    print("Class:Wizard")
    random_race()
    random_height()
    random_weight()
    stats()
    weapons()
    hitpoints()
    ac()
    loot()






random_char()

pdf.add_page()
pdf.image("spells.png", x=0,y=0,w=210)
pdf.set_font("Arial",size =18)




def spells():
    pdf.set_font("Arial", size = 18)
    pdf.text(104,23, txt = f"{Imod}")
    pdf.text(140,23, txt = f"{spell_save}")
    pdf.text(178,23, txt = f"{spell_bonus}")
    #pdf.text(140,23, txt = f"{Save DC}")
    pdf.set_font("Arial",size =18)
    wiz1spells = ['Absorb elements', 'Alarm', 'Burning Hands', 'Catapult', 'Cause Fear', 'Charm person', 'Chromatic Orb',
    'Color Spray', 'Comprehend languages', 'Detect Magic', 'Disguise Self', 'Distort Value', 'Earth Tremor', 'Expeditious Retreat',
    'False Life', 'Feather Fall', 'Find Familiar', 'floating disk','Fog Cloud', 'Frost Fingers', 'Grease', 'Hideous Laughter',
    'Ice Knife', 'Identity', 'Illusory Script', 'Jims Magic Missile', 'Jump', 'Longstrider', 'Mage Armor', 'Magic Missile', 'Protection from evil',
    'Ray of Sickness', 'Shield', 'Silent Image','Silvery Barbs','Sleep','Snare','Tashas Hideous Laugther','Tashas Caustic Brew',
    'Tensers Floating Disk','Thunderwave','Unseen Servant','Witch Bolt']
    wiz2spells = ['Arcane Lock', 'Arcanists magic Aura','blindness/deafness','blur','borrowed Knowledge', 'Cloud of Daggers', 'Continual Flame',
    'Crown of Madness','Darkness','Darkvision','Detect Thoughts','Dragons Breath','Dust Devil', 'Earthbind', 'Enlarge/Reduce', 'Flaming Sphere',
    'Flock of familiars','Gentle Repose','Gift of Gab', 'Gust of Wind', 'Hold Person','Invisibility', 'Jims Glowing Coin', 'Kinetic Jaunt', 'Knock',
    'Levitate', 'Locate Object','Magic Mouth','Magic Weapon','Maximillians Earthen Grasp',' Melfs Acid Arrow','Mind Spike','Mirror Image','Misty Step',
    'Nathairs Mischeif','Nystuls Magic Aura','Phatasmal Force','Pyrotechnics','Ray of Enfeeblement','Rimes Binding Ice','Rope Trick','Scorching Ray',
    'See Invisibility', 'Shadow Blade','Shatter','Skywrite','Snillocs Snowball Swarm','Spider Climb','Suggestion','Tashas Mind Whip','Vortex Warp',
    'Warding Wind','Web','Wither and Bloom']
    wiz3spells = ['Animate Dead', 'Ashardalons Stride','Bestow Curse', 'Blink', 'Catnap','Clairvoyance','Counterspell','Dispel Magic','Enemies Abound',
    'Erupting Earth','Fast Friends','Fear','Feign Death','Fireball','Flame Arrows','Fly','Galders Tower','Gaseous Form','Glyph of Warding','Haste',
    'Hypnotic Pattern','Incite Greed', 'Intellect Fortress','Leomunds Tiny Hut','Life Transference','Lightning Bolt','Magic Circle','Major Image',
    'Melfs Minute Meteros', 'Nondetection','Phantom Steed','Projection from Energy','Remove Curse','Sending','Sleept Storm','Slow','Spirit Shroud',
    'Stinking Cloud','Summon Fey','Summom Lesser Demon','Summon Shadowspear','Summon Undead','Thunder Step','Tidal Wave','Tiny Hut','Tiny Servant',
    'Tongues','Vampiric Touch','Wall of Sand','Wall of Water', 'Water Breathing']
    wiz4spells = ['Arcane Eye','Banishment','Black Tentacles','Blight','Charm Monster','Confusion', 'Conjure Minor Elements', 'Control Water','Dimension Door',
    'Elemental Bane','Evards Black Tentacles','Fabricate','Faithful Hound','Fire Shield','Greater Invisibility','Hallucinatory Terrain','Ice Storm','Lemonunds Secret Chest',
    'Locate Creature','Mordenkaines Faithful','Otilukes Resilient','Phantasmal Killer','Polymorph','Private Sanctum','Ralothims Psychic Lance','Resilient Sphere',
    'Secret Chest','Sickening Radiance','Stone Shape','Stoneskin','Storm Sphere','Summon Abberration','Summon Construct','Summon Elemental','Summon Greater Demon',
    'Vitriolic Sphere','Wall of Fire','Watery Sphere']
    wiz5spells = ['Animate Objects','Transmutation','Arcane Hand','Evocation','Cloudkill','Conjuration','Cone of Cold',	'Evocation','Conjure Elemental','Conjuration','Contact Other Plane','Divination','Creation','Illusion',
    'Dominate Person','Enchantment','Dream','Illusion','Geas','Enchantment','Hold Monster',	'Enchantment',
    'Legend Lore','Divination','Mislead','Illusion','Modify Memory','Enchantment','Passwall','Transmutation',
    'Planar Binding','Abjuration','Scrying','Divination','Seeming','Illusion','Telekinesis','Transmutation',
    'Telepathic Bond','Divination','Teleportation Circle','Conjuration','Wall of Force','Evocation','Wall of Stone']
    wiz6spells =['Chain Lightning', 'Circle of Death','Contingency','Create Undead','Disintegrate','Eyebite','Flesh to Stone','Freezing Spehre','Globe of Invulnerability','Guards and Wards','Instant Summons','Irresistible Dance','Magic Jar','Mass Suggestion','Move Earth','Programmed Illusion','Sunbeam','True Seeing','Wall of Ice']
    wiz7spells = ['Arcan Sword','Delayed Blas Fireball','Etherealness','Finger of Death','Forcecage','Magnificent Mansion','Mirage Arcane','Plane Shift','Prismatic Spray','Project Image','Reverse Gravity','Sequester','Simalucrum','Symbol','Teleport']
    wiz8spells=['Antimagic Field','Antipathy/Sympathy','Clone','Control Weather','Demiplane','Dominate Monster','Feeblemind','Incendiary Cloud','Maze','Mind Blank','Power Word Stun','Sunburst']
    wiz9spells= ['Astral Projection','Foresight','Gate','Imprisonment','Metero Swarm','Power Word Kill','Prismatic Wall','Shapechange','Time Stop','True Polymorph','Weird','Wish']

#this is for wizards under level 1 and 2 ********************************************
##Level 1 spells
    if level == 1 or level == 2:
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "3 Spell Slots")
        print("You have 3 level 1 spell slots")
        print("Known level 1 Spells:\n")
        wiz1spellslen = len(wiz1spells)
        var = 14
        var2 = 117.5
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =(f'{ran_can}'),
            border = 0)
            var2 =  var2 + 4.75
##Level 3 or 4 wizard ********************************************************
## first level spells
    if level == 3 or level == 4:
        var = 14
        var2 = 117.5
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "3 Spell Slots")
        print("You have 4 level 1 spell slots")
        print("Known level 1 Spells:\n")
        wiz1spellslen = len(wiz1spells)
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 =  var2 + 4.75

# level 2 spells*************************************
        print("You have 2 level 2 spell slots")
        print("Known level 2 Spells:\n")
        pdf.text(40, 191, "2 Spell Slots")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        for i in range(3):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75


## level 5 or 6 wizard *********************************************************
## Level 1 spells
    if level == 5 or level == 6:
        var = 14
        var2 = 117.5
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "4 Spell Slots")
        print("You have 4 level 1 spell slots")
        print("Known level 1 Spells:\n")
        wiz1spellslen = len(wiz1spells)
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 =  var2 + 4.75
# level 2 spells*************************************
        print("You have 2 level 2 spell slots")
        print("Known level 2 Spells:\n")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        pdf.text(40, 191, "3 Spell Slots")
        for i in range(3):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 3 spells********************************************
        print("You have 3 level 3 spell slots")
        print("Known level 3 Spells:\n")
        wiz3spellslen = len(wiz3spells)
        var = 80
        var2 = 59
        pdf.text(105,55, "2 Spell Slots")
        for i in range(4):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz3spellslen-1)
            ran_can = wiz3spells.pop(ran_num)
            wiz3spellslen = wiz3spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

## Level 7 or 8 wizard**********************************************************
## level 1 spells
    if level == 7 or level == 8:
        print("You have 4 level 1 spell slots")
        print("Known level 1  Spells:\n")
        var = 14
        var2 = 117.5
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "4 Spell Slots")
        wiz1spellslen = len(wiz1spells)
        for i in range(8):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

# level 2 spells*************************************
        print("You have 3 level 2 spell slots")
        print("Known level 2 Spells:\n")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        pdf.text(40, 191, "3 Spell Slots")
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 3 spells********************************************
        print("You have 3 level 3 spell slots")
        print("Known level 3 Spells:\n")
        wiz3spellslen = len(wiz3spells)
        var = 80
        var2 = 59
        pdf.text(105,55, "3 Spell Slots")
        for i in range(4):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz3spellslen-1)
            ran_can = wiz3spells.pop(ran_num)
            wiz3spellslen = wiz3spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 4 spells********************************************
        print("You have 2 level 4 spell slots")
        print("Known level 4 Spells:\n")
        wiz4spellslen = len(wiz4spells)
        var = 80
        var2 = 136.5
        pdf.text(105,132, "3 Spell Slots")
        for i in range(3):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz4spellslen-1)
            ran_can = wiz4spells.pop(ran_num)
            wiz4spellslen = wiz4spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

## leve 9 and 10 wizards********************************************************
    if level == 9 or level == 10:
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "4 Spell Slots")
        print("You have 4 level 1 spell slots")
        print("Known level 1 Spells:\n")
        var = 14
        var2 = 117.5
        wiz1spellslen = len(wiz1spells)
        for i in range(9):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 2 spells*************************************
        print("You have 3 level 2 spell slots")
        print("Known level 2 Spells:\n")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        pdf.text(40, 191, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 3 spells********************************************
        print("You have 3 level 3 spell slots")
        print("Known level 3 Spells:\n")
        wiz3spellslen = len(wiz3spells)
        var = 80
        var2 = 59
        pdf.text(105,55, "3 Spell Slots")
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz3spellslen-1)
            ran_can = wiz3spells.pop(ran_num)
            wiz3spellslen = wiz3spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 4 spells********************************************
        print("You have 3 level 4 spell slots")
        print("Known level 4 Spells:\n")
        wiz4spellslen = len(wiz4spells)
        var = 80
        var2 = 136.5
        pdf.text(105,132, "3 Spell Slots")
        for i in range(4):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz4spellslen-1)
            ran_can = wiz4spells.pop(ran_num)
            wiz4spellslen = wiz4spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 5 spells********************************************
        print("You have 2 level 5 spell slots")
        print("Known level 5 Spells:\n")
        wiz5spellslen = len(wiz5spells)
        var = 80
        var2= 214.75
        pdf.text(105,210, "1 Spell Slots")
        for i in range(3):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz5spellslen-1)
            ran_can = wiz5spells.pop(ran_num)
            wiz5spellslen = wiz5spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

## leve 11 and 12 wizards********************************************************
# level 1 spells
    if level == 11 or level == 12:
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "4 Spell Slots")
        print("You have 4 level 1 spell slots")
        print("Known level 1 Spells:\n")
        wiz1spellslen = len(wiz1spells)
        var = 14
        var2 = 117.5
        pdf.text(40, 191, "3 Spell Slots")
        for i in range(9):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 2 spells*************************************
        print("You have 3 level 2 spell slots")
        print("Known level 2 Spells:\n")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 3 spells********************************************
        print("You have 3 level 3 spell slots")
        print("Known level 3 Spells:\n")
        wiz3spellslen = len(wiz3spells)
        var = 80
        var2 = 59
        pdf.text(105,55, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz3spellslen-1)
            ran_can = wiz3spells.pop(ran_num)
            wiz3spellslen = wiz3spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 4 spells********************************************
        print("You have 3 level 4 spell slots")
        print("Known level 4 Spells:\n")
        wiz4spellslen = len(wiz4spells)
        var = 80
        var2 = 136.5
        pdf.text(105,132, "3 Spell Slots")
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz4spellslen-1)
            ran_can = wiz4spells.pop(ran_num)
            wiz4spellslen = wiz4spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 5 spells********************************************
        print("You have 2 level 5 spell slots")
        print("Known level 5 Spells:\n")
        wiz5spellslen = len(wiz5spells)
        var = 80
        var2= 214.75
        pdf.text(105,210, "2 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz5spellslen-1)
            ran_can = wiz5spells.pop(ran_num)
            wiz5spellslen = wiz5spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 6 spells********************************************
        print("You have 1 level 6 spell slots")
        print("Known level 6 Spells:\n")
        wiz6spellslen = len(wiz6spells)
        var = 150
        var2 = 59
        pdf.text(169,55, "1 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz6spellslen-1)
            ran_can = wiz6spells.pop(ran_num)
            wiz6spellslen = wiz6spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2 + 4.75

## level 13 and 14 wizards********************************************************
# level 1 spells
    if level == 13 or level == 14:
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "4 Spell Slots")
        print("You have 4 level 1 spell slots")
        print("Known level 1 Spells:\n")
        wiz1spellslen = len(wiz1spells)
        var = 14
        var2 = 117.5
        for i in range(9):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 2 spells*************************************
        print("You have 3 level 2 spell slots")
        print("Known level 2 Spells:\n")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        pdf.text(40, 191, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 3 spells********************************************
        print("You have 3 level 3 spell slots")
        print("Known level 3 Spells:\n")
        wiz3spellslen = len(wiz3spells)
        var = 80
        var2 = 59
        pdf.text(105,55, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz3spellslen-1)
            ran_can = wiz3spells.pop(ran_num)
            wiz3spellslen = wiz3spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 4 spells********************************************
        print("You have 3 level 4 spell slots")
        print("Known level 4 Spells:\n")
        wiz4spellslen = len(wiz4spells)
        var = 80
        var2 = 136.5
        pdf.text(105,132, "3 Spell Slots")
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz4spellslen-1)
            ran_can = wiz4spells.pop(ran_num)
            wiz4spellslen = wiz4spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 5 spells********************************************
        print("You have 2 level 5 spell slots")
        print("Known level 5 Spells:\n")
        wiz5spellslen = len(wiz5spells)
        var = 80
        var2= 214.75
        pdf.text(105,210, "2 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz5spellslen-1)
            ran_can = wiz5spells.pop(ran_num)
            wiz5spellslen = wiz5spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 6 spells********************************************
        print("You have 1 level 6 spell slots")
        print("Known level 6 Spells:\n")
        wiz6spellslen = len(wiz6spells)
        var = 150
        var2 = 59
        pdf.text(169,55, "1 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz6spellslen-1)
            ran_can = wiz6spells.pop(ran_num)
            wiz6spellslen = wiz6spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 7 spells********************************************
        print("You have 1 level 7 spell slots")
        print("Known level 7 Spells:\n")
        wiz7spellslen = len(wiz7spells)
        var = 150
        var2 = 117.75
        pdf.text(169,113, "1 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz7spellslen-1)
            ran_can = wiz7spells.pop(ran_num)
            wiz7spellslen = wiz7spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

## level 15 and 16 wizards********************************************************
# level 1 spells
    if level == 15 or level == 16:
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "4 Spell Slots")
        print("You have 4 level 1 spell slots")
        print("Known level 1 Spells:\n")
        wiz1spellslen = len(wiz1spells)
        var = 14
        var2 = 117.5
        for i in range(9):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 2 spells*************************************
        print("You have 3 level 2 spell slots")
        print("Known level 2 Spells:\n")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        pdf.text(40, 191, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 3 spells********************************************
        print("You have 3 level 3 spell slots")
        print("Known level 3 Spells:\n")
        wiz3spellslen = len(wiz3spells)
        var = 80
        var2 = 59
        pdf.text(105,55, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz3spellslen-1)
            ran_can = wiz3spells.pop(ran_num)
            wiz3spellslen = wiz3spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 4 spells********************************************
        print("You have 3 level 4 spell slots")
        print("Known level 4 Spells:\n")
        wiz4spellslen = len(wiz4spells)
        var = 80
        var2 = 136.5
        pdf.text(105,132, "3 Spell Slots")
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz4spellslen-1)
            ran_can = wiz4spells.pop(ran_num)
            wiz4spellslen = wiz4spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 5 spells********************************************
        print("You have 2 level 5 spell slots")
        print("Known level 5 Spells:\n")
        wiz5spellslen = len(wiz5spells)
        var = 80
        var2= 214.75
        pdf.text(105,210, "2 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz5spellslen-1)
            ran_can = wiz5spells.pop(ran_num)
            wiz5spellslen = wiz5spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 6 spells********************************************
        print("You have 1 level 6 spell slots")
        print("Known level 6 Spells:\n")
        wiz6spellslen = len(wiz6spells)
        var = 150
        var2 = 59
        pdf.text(169,55, "1 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz6spellslen-1)
            ran_can = wiz6spells.pop(ran_num)
            wiz6spellslen = wiz6spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 7 spells********************************************
        print("You have 1 level 7 spell slots")
        print("Known level 7 Spells:\n")
        wiz7spellslen = len(wiz7spells)
        var = 150
        var2 = 117.75
        pdf.text(169,113, "1 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz7spellslen-1)
            ran_can = wiz7spells.pop(ran_num)
            wiz7spellslen = wiz7spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 8 spells********************************************
        print("You have 1 level 8 spell slots")
        print("Known level 8 Spells:\n")
        wiz8spellslen = len(wiz8spells)
        var = 150
        var2 = 176
        pdf.text(169,171, "1 Spell Slots")
        for i in range(1):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz8spellslen-1)
            ran_can = wiz8spells.pop(ran_num)
            wiz8spellslen = wiz8spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

## level 17 and 18     ********************************************************
# level 1 spells
    if level == 17 or level == 18:
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "4 Spell Slots")
        print("You have 4 level 1 spell slots")
        print("Known level 1 Spells:\n")
        wiz1spellslen = len(wiz1spells)
        var = 14
        var2 = 117.5
        for i in range(9):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 2 spells*************************************
        print("You have 3 level 2 spell slots")
        print("Known level 2 Spells:\n")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        pdf.text(40, 191, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 3 spells********************************************
        print("You have 3 level 3 spell slots")
        print("Known level 3 Spells:\n")
        wiz3spellslen = len(wiz3spells)
        var = 80
        var2 = 59
        pdf.text(105,55, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz3spellslen-1)
            ran_can = wiz3spells.pop(ran_num)
            wiz3spellslen = wiz3spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 4 spells********************************************
        print("You have 3 level 4 spell slots")
        print("Known level 4 Spells:\n")
        wiz4spellslen = len(wiz4spells)
        var = 80
        var2 = 136.5
        pdf.text(105,132, "3 Spell Slots")
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz4spellslen-1)
            ran_can = wiz4spells.pop(ran_num)
            wiz4spellslen = wiz4spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 5 spells********************************************
        print("You have 2 level 5 spell slots")
        print("Known level 5 Spells:\n")
        wiz5spellslen = len(wiz5spells)
        var = 80
        var2= 214.75
        pdf.text(105,210, "2 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz5spellslen-1)
            ran_can = wiz5spells.pop(ran_num)
            wiz5spellslen = wiz5spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 6 spells********************************************
        print("You have 1 level 6 spell slots")
        print("Known level 6 Spells:\n")
        wiz6spellslen = len(wiz6spells)
        var = 150
        var2 = 59
        pdf.text(169,55, "1 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz6spellslen-1)
            ran_can = wiz6spells.pop(ran_num)
            wiz6spellslen = wiz6spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 7 spells********************************************
        print("You have 1 level 7 spell slots")
        print("Known level 7 Spells:\n")
        wiz7spellslen = len(wiz7spells)
        var = 150
        var2 = 117.75
        pdf.text(169,113, "1 Spell Slots")
        for i in range(1):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz7spellslen-1)
            ran_can = wiz7spells.pop(ran_num)
            wiz7spellslen = wiz7spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 8 spells********************************************
        print("You have 1 level 8 spell slots")
        print("Known level 8 Spells:\n")
        wiz8spellslen = len(wiz8spells)
        var = 150
        var2 = 176
        pdf.text(169,171, "1 Spell Slots")
        for i in range(1):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz8spellslen-1)
            ran_can = wiz8spells.pop(ran_num)
            wiz8spellslen = wiz8spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

# level 9 spells********************************************
        print("You have 1 level 9 spell slots")
        print("Known level 9 Spells:\n")
        wiz9spellslen = len(wiz9spells)
        var = 159
        var2 = 224
        pdf.text(169,220, "1 Spell Slots")
        for i in range(1):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz9spellslen-1)
            ran_can = wiz9spells.pop(ran_num)
            wiz9spellslen = wiz9spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
## level 19 and 20 wizards********************************************************
#level 1 spells
    if level == 19 or level == 20:
        pdf.set_font("Arial",size = 12)
        pdf.text(40, 112, "4 Spell Slots")
        print("You have 4 level 1 spell slots")
        print("Known level 1 Spells:\n")
        wiz1spellslen = len(wiz1spells)
        var = 14
        var2 = 117.5
        pdf.text(40, 191, "3 Spell Slots")
        for i in range(9):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz1spellslen-1)
            ran_can = wiz1spells.pop(ran_num)
            wiz1spellslen = wiz1spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

# level 2 spells*************************************
        print("You have 3 level 2 spell slots")
        print("Known level 2 Spells:\n")
        wiz2spellslen = len(wiz2spells)
        var = 14
        var2 = 195.5
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz2spellslen-1)
            ran_can = wiz2spells.pop(ran_num)
            wiz2spellslen = wiz2spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 3 spells********************************************
        print("You have 3 level 3 spell slots")
        print("Known level 3 Spells:\n")
        wiz3spellslen = len(wiz3spells)
        var = 80
        var2 = 59
        pdf.text(105,55, "3 Spell Slots")
        for i in range(6):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz3spellslen-1)
            ran_can = wiz3spells.pop(ran_num)
            wiz3spellslen = wiz3spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 4 spells********************************************
        print("You have 3 level 4 spell slots")
        print("Known level 4 Spells:\n")
        wiz4spellslen = len(wiz4spells)
        var = 80
        var2 = 136.5
        pdf.text(105,132, "3 Spell Slots")
        for i in range(5):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz4spellslen-1)
            ran_can = wiz4spells.pop(ran_num)
            wiz4spellslen = wiz4spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 5 spells********************************************
        print("You have 2 level 5 spell slots")
        print("Known level 5 Spells:\n")
        wiz5spellslen = len(wiz5spells)
        var = 80
        var2= 214.75
        pdf.text(105,210, "2 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz5spellslen-1)
            ran_can = wiz5spells.pop(ran_num)
            wiz5spellslen = wiz5spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 6 spells********************************************
        print("You have 2 level 6 spell slots")
        print("Known level 6 Spells:\n")
        wiz6spellslen = len(wiz6spells)
        var = 150
        var2 = 59
        pdf.text(169,55, "2 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz6spellslen-1)
            ran_can = wiz6spells.pop(ran_num)
            wiz6spellslen = wiz6spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 7 spells********************************************
        print("You have 2 level 7 spell slots")
        print("Known level 7 Spells:\n")
        wiz7spellslen = len(wiz7spells)
        var = 150
        var2 = 117.75
        pdf.text(169,113, "1 Spell Slots")
        for i in range(2):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz7spellslen-1)
            ran_can = wiz7spells.pop(ran_num)
            wiz7spellslen = wiz7spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75
# level 8 spells********************************************
        print("You have 1 level 8 spell slots")
        print("Known level 8 Spells:\n")
        wiz8spellslen = len(wiz8spells)
        var = 150
        var2 = 176
        pdf.text(169,171, "1 Spell Slots")
        for i in range(1):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz8spellslen-1)
            ran_can = wiz8spells.pop(ran_num)
            wiz8spellslen = wiz8spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

# level 9 spells********************************************
        print("You have 1 level 9 spell slots")
        print("Known level 9 Spells:\n")
        wiz9spellslen = len(wiz9spells)
        var = 159
        var2 = 224
        pdf.text(169,220, "1 Spell Slots")
        for i in range(1):
            pdf.set_xy(var, var2)
            ran_num = random.randint(0, wiz9spellslen-1)
            ran_can = wiz9spells.pop(ran_num)
            wiz9spellslen = wiz9spellslen - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75

def cantrips():
    wizardcantrips = ['Acid Splash', 'Blade Ward', 'Blooming Blade', 'Chill Touch', 'Control Flames', 'Create Bonfire', 'Dancing Lights',
    'Encode Thoughts', 'Fire Bolt', 'Friends', 'Frostbite', 'Green-Flame Blade', 'Gust', 'Infestation', 'Light', 'Lightning Lure',
    'Mage Hand', 'Mending', 'Message', 'Mind Silver', 'Minor Illusion', 'Mold Earth', 'On/Off', 'Poison Spray','Prestidigitation',
    'Ray of Frost', 'Snapping String', 'Shape of Water', 'Shocking Grasp', 'Sword Bust', 'Thunderclap', 'Toll of the Dead', 'True Strike']
    if level < 5:
        print("Cantrips:\n")
        wizcantrips = len(wizardcantrips)
        var = 14
        var2 = 59
        for i in range(4):
            pdf.set_xy(var,var2)
            ran_num = random.randint(0, wizcantrips-1)
            ran_can = wizardcantrips.pop(ran_num)
            wizcantrips = wizcantrips - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+4.75


    if level >= 5:
        print("Cantrips:\n")
        wizcantrips = len(wizardcantrips)
        var = 14
        var2 = 59
        for i in range(5):
            pdf.set_xy(var,var2)
            ran_num = random.randint(0, wizcantrips - 1)
            ran_can = wizardcantrips.pop(ran_num)
            wizcantrips = wizcantrips - 1
            print(ran_can)
            pdf.set_font("Arial",size =10)
            pdf.multi_cell(w=55, h =5,
            txt =f'{ran_can}',
            border = 0)
            var2 = var2+ 4.75


cantrips()
spells()
window.mainloop()
pdf.output("randomcharacter.pdf")
file = open("randomcharacter.pdf")
webbrowser.open("randomcharacter.pdf")
