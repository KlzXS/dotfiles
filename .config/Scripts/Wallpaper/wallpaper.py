import sys
import os
import random

from os import listdir
from os.path import isfile, join
from shutil import copyfile
from datetime import datetime

#Gets all available wallpapers
mypath = "/home/ajaw/Wallpaper"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
files.sort()

#Gets the most recent wallpapers sothat they aren't overused
filew = []
recent=5
fi = open("/home/ajaw/.config/Scripts/Wallpaper/wallpapers", "r")

for i in range(1,recent+1):
    tmp = fi.read(7)
    filew.append(tmp)
fi.close()

#Removes them from list
for i in filew:
    tmp = i[6:]
    tmp = int(tmp)
    del files[tmp-1]

wallpapers = len(files)

random.seed(datetime.now())
choose = random.randrange(0, wallpapers)

wallpaper = files[choose]
del filew[0]
filew.append(wallpaper)

wallpaper = "/home/ajaw/Wallpaper/" + wallpaper
copyfile(wallpaper, "/home/ajaw/.config/wall.png")

fi = open("/home/ajaw/.config/Scripts/Wallpaper/wallpapers", "w")
for i in filew:
    fi.write(i)
fi.close()

