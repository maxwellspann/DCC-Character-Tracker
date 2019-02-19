# -*- coding: utf-8 -*-

class Character:
    
    def __init__(self, name, ch_class, title, alignment, speed, level, xp, strength, agility, stamina, personality, intelligence, luck, AC, max_hp, initiative, actions, attack, crit_die, crit_table, ref_save, fort_save, will_save):
        self.name = name
        self.ch_class = ch_class
        self.title = title
        self.alignment = alignment
	self.speed = speed
	self.level = level
	self.xp = xp
	self.strength = strength
	self.agility = agility
	self.stamina = stamina
	self.personality = personality
	self.intelligence = intelligence
	self.luck = luck
	self.AC = AC
	self.max_hp = max_hp
	self.initiative = initiative
	self.actions = actions
	self.attack = attack
	self.crit_die = crit_die
	self.crit_table = crit_table
	self.ref_save = ref_save
	self.fort_save = fort_save
	self.will_save = will_save

character_1 = Character('Sigmund', 'Wizard', 'Enchanter', 'Neutral', 30, 2, 76, 12, 9, 18, 12, 12, 16, 12, 21, 0, '1D20', '+1', '1D6', 'I', 0, 4, 1)
print(character_1.name)
print(character_1.strength)
print(character_1.will_save)
print(character_1.AC)

