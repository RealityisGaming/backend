import math
import random

enemy_stats = [
  {
    "slime": { 
      "slime_strength" : 4,
      "slime_agi" : 6,
      "slime_con" : 8,
      "slime_spr" : 6,
      "slime_hp" : 10,
      "btl_speed": dice['1d20'] + 1
    }
  },
  {
    'red_slime': {
      "red_slime_strength" : 5,
      "red_slime_agi" : 7,
      "red_slime_con" : 9,
      "red_slime_spr" : 7,
      "red_slime_hp" : 15,
      "btl_speed": dice['1d20'] + 2
    }
  },
  { 
    'purple_slime': {
      "purple_slime_strength" : 7,
      "purple_slime_agi" : 10,
      "purple_slime_con" : 11,
      "purple_slime_spr" : 9,
      "purple_slime_hp" : 10,
      "btl_speed": dice['1d20'] + 4
    }
  }
]


enemy_initative = {
  'slime': dice['1d20'] + enemy_stats[0]['slime']['slime_agi'],
  'red_slime': dice['1d20'] + enemy_stats[1]['red_slime']['red_slime_agi'],
  'purple_slime': dice['1d20'] + enemy_stats[2]['purple_slime']['purple_slime_agi']
}

slime = enemy_stats[0]
red_slime = enemy_stats[1]
purple_slime = enemy_stats[2]

enemy_list = [slime, red_slime, purple_slime]

slime = 2
red_slime = slime * 1.50
purple_slime = slime * 2.50