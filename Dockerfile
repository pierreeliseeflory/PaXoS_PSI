FROM ubuntu:20.04

# Issues
# - each project installs its own requirements

ARG DEBIAN_FRONTEND=noninteractive

#################################################
# Install system dependencies.
#################################################

RUN apt-get -yqq update && apt-get install -yqq --no-install-recommends \
    ca-certificates \
    wget \
    build-essential \
    m4 \
    autoconf \
    automake \
    cmake \
    pkg-config \
    libtool \
    git \
    libssl-dev \
    libopenblas-dev \
    zlib1g-dev \
    liblog4cpp5-dev \
    python \
    && rm -rf /var/lib/apt/lists/*


# required by libscapi
ENV HOME=/root
WORKDIR ${HOME}

#################################################
# Install local dependencies.
#################################################

COPY thirdparty/ ${HOME}/thirdparty/
RUN cd thirdparty/linux \
    && bash get_gmp.sh \
    && bash get_gf2x.sh \
    && bash get_ntl.sh

#################################################
# Build libOTe.
#################################################

# TODO : turn into a submodule
RUN git clone --recursive https://github.com/osu-crypto/libOTe.git \
    && cd libOTe \
    && git checkout 8b4e2e23eab4e068fe0df6d609dd452236144bdf \
    && cd cryptoTools \
    && git checkout 3a71a8283c85ac417f2f841ba2357045d0efe0b4

COPY boost.patch libOTe/cryptoTools/thirdparty/linux/

RUN cd libOTe/cryptoTools/thirdparty/linux/ \
    # update Boost CDN && installation
    && git apply boost.patch \
    && bash boost.get \
    && bash miracl.get
RUN cd libOTe && cmake . && make

#################################################
# Build libSCAPI.
#################################################

RUN git clone https://github.com/cryptobiu/libscapi.git \
    && cd ${HOME}/libscapi \
    # Use the same commit as the PaXoS experiments.
    && git checkout 3505b6f4d9ee8382ac3ffe43bf0cef16e27add65
# Remove libscapi's packaged version of libOTe, and instead link in our version.
RUN rm -rf ${HOME}/libscapi/lib/libOTe \
    && ln -s ${HOME}/libOTe ${HOME}/libscapi/lib/libOTe
# Build the remaining libraries. (NTL is already built)
RUN cd ${HOME}/libscapi \
    && make compile-blake compile-otextension-bristol compile-kcp

RUN cd ${HOME}/libscapi \
    && rm makefile \
    && cmake . \
    && make scapi

#################################################
# Build linbox.
#################################################

RUN wget https://github.com/pierreeliseeflory/linbox/raw/master/linbox-auto-install.sh 
RUN bash linbox-auto-install.sh \
    --with-blas-libs="-lopenblas" \
    --make-flags=-j32 \
    --prefix=/usr/local

#################################################
# Build libxxhash.
#################################################

RUN git clone https://github.com/Cyan4973/xxHash.git
RUN cd xxHash \
    && mkdir build \
    && cd build \
    && cmake ../cmake_unofficial -DCMAKE_BUILD_TYPE=Release \
    && cmake --build . --target install

#################################################
# Compile PSI library.
#################################################

COPY frontend/ ${HOME}/frontend/
COPY libPSI/ ${HOME}/libPSI/
COPY CMakeLists.txt ${HOME}/
COPY cmake/ ${HOME}/cmake/


RUN cmake . && make -j32

# #################################################
# # Run PSI
# #################################################

COPY data/ /data/
COPY run.sh /
ENTRYPOINT [ "/run.sh" ]
