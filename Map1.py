from SafeSpot import SafeSpot
from GasLeak import GasLeak
from Person import Person
import sys
import math
import pygame                           # MAKE SURE TO DOWNLOAD PYGAME
                                        # www.pygame.org/download.shtml
# Define
Open = 0  # open spot
Unsafe = -1  # unsafe spot
Gas = -500

WHITE = (240, 248, 255)
GREEN = (60, 179, 113)
BLUE = (0, 0, 139)
RED = (220, 20, 60)
PURPLE = (148, 0, 211)

TileColor = {
    Open: WHITE,
    Unsafe: RED,
    Gas: PURPLE
}


def run_map1():
    # ********** MAP 1 **********#
    # will have 4 safe spots of equal square sizes
    # will have 1 person
    # will have 1 gas leak

    # Step 1: Create a 100 by 100 grid
    map1 = [[Open] * 100 for n in range(100)]

    # Step 2: Create Safe Spots where [0,0] is ordered pair of row 0, column 0
    # a coordinate pair is like having the person's GPS longitude, latitude information
    ss1 = SafeSpot(1, [[0, 0, False], [0, 1, False], [0, 2, False], [0, 3, False], [0, 4, False],
                       [1, 0, False], [1, 1, False], [1, 2, False], [1, 3, False], [1, 4, False],
                       [2, 0, False], [2, 1, False], [2, 2, False], [2, 3, False], [2, 4, False],
                       [3, 0, False], [3, 1, False], [3, 2, False], [3, 3, False], [3, 4, False],
                       [4, 0, False], [4, 1, False], [4, 2, False], [4, 3, False], [4, 4, False]], 25)
    ss2 = SafeSpot(2, [[50, 65, False], [50, 66, False], [50, 67, False], [50, 68, False], [50, 69, False],
                       [51, 65, False], [51, 66, False], [51, 67, False], [51, 68, False], [51, 69, False],
                       [52, 65, False], [52, 66, False], [52, 67, False], [52, 68, False], [52, 69, False],
                       [53, 65, False], [53, 66, False], [53, 67, False], [53, 68, False], [53, 69, False],
                       [54, 65, False], [54, 66, False], [54, 67, False], [54, 68, False], [54, 69, False]], 25)
    ss3 = SafeSpot(3, [[95, 0, False], [95, 1, False], [95, 2, False], [95, 3, False], [95, 4, False],
                       [96, 0, False], [96, 1, False], [96, 2, False], [96, 3, False], [96, 4, False],
                       [97, 0, False], [97, 1, False], [97, 2, False], [97, 3, False], [97, 4, False],
                       [98, 0, False], [98, 1, False], [98, 2, False], [98, 3, False], [98, 4, False],
                       [99, 0, False], [99, 1, False], [99, 2, False], [99, 3, False], [99, 4, False]], 25)
    ss4 = SafeSpot(4, [[0, 95, False], [0, 96, False], [0, 97, False], [0, 98, False], [0, 99, False],
                       [1, 95, False], [1, 96, False], [1, 97, False], [1, 98, False], [1, 99, False],
                       [2, 95, False], [2, 96, False], [2, 97, False], [2, 98, False], [2, 99, False],
                       [3, 95, False], [3, 96, False], [3, 97, False], [3, 98, False], [3, 99, False],
                       [4, 95, False], [4, 96, False], [4, 97, False], [4, 98, False], [4, 99, False]], 25)

    ss1.locationCenter = ss1.listOfSpotsOccupied[12]  # floor(count/2)
    ss2.locationCenter = ss2.listOfSpotsOccupied[12]
    ss3.locationCenter = ss3.listOfSpotsOccupied[12]
    ss4.locationCenter = ss4.listOfSpotsOccupied[12]

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
    listOfEmployees = [p1]

    for emp in listOfEmployees:
        map1[emp.get_row()][emp.get_col()] = emp.get_id()
        TileColor[emp.get_id()] = BLUE

    # Step 6: create THE gas leak. Simulates a location ping from Blackline Safety
    # coupled with the wind direction data
    windData = 90
    gl = GasLeak(25, 67, windData)
    map1[gl.get_row()][gl.get_col()] = Gas

    # Step 7: Define necessary values
    TILESIZE = 5
    MAPWIDTH = 100
    MAPLENGTH = 100
    WIDTH = TILESIZE * MAPWIDTH
    HEIGHT = TILESIZE * MAPLENGTH
    DEG = 45

    # Step 8: Create the map without wind
    pygame.init()
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

    for row in range(MAPLENGTH):
        for col in range(MAPWIDTH):
            pygame.draw.rect(DISPLAY, TileColor[map1[row][col]],
                             (col * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))

    pygame.display.update()

    # Step 9: add the gas leak wind indicator and cone of danger. For simplicity, we only
    # allowed the wind to go in the direct north, east, south, or west direction

    if 315 <= gl.get_direction() <= 359 or 0 <= gl.get_direction() <= 44:  # north
        x = gl.get_row() - 1
        y = gl.get_col()

        while x >= 0:
            if 1 <= map1[x][y] <= 101:  # very inefficient implementation
                for spot in listOfSafeSpots:
                    if spot.get_id() == map1[x][y]:
                        for index in spot.get_list():
                            if index[0] == x and index[1] == y:
                                index[2] = True
            elif map1[x][y] >= 101:
                for emp in listOfEmployees:
                    if emp.id == map1[x][y]:
                        emp.safe = False
            else:
                map1[x][y] = Unsafe
            x = x - 1

        x = gl.get_row() - 1
        iteration = 1
        while x >= 0:
            for q in range(1, iteration + 1):
                if y - q >= 0:
                    if 1 <= map1[x][y - q] < 101:  # very inefficient implementation
                        for spot in listOfSafeSpots:
                            if spot.get_id() == map1[x][y - q]:
                                for index in spot.get_list():
                                    if index[0] == x and index[1] == y - q:
                                        index[2] = True
                    elif map1[x][y - q] >= 101:
                        for emp in listOfEmployees:
                            if emp.id == map1[x][y - q]:
                                emp.safe = False
                    else:
                        map1[x][y - q] = Unsafe
                if y + q < MAPWIDTH:
                    if 1 <= map1[x][y + q] < 101:  # very inefficient implementation
                        for spot in listOfSafeSpots:
                            if spot.get_id() == map1[x][y + q]:
                                for index in spot.get_list():
                                    if index[0] == x and index[1] == y + q:
                                        index[2] = True
                    elif map1[x][y + q] >= 101:
                        for emp in listOfEmployees:
                            if emp.id == map1[x][y + q]:
                                emp.safe = False
                    else:
                        map1[x][y + q] = Unsafe
            x = x - 1
            iteration = iteration + 1

            for row in range(MAPLENGTH):
                for col in range(MAPWIDTH):
                    pygame.draw.rect(DISPLAY, TileColor[map1[row][col]],
                                     (col * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
            pygame.display.update()

        pygame.draw.line(DISPLAY, BLUE,
                         (gl.get_col() * TILESIZE + TILESIZE / 2, gl.get_row() * TILESIZE),
                         (gl.get_col() * TILESIZE + TILESIZE / 2, gl.get_row() * TILESIZE - HEIGHT))

    elif 45 <= gl.get_direction() <= 134:  # east
        x = gl.get_row()
        y = gl.get_col() + 1

        while y < MAPWIDTH:
            if 1 <= map1[x][y] < 101:  # very inefficient implementation
                for spot in listOfSafeSpots:
                    if spot.get_id() == map1[x][y]:
                        for index in spot.get_list():
                            if index[0] == x and index[1] == y:
                                index[2] = True
            elif map1[x][y] >= 101:  # very inefficient implementation
                for emp in listOfEmployees:
                    if emp.get_id() == map1[x][y]:
                        emp.safe = False
            else:
                map1[x][y] = Unsafe
            y = y + 1

        y = gl.get_col() + 1
        iteration = 1
        while y < MAPWIDTH:
            for q in range(1, iteration + 1):
                if x - q >= 0:
                    if 1 <= map1[x - q][y] < 101:  # very inefficient implementation
                        for spot in listOfSafeSpots:
                            if spot.get_id() == map1[x - q][y]:
                                for index in spot.get_list():
                                    if index[0] == x - q and index[1] == y:
                                        index[2] = True
                    elif map1[x - q][y] >= 101:  # very inefficient implementation
                        for emp in listOfEmployees:
                            if emp.get_id() == map1[x - q][y]:
                                emp.safe = False
                    else:
                        map1[x - q][y] = Unsafe
                if x + q < MAPLENGTH:
                    if 1 <= map1[x + q][y] < 101:  # very inefficient implementation
                        for spot in listOfSafeSpots:
                            if spot.get_id() == map1[x + q][y]:
                                for index in spot.get_list():
                                    if index[0] == x + q and index[1] == y:
                                        index[2] = True
                    elif map1[x + q][y] >= 101:  # very inefficient implementation
                        for emp in listOfEmployees:
                            if emp.get_id() == map1[x + q][y]:
                                emp.safe = False
                    else:
                        map1[x + q][y] = Unsafe
            y = y + 1
            iteration = iteration + 1

            for row in range(MAPLENGTH):
                for col in range(MAPWIDTH):
                    pygame.draw.rect(DISPLAY, TileColor[map1[row][col]],
                                     (col * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
            pygame.display.update()

        pygame.draw.line(DISPLAY, BLUE,
                         (gl.get_col() * TILESIZE, gl.get_row() * TILESIZE + TILESIZE / 2),
                         (gl.get_col() * TILESIZE + WIDTH, gl.get_row() * TILESIZE + TILESIZE / 2))

    elif 135 <= gl.get_direction() <= 224:  # south
        x = gl.get_row() + 1
        y = gl.get_col()

        while x < MAPLENGTH:
            if 1 <= map1[x][y] <= 101:  # very inefficient implementation
                for spot in listOfSafeSpots:
                    if spot.get_id() == map1[x][y]:
                        for index in spot.get_list():
                            if index[0] == x and index[1] == y:
                                index[2] = True
            elif map1[x][y] >= 101:
                for emp in listOfEmployees:
                    if emp.id == map1[x][y]:
                        emp.safe = False
            else:
                map1[x][y] = Unsafe
            x = x + 1

        x = gl.get_row() + 1
        iteration = 1
        while x < MAPLENGTH:
            for q in range(1, iteration + 1):
                if y - q >= 0:
                    if 1 <= map1[x][y - q] < 101:  # very inefficient implementation
                        for spot in listOfSafeSpots:
                            if spot.get_id() == map1[x][y - q]:
                                for index in spot.get_list():
                                    if index[0] == x and index[1] == y - q:
                                        index[2] = True
                    elif map1[x][y - q] >= 101:
                        for emp in listOfEmployees:
                            if emp.id == map1[x][y - q]:
                                emp.safe = False
                    else:
                        map1[x][y - q] = Unsafe
                if y + q < MAPWIDTH:
                    if 1 <= map1[x][y + q] < 101:  # very inefficient implementation
                        for spot in listOfSafeSpots:
                            if spot.get_id() == map1[x][y + q]:
                                for index in spot.get_list():
                                    if index[0] == x and index[1] == y + q:
                                        index[2] = True
                    elif map1[x][y + q] >= 101:
                        for emp in listOfEmployees:
                            if emp.id == map1[x][y + q]:
                                emp.safe = False
                    else:
                        map1[x][y + q] = Unsafe
            x = x + 1
            iteration = iteration + 1

            for row in range(MAPLENGTH):
                for col in range(MAPWIDTH):
                    pygame.draw.rect(DISPLAY, TileColor[map1[row][col]],
                                     (col * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
            pygame.display.update()

        pygame.draw.line(DISPLAY, BLUE,
                         (gl.get_col() * TILESIZE + TILESIZE / 2, gl.get_row() * TILESIZE),
                         (gl.get_col() * TILESIZE + TILESIZE / 2, gl.get_row() * TILESIZE + HEIGHT))

    elif 225 <= gl.get_direction() <= 314:  # west
        x = gl.get_row()
        y = gl.get_col() - 1

        while y >= 0:
            if 1 <= map1[x][y] < 101:  # very inefficient implementation
                for spot in listOfSafeSpots:
                    if spot.get_id() == map1[x][y]:
                        for index in spot.get_list():
                            if index[0] == x and index[1] == y:
                                index[2] = True
            elif map1[x][y] >= 101:  # very inefficient implementation
                for emp in listOfEmployees:
                    if emp.get_id() == map1[x][y]:
                        emp.safe = False
            else:
                map1[x][y] = Unsafe
            y = y - 1

        y = gl.get_col() - 1
        iteration = 1
        while y >= 0:
            for q in range(1, iteration + 1):
                if x - q >= 0:
                    if 1 <= map1[x - q][y] < 101:  # very inefficient implementation
                        for spot in listOfSafeSpots:
                            if spot.get_id() == map1[x - q][y]:
                                for index in spot.get_list():
                                    if index[0] == x - q and index[1] == y:
                                        index[2] = True
                    elif map1[x - q][y] >= 101:  # very inefficient implementation
                        for emp in listOfEmployees:
                            if emp.get_id() == map1[x - q][y]:
                                emp.safe = False
                    else:
                        map1[x - q][y] = Unsafe
                if x + q < MAPLENGTH:
                    if 1 <= map1[x + q][y] < 101:  # very inefficient implementation
                        for spot in listOfSafeSpots:
                            if spot.get_id() == map1[x + q][y]:
                                for index in spot.get_list():
                                    if index[0] == x + q and index[1] == y:
                                        index[2] = True
                    elif map1[x + q][y] >= 101:  # very inefficient implementation
                        for emp in listOfEmployees:
                            if emp.get_id() == map1[x + q][y]:
                                emp.safe = False
                    else:
                        map1[x + q][y] = Unsafe
            y = y - 1
            iteration = iteration + 1

            for row in range(MAPLENGTH):
                for col in range(MAPWIDTH):
                    pygame.draw.rect(DISPLAY, TileColor[map1[row][col]],
                                     (col * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
            pygame.display.update()

        pygame.draw.line(DISPLAY, BLUE,
                         (gl.get_col() * TILESIZE, gl.get_row() * TILESIZE + TILESIZE / 2),
                         (gl.get_col() * TILESIZE - WIDTH, gl.get_row() * TILESIZE + TILESIZE / 2))

    pygame.display.update()

    for spot in listOfSafeSpots:
        spot.completelyUnsafe = True
        for index in spot.get_list():
            if not index[2]:
                spot.completelyUnsafe = False

    for spot in listOfSafeSpots:
        spot.completelySafe = True
        for index in spot.get_list():
            if index[2]:
                spot.completelySafe = False

    def check_ss_crosswind(emp, gl):
        for spot in listOfSafeSpots:
            if 67 <= gl.get_direction() <= 112 or 248 <= gl.get_direction() <= 292:  # east or west
                if gl.get_row() > emp.get_row():
                    if spot.locationCenter[0] < gl.get_row():
                        spot.isCrossWind = True
                elif gl.get_row() <= emp.get_row():
                    if spot.locationCenter[0] >= gl.get_row():
                        spot.isCrossWind = True
            elif 338 <= gl.get_direction() <= 359 or 0 <= gl.get_direction() <= 22 \
                    or 158 <= gl.get_direction() <= 202:  # north or south
                if gl.get_col() > emp.get_col():
                    if spot.locationCenter[1] < gl.get_col():
                        spot.isCrossWind = True
                elif gl.get_col() <= emp.get_col():
                    if spot.locationCenter[1] >= gl.get_col():
                        spot.isCrossWind = True

    # M A I N   A L G O R I T H M
    for emp in listOfEmployees:
        if not emp.is_safe():
            check_ss_crosswind(emp, gl)

            # if there are uncontaminated crosswind safe spots, send to nearest one
            closestLoc = -1
            minDist = sys.maxsize
            for spot in listOfSafeSpots:
                if spot.isCrossWind and spot.completelySafe:
                    if math.sqrt((spot.locationCenter[0] - emp.get_row()) ** 2 +
                                 (spot.locationCenter[1] - emp.get_col()) ** 2) < minDist:
                        closestLoc = spot
                        minDist = math.sqrt((spot.locationCenter[0] - emp.get_row()) ** 2 +
                                            (spot.locationCenter[1] - emp.get_col()) ** 2)

            if closestLoc != -1:
                pygame.draw.circle(DISPLAY, BLUE, (closestLoc.locationCenter[1] * TILESIZE,
                                                   closestLoc.locationCenter[0] * TILESIZE), 4 * TILESIZE)
                pygame.draw.line(DISPLAY, PURPLE, (emp.get_col() * TILESIZE, emp.get_row() * TILESIZE),
                                 (closestLoc.locationCenter[1] * TILESIZE, closestLoc.locationCenter[0] * TILESIZE))
                pygame.display.update()
                continue

            # if there are uncontaminated safe spots, send to nearest one
            closestLoc = -1
            minDist = sys.maxsize
            for spot in listOfSafeSpots:
                if spot.completelySafe:
                    if math.sqrt((spot.locationCenter[0] - emp.get_row()) ** 2 +
                                 (spot.locationCenter[1] - emp.get_col()) ** 2) < minDist:
                        closestLoc = spot
                        minDist = math.sqrt((spot.locationCenter[0] - emp.get_row()) ** 2 +
                                            (spot.locationCenter[1] - emp.get_col()) ** 2)

            if closestLoc != -1:
                pygame.draw.circle(DISPLAY, BLUE, (closestLoc.locationCenter[1] * TILESIZE,
                                                   closestLoc.locationCenter[0] * TILESIZE), 4 * TILESIZE)
                pygame.draw.line(DISPLAY, PURPLE, (emp.get_col() * TILESIZE, emp.get_row() * TILESIZE),
                                 (closestLoc.locationCenter[1] * TILESIZE, closestLoc.locationCenter[0] * TILESIZE))
                pygame.display.update()
                continue

            # if there are no completely safe but partly covered safespots, send to nearest one
            closestLoc = -1
            minDist = sys.maxsize
            for spot in listOfSafeSpots:
                if not spot.completelySafe and not spot.completelyUnsafe:
                    if math.sqrt((spot.locationCenter[0] - emp.get_row()) ** 2 +
                                 (spot.locationCenter[1] - emp.get_col()) ** 2) < minDist:
                        closestLoc = spot
                        minDist = math.sqrt((spot.locationCenter[0] - emp.get_row()) ** 2 +
                                            (spot.locationCenter[1] - emp.get_col()) ** 2)

            if closestLoc != -1:
                pygame.draw.circle(DISPLAY, BLUE, (closestLoc.locationCenter[1] * TILESIZE,
                                                   closestLoc.locationCenter[0] * TILESIZE), 4 * TILESIZE)
                pygame.draw.line(DISPLAY, PURPLE, (emp.get_col() * TILESIZE, emp.get_row() * TILESIZE),
                                 (closestLoc.locationCenter[1] * TILESIZE, closestLoc.locationCenter[0] * TILESIZE))
                pygame.display.update()
                continue

            # if there are no safe spots, send to the one farthest from gas leak
            farthestLoc = -1
            maxDist = 0
            for spot in listOfSafeSpots:
                if spot.completelyUnsafe:
                    if math.sqrt((spot.locationCenter[0] - emp.get_row()) ** 2 +
                                 (spot.locationCenter[1] - emp.get_col()) ** 2) > maxDist:
                        farthestLoc = spot
                        maxDist = math.sqrt((spot.locationCenter[0] - emp.get_row()) ** 2 +
                                            (spot.locationCenter[1] - emp.get_col()) ** 2)

            if farthestLoc != -1:
                pygame.draw.circle(DISPLAY, BLUE, (farthestLoc.locationCenter[1] * TILESIZE,
                                                   farthestLoc.locationCenter[0] * TILESIZE), 4 * TILESIZE)
                pygame.draw.line(DISPLAY, PURPLE, (emp.get_col() * TILESIZE, emp.get_row() * TILESIZE),
                                 (closestLoc.locationCenter[1] * TILESIZE, closestLoc.locationCenter[0] * TILESIZE))
                pygame.display.update()
                continue

    keepLooping = True
    while keepLooping:
        for event in pygame.event.get():
            # if you press the X in the top-right corner
            if event.type == pygame.QUIT:
                pygame.quit()
                keepLooping = False
                break
