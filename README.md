# PaXoS PSI

This is the implementation of the EUROCRYPT 2020 paper: [PSI from PaXoS: Fast, Malicious Private Set Intersection](https://eprint.iacr.org/2020/193).

## Installation

### Container

#### Requirements

- [docker](https://www.docker.com/)

#### Build

```shell
docker build -t paxos -f Dockerfile .
```

#### Run

```shell
docker run paxos
```

## Configuration

See the example config file [here](data/config.txt).

Syntax:

```shell
# comments
parameter = value
```

## Usage

Main executable : `frontend.exe`

```shell
frontend.exe -partyID 0 -hashSize 1000000 -fieldSize 132 -partiesFile config.txt -reportStatistics 0 -internalIterationsNumber 1
```

### Parameters

- -partyID
  - 0 $\to$ receiver
  - 1 $\to$ sender
- -hashSize
- -fieldSize
  - 65
  - 72
  - 84
  - 90
  - 132
  - 138
  - 144
  - 150
  - 156
  - 162
  - 168
  - 174
  - 210
  - 217
  - 231
  - 238
- -partiesFile
  - configuration file (for networking)
- -reportStatistics
- -internalIterationsNumber

## References

Produced from [https://github.com/schoppmp/PaXoS_PSI/tree/docker](https://github.com/schoppmp/PaXoS_PSI/tree/docker) and [https://github.com/cryptobiu/PaXoS_PSI](https://github.com/cryptobiu/PaXoS_PSI).