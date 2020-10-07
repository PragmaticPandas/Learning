/**
Subnetting version 1.0, created by Joshua Gomez
Input an IP Address and CIDR
Outputs solved IP address for all 7 subnetting attributes
**/
const cidr_db = {
        32:[[255,255,255,255],1,3],
        31:[[255,255,255,254],2,3],
        30:[[255,255,255,252],4,3],
        29:[[255,255,255,248],8,3],
        28:[[255,255,255,240],16,3],
        27:[[255,255,255,224],32,3],
        26:[[255,255,255,192],64,3],
        25:[[255,255,255,128],128,3],
        24:[[255,255,255,0],1,2],
        23:[[255,255,254,0],2,2],
        22:[[255,255,252,0],4,2],
        21:[[255,255,248,0],8,2],
        20:[[255,255,240,0],16,2],
        19:[[255,255,224,0],32,2],
        18:[[255,255,192,0],64,2],
        17:[[255,255,128,0],128,2],
        16:[[255,255,0,0],1,1],
        15:[[255,254,0,0],2,1],
        14:[[255,252,0,0],4,1],
        13:[[255,248,0,0],8,1],
        12:[[255,240,0,0],16,1],
        11:[[255,224,0,0],32,1],
        10:[[255,192,0,0],64,1],
        9:[[255,128,0,0],128,1],
        8:[[255,0,0,0],1,0],
        7:[[254,0,0,0],2,0],
        6:[[252,0,0,0],4,0],
        5:[[248,0,0,0],8,0],
        4:[[240,0,0,0],16,0],
        3:[[224,0,0,0],32,0],
        2:[[192,0,0,0],64,0],
        1:[[128,0,0,0],128,0],
        };

//There might be a way to skip declaring variables
//before entering the function
//use var before defining a variable
Network_ID = [0,0,0,0]
First_host = [0,0,0,0]
Last_Host = [0,0,0,0]
Broadcast = [0,0,0,0]
Next_Subnet = [0,0,0,0]
number_ip = 0
i = 0
Network_ID_31 = []

//should continue to ask for input until correct ip is given
// var s_ip = prompt("IP: ")
// var ip = s_ip.split('.').map(Number);
ip = [156,76,248,28]

//will continue to ask for input until correct cidr is given
while ("TRUE") {
	cidr = parseInt(prompt("CIDR: "))
	if (cidr in cidr_db) {
		alert(cidr)
		break
	}
	else {
		alert("That is not a valid CIDR")
	};
};

//output ip address, cidr, and subnet mask we're solving for
console.log(ip,"/",cidr);
console.log(cidr_db[cidr][0]);

function subnetSolver(array) {
	//solves for network id
	if (cidr == 32) {
		console.log("Used for single host address")
	}

};

subnetSolver(ip)


(255).toString(); // "255" (default is radix 10)
(255).toString(2); // "11111111" (radix 2, i.e. binary)
(255).toString(16); // "ff" (radix 16, i.e. hexadecimal)
