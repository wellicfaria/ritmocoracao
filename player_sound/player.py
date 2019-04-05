import pygame as pygame
from sound import getSoundOfaHistoy
from time import sleep

path_sounds = '../sounds_history'


x = getSoundOfaHistoy('0','0')

path_sound = '{}/{}/{}'.format(path_sounds,x['folder'],x['name_sound'])
print(path_sound)

#pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound(path_sound)
sounda.play()



