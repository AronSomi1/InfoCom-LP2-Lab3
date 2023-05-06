import math
import requests
import argparse
import time

""" def travel(start,stop): # räknar ut förflyttningar
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
        time.sleep(0.1)

 """

""" def route_planned(current_coords,destination, arrived):

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

    return(current_coords,arrived) """

#This sendas the updatad positions to somewheren have't ofigure this out! It sends to database.py, I think because that is running on port 5001
def setpos(x,y): # ändrar positionen 
    print("setpos", x, y)
    SERVER_URL = "http://127.0.0.1:5001/drone"

    with requests.Session() as session:
            drone_location = {'longitude': x,
                              'latitude': y
                        }
            resp = session.post(SERVER_URL, json=drone_location)

#Updates the drones coordinates
def moveDrone(src, d_long, d_la):
    x, y = src
    x = x + d_long
    y = y + d_la
    return (x, y)

def getMovement(src, dst): #anledningen för detta är att drönaren ska komma fram samtidigt i x och y led. 
    speed = 0.00003   #default är 0.00001
    dst_x, dst_y = dst
    x, y = src
    direction = math.sqrt((dst_x - x)**2 + (dst_y - y)**2)
    longitude_move = speed * ((dst_x - x) / direction)
    latitude_move = speed * ((dst_y - y) / direction)
    return longitude_move, latitude_move 
    
def getTime(src, dst, time_sleep):  
    speed = 0.00003
    dst_x, dst_y = dst
    x, y = src
    direction = math.sqrt((dst_x - x)**2 + (dst_y - y)**2)
    #print('Distance' + str(direction))

    longitude_move = abs(speed * ((dst_x - x) / direction))
    #print('Longitude move' + str(longitude_move))

    amout_of_steps = abs(dst_x-x)/longitude_move
    print('Amount of steps' + str(amout_of_steps))
    total_time = amout_of_steps*time_sleep
   # print('mellan tid' + str(total_time))
    return total_time
    
    #This function moves the drone from point current coord, to from_cords and then to to_coords
def run(current_coord, from_coords , to_coords):
    drone_coords=current_coord
    d_long, d_la = getMovement(drone_coords, from_coords)
    
    while ((from_coords[0] - drone_coords[0])**2 + (from_coords[1] - drone_coords[1])**2)*10**6 > 0.0002:
        drone_coords = moveDrone(drone_coords, d_long, d_la)
        setpos(drone_coords[0],drone_coords[1])
        time.sleep(0.05)
        
    d_long, d_la = getMovement(drone_coords, to_coords)
    
    while ((to_coords[0] - drone_coords[0])**2 + (to_coords[1] - drone_coords[1])**2)*10**6 > 0.0002:
        drone_coords = moveDrone(drone_coords, d_long, d_la)
        setpos(drone_coords[0],drone_coords[1])
        time.sleep(0.05)


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

    total_time = getTime(current_coords, from_coords, 0.5) + getTime(from_coords, to_coords, 0.5) # räknar ut totalhastighet i s


    run(current_coords, from_coords, to_coords)
    
    #travel(current_coords, from_coords)
    #travel(from_coords, to_coords)
