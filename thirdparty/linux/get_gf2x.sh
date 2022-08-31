#!/usr/bin/env sh

GF2X_VERSION="1.2"

wget https://gitlab.inria.fr/gf2x/gf2x/uploads/46a3851a4aa6888e6a6a7ce3de33f0f4/gf2x-${GF2X_VERSION}.tar.gz
tar -zxvf gf2x-${GF2X_VERSION}.tar.gz
mv gf2x-${GF2X_VERSION} gf2x
rm gf2x-${GF2X_VERSION}.tar.gz

cd gf2x/ || 1
./configure ABI=64 CFLAGS="-m64 -O2"
make && make check && make install && ldconfig
