#!/usr/bin/env bash

touch /log

/root/bin/frontend -partyID 0 -hashSize 128 -fieldSize 90 -partiesFile /data/config.txt -malicious 0 reportStatistics 0 -internalIterationsNumber 1 &>/log &

echo
echo "# Sender"
echo

/root/bin/frontend -partyID 1 -hashSize 128 -fieldSize 90 -partiesFile /data/config.txt -malicious 0 reportStatistics 0 -internalIterationsNumber 1

echo
echo "# Receiver"
echo

cat /log

exit 0
