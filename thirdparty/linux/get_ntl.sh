#!/usr/bin/env sh

NTL_VERSION="11.4.3"

wget https://libntl.org/ntl-${NTL_VERSION}.tar.gz
tar -zxvf ntl-${NTL_VERSION}.tar.gz
mv ntl-${NTL_VERSION} ntl
rm ntl-${NTL_VERSION}.tar.gz

cd ntl/src || exit 1
./configure NTL_GF2X_LIB=on NTL_THREAD_BOOST=on NTL_FFT_LAZYMUL=on NTL_FFT_BIGTAB=on SHARED=on
make && make check && make install && ldconfig
