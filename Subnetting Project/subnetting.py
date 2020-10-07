"""
Subnetting version 1.2, created by Joshua Gomez

Changelog:
1.1, there was no way to check if the IP address
that was input by the user was correct
    
1.0, program without attribute labels and number of 
usable ip addresses was pulled from the dictionary
instead of being calculated manually

Input an IP Address and CIDR
Outputs solved IP address for all 7 subnetting attributes
"""

cidr_db = {
        32:([255,255,255,255],1,3),
        31:([255,255,255,254],2,3),
        30:([255,255,255,252],4,3),
        29:([255,255,255,248],8,3),
        28:([255,255,255,240],16,3),
        27:([255,255,255,224],32,3),
        26:([255,255,255,192],64,3),
        25:([255,255,255,128],128,3),
        24:([255,255,255,0],1,2),
        23:([255,255,254,0],2,2),
        22:([255,255,252,0],4,2),
        21:([255,255,248,0],8,2),
        20:([255,255,240,0],16,2),
        19:([255,255,224,0],32,2),
        18:([255,255,192,0],64,2),
        17:([255,255,128,0],128,2),
        16:([255,255,0,0],1,1),
        15:([255,254,0,0],2,1),
        14:([255,252,0,0],4,1),
        13:([255,248,0,0],8,1),
        12:([255,240,0,0],16,1),
        11:([255,224,0,0],32,1),
        10:([255,192,0,0],64,1),
        9:([255,128,0,0],128,1),
        8:([255,0,0,0],1,0),
        7:([254,0,0,0],2,0),
        6:([252,0,0,0],4,0),
        5:([248,0,0,0],8,0),
        4:([240,0,0,0],16,0),
        3:([224,0,0,0],32,0),
        2:([192,0,0,0],64,0),
        1:([128,0,0,0],128,0),
        }

#will continue to ask for input until correct ip is given
ip = [256,256,256,256]

while ip[0] > 255 or ip[1] > 255 or ip[2] > 255 or ip[3] > 255: 
    s_ip = input("Please enter a valid IP address: ")
    ip = [int(octet) for octet in s_ip.split('.')]

# will continue to ask for input until correct cidr is given
while True:
    cidr = int(input("CIDR: "))
    if cidr in cidr_db:
        break
    else:
        print("That is not a valid CIDR")  

#output ip address, cidr, and subnet mask we're solving for
print("Address to solve for:",ip,"/",cidr, sep='')
print("CIDR Subnet Mask:",cidr_db[cidr][0])

#function that solves subnets
def subnet_solver(array):
    Network_ID = [0,0,0,0]
    First_Host = [0,0,0,0]
    Last_Host = [0,0,0,0]
    Broadcast = [0,0,0,0]
    Next_Subnet = [0,0,0,0]
    i = 0
    Network_ID_31 = []

#solves for network ID
    if cidr == 32:
        print("Used for single host address")
    else:
        while i <= ip[cidr_db[cidr][2]]:
            i = i + cidr_db[cidr][1]
            index = cidr_db[cidr][2]
            Network_ID[index] = i - cidr_db[cidr][1]
            for octet in Network_ID[index:0:-1]:
                index = index - 1
                Network_ID[index] = ip[index]
        print("Network ID:",Network_ID)
#/31 cidr exception            
        if cidr == 31:
            Network_ID_31 = Network_ID.copy()
            Network_ID_31[3] += 1
            print(Network_ID_31)
            print("/31 is peer to peer")
#solves for first host
    index = cidr_db[cidr][2]
    First_Host = Network_ID.copy()
    First_Host[3] += 1
    print("First Host:",First_Host)
#solves for next subnet
    Next_Subnet = Network_ID.copy()
    Next_Subnet[index] = i
    if Next_Subnet[index] == 256:
        Next_Subnet[index] = 0
        index = index - 1
        Next_Subnet[index] = Next_Subnet[index] + 1                    
#solves for broadcast
    Broadcast = Next_Subnet.copy()
    Broadcast[index] = Broadcast[index] - 1
    for octet in Broadcast[index:3:1]:
        index = index + 1
        Broadcast[index] = 255        
#solves for last host
    Last_Host = Broadcast.copy()
    Last_Host[3] = Last_Host[3] - 1
    
#/1 cidr exception
    if cidr == 1:
        if Network_ID[0] == 128:
            Last_Host = [255,255,255,254]
            Broadcast = [255,255,255,255]
            Next_Subnet = [0,0,0,0]
            print("Last Host",Last_Host)
            print("Broadcast:",Broadcast)
            print("Exceeded available range of IP addresses")
            print("Next Subnet",Next_Subnet)   
#Printing next three attributes            
    if Network_ID[0] == 0:
        Last_Host = [127,255,255,254]
        Broadcast = [127,255,255,255]
        Next_Subnet = [128,0,0,0]
        print("Last Host",Last_Host)
        print("Broadcast:",Broadcast)
        print("Next Subnet",Next_Subnet)            
    else:        
        print("Last Host",Last_Host)
        print("Broadcast:",Broadcast)
        print("Next Subnet",Next_Subnet)            
#number of usable ip addresses   
    usable_ips_list = []
    power = 0
    for octet in cidr_db[cidr][0]:
        usable_ips_list += '{0:08b}'.format(octet)
    for octet in usable_ips_list:
        if octet == '0':
            power += 1
    
    usable_ips = (2 ** power) - 2
    print("Number of usable addresses:",usable_ips)

#calling the sfunction
#solved values are output in a list format
subnet_solver(ip)
