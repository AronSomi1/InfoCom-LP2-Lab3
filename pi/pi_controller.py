import math
import requests
import argparse

def travel(start,stop): # räknar ut förflyttningar
    x1 = start[0]
    y1 = start[1]
    x2 = stop[0]
    y2 = stop[1]

    dx = abs(x1-x2)
    dy = abs(y1-y2)
    d = math.sqrt(dx*dx + dy*dy)
    steps = d/0.0001
    dxR = x1-x2
    dyR = y1 -y2
    steps = int(steps)
    print(steps)
    for i in range(steps):
        setpos(x1 + i*(dxR/steps), y1 + i*(dyR/steps))



def setpos(x,y): # ändrar positionen 
    print("setpos", x, y)
    SERVER_URL = "http://127.0.0.1:5001/drone"

    with requests.Session() as session:
            drone_location = {'longitude': x,
                              'latitude': y
                        }
            resp = session.post(SERVER_URL, json=drone_location)


def route_planned(current_coords,destination, arrived):

    list_current_coords = list(current_coords)
    list_destination = list(destination)

    if abs(list_current_coords[0]-list_destination[0]) > abs(list_current_coords[1]-list_destination[1]):
        #ta ett steg i longitude riktning
        print("Steg i long riktning")
        if list_current_coords[0]-list_destination[0] >= 0:
            list_current_coords[0] = list_current_coords[0] - distance_per_hop()
            print("Steg i long riktning -")
        else: 
            list_current_coords[0] = list_current_coords[0] + distance_per_hop()
            print("Steg i long riktning +")

    else: #ta ett steg i lat led
        print("Ta ett steg i lat riktning")
        if list_current_coords[1]-list_destination[1] > 0:
            list_current_coords[1] = list_current_coords[1] - distance_per_hop()
            print("Steg i lat riktning -")
        else:
            list_current_coords[1] = list_current_coords[1] - distance_per_hop()
            print("Steg i lat riktning +")
    
    if abs(list_current_coords[0]-list_destination[0]) <= distance_per_hop() and abs(list_current_coords[1]-list_destination[1]) <= distance_per_hop() :
        print("Vi är framme")
        arrived = True

    current_coords = tuple(list_current_coords)
    print("Nuvarande koordinater", current_coords)
    print(arrived)

    return(current_coords,arrived)


   
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"

    parser = argparse.ArgumentParser()
    parser.add_argument("--clong", help='current longitude of drone location' ,type=float)
    parser.add_argument("--clat", help='current latitude of drone location',type=float)
    parser.add_argument("--flong", help='longitude of input [from address]',type=float)
    parser.add_argument("--flat", help='latitude of input [from address]' ,type=float)
    parser.add_argument("--tlong", help ='longitude of input [to address]' ,type=float)
    parser.add_argument("--tlat", help ='latitude of input [to address]' ,type=float)
    args = parser.parse_args()

    current_coords = (args.clong, args.clat)
    from_coords = (args.flong, args.flat)
    to_coords = (args.tlong, args.tlat)

    travel(current_coords, from_coords)
    travel(from_coords, to_coords)
