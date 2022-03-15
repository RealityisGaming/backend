import math
import random
# #Make variables to shorten the code


dice = {
  "2d8": random.randrange(2, 17),
  "2d4": random.randrange(2, 9),
  "1d8": random.randrange(1, 9),
  "1d20": random.randrange(1, 21)
}


# a
hero_stats = [
  {
    "warrior": { 
      "warrior_strength" : 8,
      "warrior_agi" : 3,
      "warrior_con" : 12,
      "warrior_spr" : 5,
      "warrior_hp" : 70,
      "btl_speed": dice['1d20'] + 5
    }
  },
  {
    'thief': {
      "thief_strength" : 4,
      "thief_agi" : 12,
      "thief_con" : 6,
      "thief_spr" : 3,
      "thief_hp" : 35,
      "btl_speed": dice['1d20'] + 3
    }
  },
  { 
    'mage': {
      "mage_strength" : 3,
      "mage_agi" : 4,
      "mage_con" : 5,
      "mage_spr" : 1,
      "mage_hp" : 18,
      "btl_speed": dice['1d20'] + 2
    }
  }
]


hero_battle = {
"warrior_dmg": dice['2d8'] + hero_stats[0]['warrior']['warrior_strength'],
"thief_dmg": dice['2d4'] + hero_stats[1]['thief']['thief_agi'],
"mage_dmg": dice['1d8'] + hero_stats[2]['mage']['mage_spr']
}

hero_initative = {
"warrior_btl_speed": dice['1d20'] + hero_stats[0]['warrior']['warrior_agi'],
"thief_btl_speed": dice['1d20'] + hero_stats[1]['thief']['thief_agi'],
"mage_btl_speed": dice['1d20'] + hero_stats[2]['mage']['mage_agi']
}

hero_hitchance = {
'warrior_hitchance': dice['1d20'] + hero_stats[0]['warrior']['warrior_strength'],
'thief_hitchance': dice['1d20'] + hero_stats[1]['thief']['thief_agi'],
'mage_hitchance': dice['1d20'] + hero_stats[2]['mage']['mage_spr']
}


warrior = hero_stats[0]
thief = hero_stats[1]
mage = hero_stats[2]


hero_list = [warrior, thief, mage]


player_one = random.choice(hero_list)


warrior = 'Warrior'
thief = 'Thief'
mage = 'Mage'

name = 'Markaeus'
level = 1
xp = 0
baseXP = 100
job = warrior
exponent = 1.65
lvlNext = math.floor(baseXP * (level ** exponent))

slime = 2
red_slime = slime * 1.50
purple_slime = slime * 2.50

def xp_gain(enemy):
  if enemy == slime:
    print('Exp gained: ', enemy)
  else:
    print('Exp gained: ', enemy)
  #TO DO return f'Gained {xp}'




# levelup(job)
while xp >= lvlNext:
  # TODO
  # nest level cap here
  # level >= 100
  level += 1
  xp = xp - lvlNext
  lvlNext = round(lvlNext * 1.5)
  # xp_gain = 

# while xp >= lvlNext:
#     strength = 

print('Character Name: ' + name)
print("Level: ", level)
print( "Class: ", job)



# """
def strength(work):
  if job == warrior:
    print('Strength: ', hero_stats[0]['warrior']['warrior_strength'])
  elif job == thief:
    print('Strength: ', hero_stats[1]['thief']['thief_strength'])
  else:
    print('Strength: ', hero_stats[2]['mage']['mage_strength'])


strength(job)

def agility(work):
  if job == warrior:
    print('Agility: ', hero_stats[0]['warrior']['warrior_agi'])
  elif job == thief:
    print('Agility: ', hero_stats[1]['thief']['thief_agi'])
  else:
    print('Agility: ', hero_stats[2]['mage']['mage_agi'])


agility(job)

def constitution(work):
  if job == warrior:
    print('Constitution: ', hero_stats[0]['warrior']['warrior_con'])
  elif job == thief:
    print('Constitution: ', hero_stats[1]['thief']['thief_agi'])
  else:
    print('Constitution: ', hero_stats[2]['mage']['mage_agi'])


constitution(job)

def health_point(work):
  if job == warrior:
    print('Health Points: ', hero_stats[0]['warrior']['warrior_hp'])
  elif job == thief:
    print('Health Points: ', hero_stats[1]['thief']['thief_hp'])
  else:
    print('Health Points: ', hero_stats[2]['mage']['mage_hp'])


health_point(job)

def initiative(work):
  if job == warrior:
    print('Initiative:',  hero_initative['warrior_btl_speed'])
  elif job == thief:
    print('Initiative:',  hero_initative['thief_btl_speed'])
  else:
    print('Initiative:',  hero_initative['mage_btl_speed'])


initiative(job)

def damage(work):
  if job == warrior:
    print('Damage:' , hero_battle['warrior_dmg'])
  elif job == thief:
    print('Damage:' , hero_battle['thief_dmg'])
  else:
    print('Damage:' , hero_battle['mage_dmg'])


damage(job)
# """
print("EXP: ", xp)
print("Next:", lvlNext)


enemy = purple_slime 

def enemies(bad):
  if bad == slime:
    print('Enemy Initiative:',  enemy_initative['slime'])
  elif bad == red_slime:
    print('Enemy Initiative:',  enemy_initative['red_slime'])
  else:
    print('Enemy Initative: ', enemy_initative['purple_slime'])

enemies(enemy)
xp_gain(enemy)
# combat = hero_stats[0]['btl_speed'] > enemy_stats[0]['btl_speed']

# def who_first(combat):
#   if combat == True:
#     print('Hero goes first')
#   else:
#     print('Enemy goes first')

# who_first(job, enemy)
# def combat_system(a, n):
#   if a <= n:
#     print("{enemy} goes first")
#   else:
#     print("{hero} goes first")

# combat_system(initiative, enemies)

#TODO


# warrior = hero_stats[0]
# thief = hero_stats[1]
# mage = hero_stats[2]
# slime = enemy_stats[0]
# red_slime = enemy_stats[1]
# purple_slime = enemy_stats[2]


# hero_list = [warrior, thief, mage]
# enemy_list = [slime, red_slime, purple_slime]


# print(hero_list[0]['warrior']['btl_speed'])


# player_one = random.choice(hero_list)
# computer = random.choice(enemy_list)


# print(player_one)
# print(computer)
# print(combat)


# def start_game(hero_list, enemy_list):
#   warrior = hero_stats[0]
#   thief = hero_stats[1]
#   mage = hero_stats[2]
#   slime = enemy_stats[0]
#   red_slime = enemy_stats[1]
#   purple_slime = enemy_stats[2]


#   hero_list = [warrior, thief, mage]
#   enemy_list = [slime, red_slime, purple_slime]


#   player_one = random.choice(hero_list)
#   computer = random.choice(enemy_list)

#   if player_one == warrior and computer == slime:
#     combat = hero_list['btle_speed'] > enemy_list['btl_speed']
#     print(combat[0], combat[1])
#   if player_one == thief and computer == slime:
#     combat = hero_list['btle_speed'] > enemy_list['btl_speed']
#     print(combat[0], combat[1])
#   if player_one == mage and computer == slime:
#     combat = hero_list['btle_speed'] > enemy_list['btl_speed']
#     print(combat[0], combat[1])

# start_game(hero_list, enemy_list)


# who_first(combat)