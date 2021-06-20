
def calculate_monster_health(player_damage, player_to_hit, monster_armor):
  #How long should the combat last
  rounds_until_player_victory = 2.5
  #How many players are in the party
  party_size = 4
  #How many attacks should players have to make
  #before th monsters are defeated
  attacks_until_defeat = 10
  return 10 * player_damage * (20 - (monster_armor - player_to_hit)) * .05

#Player hit percentage is how often you want the players to hit the monster
def calculate_monster_armor(player_to_hit, chance_to_hit):
  return player_to_hit + 20 - 20 * chance_to_hit

def calculate_monster_health_and_armor(player_damage, player_to_hit, chance_to_hit):
  monster_armor = calculate_monster_armor(player_to_hit, chance_to_hit)
  monster_health = calculate_monster_health(player_damage, player_to_hit, monster_armor)
  return monster_health, monster_armor


assert(calculate_monster_health(10, 8, 20) == 40)
assert(calculate_monster_armor(8, .4) == 20)
assert(calculate_monster_health_and_armor(10, 8, .4) == (40, 20))

def calculate_monster_to_hit(player_armor, monster_hit_chance):
  return player_armor - 20 + 20 * monster_hit_chance
  # return int((player_armor - 10) / monster_hit_chance)

def calculate_monster_damage(party_health, monster_hit_chance):
  rounds_until_monster_victory = 3
  return int(party_health / (rounds_until_monster_victory * monster_hit_chance))

assert(calculate_monster_to_hit(15, .5) == 5)
assert(calculate_monster_to_hit(15, .8) == 11)
assert(calculate_monster_damage(88, .6) == 48)


def calculate_monster_stat_table(player_damages, player_to_hits, chance_to_hits, party_health, monster_chance_to_hit, player_armors):
  assert(len(player_damages) == len(player_to_hits) == len(chance_to_hits) == len(party_health) == len(monster_chance_to_hit) == len(player_armors))
  stats = zip(player_damages, player_to_hits, chance_to_hits, party_health, monster_chance_to_hit, player_armors)
  monster_healths = []
  monster_armors = []
  monster_to_hits = []
  monster_damages = []
  for stat in stats:
    monster_health, monster_armor = calculate_monster_health_and_armor(stat[0], stat[1], stat[2])
    monster_healths.append(monster_health)
    monster_armors.append(monster_armor)
    monster_to_hits.append(calculate_monster_to_hit(stat[5], stat[4]))
    monster_damages.append(calculate_monster_damage(stat[3], stat[4]))
  monster_stats = dict()
  monster_stats['health'] = monster_healths
  monster_stats['armors'] = monster_armors
  monster_stats['to_hit'] = monster_to_hits
  monster_stats['damage'] = monster_damages
  return monster_stats

player_damages = [12, 13, 14, 17, 20, 27, 27, 32, 37, 37]
player_to_hits = [6, 7, 8, 8, 8, 10, 11, 11, 11, 11]
chance_to_hits = [.6, .6, .6, .6, .6, .6, .55, .55, .55, .5]
party_size = 4
player_health = [20, 22, 24, 25, 27, 28, 30, 33, 35, 35]
party_health = []
for health in player_health:
  party_health.append(health * party_size)
monster_chance_to_hit = [.5, .5, .55, .55, .6, .6, .65, .65, .7, .7]
player_armors = [16, 16, 16, 18, 18, 18, 18, 20, 20, 20]

print(calculate_monster_stat_table(player_damages, player_to_hits, chance_to_hits, party_health, monster_chance_to_hit, player_armors))


