##############################################
##                 Link NTL                  #
##############################################

find_package(NTL REQUIRED)

message(STATUS "NTL  ${NTL_LIB}")
message(STATUS "NTL  ${NTL_INCLUDE_DIR}")
message(STATUS "NTL  ${NTL_LIB_DIR}")

##############################################
##                 Link GMP                  #
##############################################

find_package(GMP REQUIRED)

message(STATUS "GMP  ${GMP_LIB}")
message(STATUS "GMP  ${GMP_INCLUDE_DIR}")
message(STATUS "GMP  ${GMP_LIB_DIR}")

##############################################
##                 Link GF2X                 #
##############################################

find_package(GF2X REQUIRED)

message(STATUS "GF2X  ${GF2X_LIB}")
message(STATUS "GF2X  ${GF2X_INCLUDE_DIR}")
message(STATUS "GF2X  ${GF2X_LIB_DIR}")

#############################################
#                 Link Boost                #
#############################################
set(Boost_USE_STATIC_LIBS        ON) # only find static libs
set(Boost_USE_STATIC_RUNTIME     ON)
set(Boost_USE_MULTITHREADED      ON)

find_package(Boost COMPONENTS system thread)

if(Boost_FOUND)
  set(Boost_LIB ${Boost_LIBRARIES})
else()
   message(FATAL_ERROR "Failed to find boost at " ${BOOST_ROOT} ". Need system thread")
endif()
 
#############################################
#                 Link Miracl               #
#############################################

find_library(
  MIRACL_LIB 
  NAMES miracl  
  HINTS "${Miracl_Dirs}/miracl/source/")
  
# if we cant fint it, throw an error
if(NOT MIRACL_LIB)
  message(FATAL_ERROR "Failed to find miracl at " ${Miracl_Dirs})
else()
  message(STATUS "Found Miracl at ${MIRACL_LIB}")
endif()

#############################################
#                 Link libOTe               #
#############################################

find_library(
    libOTe_LIB
    NAMES libOTe
    HINTS "${libOTe_Dirs}/lib/")
	
find_library(
    cryptoTools_LIB
    NAMES cryptoTools
    HINTS "${libOTe_Dirs}/lib/")
	
#############################################
#              Build libPSI                #
#############################################

file(GLOB_RECURSE SRCS *.cpp)

add_library(libPSI ${SRCS})

target_include_directories(libPSI PUBLIC ${Boost_INCLUDE_DIR}) 
target_include_directories(libPSI PUBLIC ${NTL_INCLUDE_DIR}) 
target_include_directories(libPSI PUBLIC ${GMP_INCLUDE_DIR})
target_include_directories(libPSI PUBLIC ${GF2X_INCLUDE_DIR})
target_include_directories(libPSI PUBLIC ${CMAKE_SOURCE_DIR}/libPSI) 

target_link_libraries(libPSI ${libOTe_LIB}  ${cryptoTools_LIB} ${MIRACL_LIB} ${NTL_LIB} ${GMP_LIB} ${GF2X_LIB} ${Boost_LIB} )
