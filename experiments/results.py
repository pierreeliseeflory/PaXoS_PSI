
# ****** ATTENTION *****
# Always run the command with -r 0 first (this is the server) because we measure the time of the client, and we don't want the client to wait for the server, this adds time to the run
# **********************


# The versions are:
results = {}
# ECDH with 2 curves versions
results['ecdh-c0'] = {}
results['ecdh-c1'] = {}
results['kkrt'] = {}
results['spot-low'] = {}
results['spot-fast'] = {}
results['rrv1'] = {}
results['rrv2'] = {}
results['paxos-ours-sh'] = {}
results['paxos-ours-mal'] = {}
results['paxos-ni-sh'] = {}
results['paxos-ni-mal'] = {}

for c in ['ecdh-c0', 'ecdh-c1', 'kkrt', 'spot-low', 'spot-fast', 'rrv1', 'rrv2', 'paxos-ours-sh', 'paxos-ours-mal', 'paxos-ni-sh', 'paxos-ni-mal']:
	results[c]['lan'] = {}
	results[c]['wan1'] = {}
	results[c]['wan2'] = {}


# ECDH
# cd ~/Ni/SpOT-PSI
# server:
# ./bin/frontend.exe -r 0 -echd -c 0 -n 12 -ip 172.31.15.222:1212
# client:
# ./bin/frontend.exe -r 1 -echd -c 0 -n 12 -ip 172.31.15.222:1212
# parameters -c {0,1} -n {12,16,20}
# *****   -c 0  ******
results['ecdh-c0']['lan'][12] = 0.0
results['ecdh-c0']['lan'][16] = 0.0
results['ecdh-c0']['lan'][20] = 0.0
results['ecdh-c0']['wan1'][12] = 0.0
results['ecdh-c0']['wan1'][16] = 0.0
results['ecdh-c0']['wan1'][20] = 0.0
results['ecdh-c0']['wan2'][12] = 0.0
results['ecdh-c0']['wan2'][16] = 0.0
results['ecdh-c0']['wan2'][20] = 0.0
# *****   -c 1  ******
results['ecdh-c1']['lan'][12] = 0.0
results['ecdh-c1']['lan'][16] = 0.0
results['ecdh-c1']['lan'][20] = 0.0
results['ecdh-c1']['wan1'][12] = 0.0
results['ecdh-c1']['wan1'][16] = 0.0
results['ecdh-c1']['wan1'][20] = 0.0
results['ecdh-c1']['wan2'][12] = 0.0
results['ecdh-c1']['wan2'][16] = 0.0
results['ecdh-c1']['wan2'][20] = 0.0


# KKRT
# cd ~/BaRK-OPRF/Release
# server:
# ./bOPRFmain.exe -r 0  -ip 0.0.0.0:1212
# client:
# ./bOPRFmain.exe -r 1  -ip 172.31.15.222:1212
# no parameters
results['kkrt']['lan'][12] = 0.0
results['kkrt']['lan'][16] = 0.0
results['kkrt']['lan'][20] = 0.0
results['kkrt']['lan'][24] = 0.0
results['kkrt']['wan1'][12] = 0.0
results['kkrt']['wan1'][16] = 0.0
results['kkrt']['wan1'][20] = 0.0
results['kkrt']['wan1'][24] = 0.0
results['kkrt']['wan2'][12] = 0.0
results['kkrt']['wan2'][16] = 0.0
results['kkrt']['wan2'][20] = 0.0
results['kkrt']['wan2'][24] = 0.0


# SpOT
# cd ~/Ni/SpOT-PSI
# server:
# ./bin/frontend.exe -r 0 -n 12 -t 1 -p 1 -ip 172.31.15.222:1212
# client:
# ./bin/frontend.exe -r 1 -n 12 -t 1 -p 1 -ip 172.31.15.222:1212
# parameters: -p {0,1}
# if -p 1: -n {12,16,20}
# if -p 0: -n {12,16,20, 24}
results['spot-low']['lan'][12] = 0.0
results['spot-low']['lan'][16] = 0.0
results['spot-low']['lan'][20] = 0.0
results['spot-low']['wan1'][12] = 0.0
results['spot-low']['wan1'][16] = 0.0
results['spot-low']['wan1'][20] = 0.0
results['spot-low']['wan2'][12] = 0.0
results['spot-low']['wan2'][16] = 0.0
results['spot-low']['wan2'][20] = 0.0

results['spot-fast']['lan'][12] = 0.0
results['spot-fast']['lan'][16] = 0.0
results['spot-fast']['lan'][20] = 0.0
results['spot-fast']['lan'][24] = 0.0
results['spot-fast']['wan1'][12] = 0.0
results['spot-fast']['wan1'][16] = 0.0
results['spot-fast']['wan1'][20] = 0.0
results['spot-fast']['wan1'][24] = 0.0
results['spot-fast']['wan2'][12] = 0.0
results['spot-fast']['wan2'][16] = 0.0
results['spot-fast']['wan2'][20] = 0.0
results['spot-fast']['wan2'][24] = 0.0

# RR17b {rrv1,rrv2}
# cd ~/Ni/libPSI
# ***** NOTE ************************************
# * The IPs are hard coded in the source coded 	*
# *	 right now the server's IP encoded IPs 		*
# *	 172.31.10.226 								*
# *	 so either change it and re-compile 		*
# *	 or change only the client's location		*
# ***********************************************
# In RR - take run times from the server side.
# server:
# ./bin/frontend.exe -rr17b -r 0 -nn 20 -s 4
# client:
# ./bin/frontend.exe -rr17b -r 1 -nn 20 -s 4
# parameters: -nn {12,16,20,24}
results['rrv1']['lan'][12] = 0.0
results['rrv1']['lan'][16] = 0.0
results['rrv1']['lan'][20] = 0.0
results['rrv1']['lan'][24] = 0.0
results['rrv1']['wan1'][12] = 0.0
results['rrv1']['wan1'][16] = 0.0
results['rrv1']['wan1'][20] = 0.0
results['rrv1']['wan1'][24] = 0.0
results['rrv1']['wan2'][12] = 0.0
results['rrv1']['wan2'][16] = 0.0
results['rrv1']['wan2'][20] = 0.0
results['rrv1']['wan2'][24] = 0.0
# server:
# ./bin/frontend.exe -rr17b-sm -r 0 -nn 16 -s 4 -b 64
# client:
# ./bin/frontend.exe -rr17b-sm -r 1 -nn 16 -s 4 -b 64
# parameters: -nn {12,16}
results['rrv2']['lan'][12] = 0.0
results['rrv2']['lan'][16] = 0.0
results['rrv2']['wan1'][12] = 0.0
results['rrv2']['wan1'][16] = 0.0
results['rrv2']['wan2'][12] = 0.0
results['rrv2']['wan2'][16] = 0.0


# Paxos ours semi-honest
# cd ~/PaXoS_PSI
# NOTE: always set -malicious 0 (because -malicious 1 has a bug)
# server:
# ./bin/frontend.exe -partyID 1 -hashSize x  -fieldSize y -partiesFile bin/Parties.txt -reportStatistics 0 -internalIterationsNumber 1 -malicious 0
# client:
# ./bin/frontend.exe -partyID 0 -hashSize x  -fieldSize y -partiesFile bin/Parties.txt -reportStatistics 0 -internalIterationsNumber 1 -malicious 0
#
# parameters: when -hashSize is x[i] then -fieldSize is y[i]
# x = [ 4096, 65536, 1048576, 16777216 ], y = [ 72, 72, 84, 90 ]
#
results['paxos-ours-sh']['lan'][12] = 0.0
results['paxos-ours-sh']['lan'][16] = 0.0
results['paxos-ours-sh']['lan'][20] = 0.0
results['paxos-ours-sh']['lan'][24] = 0.0
results['paxos-ours-sh']['wan1'][12] = 0.0
results['paxos-ours-sh']['wan1'][16] = 0.0
results['paxos-ours-sh']['wan1'][20] = 0.0
results['paxos-ours-sh']['wan1'][24] = 0.0
results['paxos-ours-sh']['wan2'][12] = 0.0
results['paxos-ours-sh']['wan2'][16] = 0.0
results['paxos-ours-sh']['wan2'][20] = 0.0
results['paxos-ours-sh']['wan2'][24] = 0.0

# Paxos ours malicious
# same commands as semi-honest, but with the following parameters
#
# parameters: when -hashSize is x[i] then -fieldSize is y[i]
# x = [ 4096, 65536, 1048576, 16777216 ], y = [ 144, 138, 138, 132 ]
#
results['paxos-ours-mal']['lan'][12] = 0.0
results['paxos-ours-mal']['lan'][16] = 0.0
results['paxos-ours-mal']['lan'][20] = 0.0
results['paxos-ours-mal']['lan'][24] = 0.0
results['paxos-ours-mal']['wan1'][12] = 0.0
results['paxos-ours-mal']['wan1'][16] = 0.0
results['paxos-ours-mal']['wan1'][20] = 0.0
results['paxos-ours-mal']['wan1'][24] = 0.0
results['paxos-ours-mal']['wan2'][12] = 0.0
results['paxos-ours-mal']['wan2'][16] = 0.0
results['paxos-ours-mal']['wan2'][20] = 0.0
results['paxos-ours-mal']['wan2'][24] = 0.0

