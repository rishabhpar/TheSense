from SafeSpot import SafeSpot
from GasLeak import GasLeak
from Person import Person
import sys
import pygame                           # MAKE SURE TO DOWNLOAD PYGAME
                                        # www.pygame.org/download.shtml

# Define
Open = 0   # open spot
Unsafe = -1  # unsafe spot
Gas = -500

WHITE = (240, 248, 255)
GREEN = (60, 179, 113)
BLUE = (0, 0, 139)
RED = (220, 20, 60)
PURPLE = (148,0,211)

TileColor = {
    Open: WHITE,
    Unsafe: RED,
    Gas: PURPLE
}

#********** MAP 1 **********#
# will have 4 safe spots of equal square sizes
# will have 1 person
# will have 1 gas leak


# Step 1: Create a 100 by 100 grid
map1 = [[Open]*100 for n in range(100)]

# Step 2: Create Safe Spots where [0,0] is ordered pair of row 0, column 0
# a coordinate pair is like having the person's GPS longitude, latitude information
ss1 = SafeSpot(1, [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                   [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                   [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                   [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                   [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]], False)
ss2 = SafeSpot(2, [[50, 65], [50, 66], [50, 67], [50, 68], [50, 69],
                   [51, 65], [51, 66], [51, 67], [51, 68], [51, 69],
                   [52, 65], [52, 66], [52, 67], [52, 68], [52, 69],
                   [53, 65], [53, 66], [53, 67], [53, 68], [53, 69],
                   [54, 65], [54, 66], [54, 67], [54, 68], [54, 69]], False)
ss3 = SafeSpot(3, [[95, 0], [95, 1], [95, 2], [95, 3], [95, 4],
                   [96, 0], [96, 1], [96, 2], [96, 3], [96, 4],
                   [97, 0], [97, 1], [97, 2], [97, 3], [97, 4],
                   [98, 0], [98, 1], [98, 2], [98, 3], [98, 4],
                   [99, 0], [99, 1], [99, 2], [99, 3], [99, 4]], False)
ss4 = SafeSpot(4, [[0, 95], [0, 96], [0, 97], [0, 98], [0, 99],
                   [1, 95], [1, 96], [1, 97], [1, 98], [1, 99],
                   [2, 95], [2, 96], [2, 97], [2, 98], [2, 99],
                   [3, 95], [3, 96], [3, 97], [3, 98], [3, 99],
                   [4, 95], [4, 96], [4, 97], [4, 98], [4, 99]], False)

listOfSafeSpots = [ss1, ss2, ss3, ss4]

# Step 3: Update the grid with safespots
for spot in listOfSafeSpots:
    for index in spot.get_list():
        map1[index[0]][index[1]] = spot.get_id()

# Step 4: update TileColors to reflect new safespots
TileColor[ss1.get_id()] = GREEN
TileColor[ss2.get_id()] = GREEN
TileColor[ss3.get_id()] = GREEN
TileColor[ss4.get_id()] = GREEN

# Step 5: create instances of people. This simulates getting the person's
# location once a gas leak is identified.
p1 = Person(28, 75, 101, True)
map1[p1.get_row()][p1.get_col()] = p1.get_id()
TileColor[p1.get_id()] = BLUE

# Step 6: create THE gas leak. Simulates a location ping from Blackline Safety
gl = GasLeak(25, 67, 0)
map1[gl.get_row()][gl.get_col()] = Gas

# Step : Define necessary
TILESIZE = 5
MAPWIDTH = 100
MAPLENGTH = 100

# Step : Create the map
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPLENGTH*TILESIZE))

for row in range(MAPLENGTH):
    for col in range(MAPWIDTH):
        pygame.draw.rect(DISPLAY, TileColor[map1[row][col]],
                         (col*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

# add the gas leak



pygame.display.update()

while True:

    for event in pygame.event.get():
        # if you press the X in the top-right corner
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw Map
    for row in range(MAPLENGTH):
        for col in range(MAPWIDTH):
            pygame.draw.rect(DISPLAY, TileColor[map1[row][col]],
                             (col*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

    # Update Display
    pygame.display.update()

