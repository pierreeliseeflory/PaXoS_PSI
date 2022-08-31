#!/usr/bin/env sh

GMP_VERSION="6.2.0"

wget https://gmplib.org/download/gmp/gmp-${GMP_VERSION}.tar.bz2

tar -jxvf gmp-${GMP_VERSION}.tar.bz2
mv gmp-${GMP_VERSION} gmp
rm gmp-${GMP_VERSION}.tar.bz2

cd gmp/ || exit 1
./configure --enable-cxx
make && make check && make install
