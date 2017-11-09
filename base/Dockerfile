FROM ubuntu

RUN apt-get -y update && apt-get -y upgrade && apt-get -y dist-upgrade && apt-get install -y \
    git \
    scons \
    ssh \
    libcurl4-openssl-dev \
    uuid-dev \
    autoconf \
    autotools-dev \
    make \
    cmake \
    build-essential \
    valgrind \
    doxygen \
    libboost-all-dev \
    libsqlite3-dev \
    libtool \
    libglib2.0-dev \
    libncurses5-dev \
    libpcap-dev \
    curl \
    libicu-dev \
    libexpat1-dev \
    default-jdk \
    unzip \
    wget \
    vim \
    htop \
    && rm -rf /var/lib/apt/lists/*

# Optional dependencies for future work
# clang \
# apt-utils \
# bzip2 \
# libbz2-dev \
# binutils \
# gettext \
# zlib1g-dev \
# file \
# libxml2 \
# qtbase5-dev \
# qt5-default \
# gcc-multilib \
# g++-multilib \
# lib32z1 \

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

RUN mkdir -p /home/iot/
WORKDIR /home/iot/

#ENV PREFIX /home/iot/out

#RUN git clone https://github.com/iotivity/iotivity.git \
RUN git clone -b 1.3-rel https://github.com/iotivity/iotivity.git \
&& cd iotivity/ \
# TODO: && git apply --check --apply ../samples.patch \
&& git clone https://github.com/01org/tinycbor.git extlibs/tinycbor/tinycbor -b v0.4.1 \
&& git clone https://github.com/ARMmbed/mbedtls.git extlibs/mbedtls/mbedtls -b mbedtls-2.4.2 \
&& scons -j4 TARGET_TRANSPORT=IP BUILD_JAVA=1 LOGGING=0 LOG_LEVEL=INFO
# TODO: Build simulator and organize generated files into /home/iot/simulator
#&& scons -j 4 TARGET_TRANSPORT=IP BUILD_JAVA=1 LOGGING=1 LOG_LEVEL=INFO --prefix=$PREFIX
#&& scons -j 4 TARGET_TRANSPORT=IP BUILD_JAVA=1 LOGGING=1 LOG_LEVEL=INFO install --prefix=$PREFIX

ENV LD_LIBRARY_PATH /home/iot/iotivity/out/linux/x86_64/release
VOLUME /home/iot/iotivity/out/linux/x86_64/release

# TODO: RUN \cp -rf *.dat $LD_LIBRARY_PATH/resource/examples
