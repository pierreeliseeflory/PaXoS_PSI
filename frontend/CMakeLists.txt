#############################################
#               Build frontend.exe           #
#############################################

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O2 -g -ggdb -rdynamic")
set(CMAKE_CXX_FLAGS_DEBUG  "-O0 -g3 -ggdb -rdynamic")

file(GLOB_RECURSE SRC_FRONTEND ${CMAKE_SOURCE_DIR}/frontend/*.cpp)
include_directories(${CMAKE_SOURCE_DIR}/frontend/ $ENV{HOME} ${CMAKE_SOURCE_DIR}/libOTe
${CMAKE_SOURCE_DIR}/libOTe/cryptoTools/cryptoTools ${CMAKE_SOURCE_DIR}/libOTe/cryptoTools/cryptoTools/Crypto)
add_executable(frontend ${SRC_FRONTEND})


#############################################
#                Link libscapi             #
#############################################

link_directories($ENV{HOME}/libscapi/install/lib)

#############################################
#                 Link xxHash               #
#############################################

find_package(xxHash 0.7 CONFIG REQUIRED)

#############################################
#                 Link libOTe               #
#############################################

find_library(
    libOTe_Tests_LIB
    NAMES libOTe_Tests
    HINTS "${libOTe_Dirs}/lib/")

find_library(
    cryptoTools_Tests_LIB
    NAMES tests_cryptoTools
    HINTS "${libOTe_Dirs}/lib/")

target_link_libraries(frontend PRIVATE libPSI ${Boost_LIBRARIES} xxHash::xxhash givaro blas gomp linbox ntl gmp $ENV{HOME}/libscapi/libscapi.a crypto)
