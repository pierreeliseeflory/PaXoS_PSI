find_path(NTL_INCLUDE_DIR
          NAMES NTL/ZZ.h
          HINTS ENV NTL_INC_DIR
                ENV NTL_DIR
          PATH_SUFFIXES include
          DOC "The directory containing the NTL include files"
          )

find_library(NTL_LIB
              NAMES ntl
              HINTS ENV NTL_LIB_DIR
                    ENV NTL_DIR
              PATH_SUFFIXES lib
              DOC "Path to the NTL library"
            )

get_filename_component(NTL_LIB_DIR ${NTL_LIB} PATH CACHE )

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args( NTL
                                    DEFAULT_MSG
                                    NTL_LIB
                                    NTL_INCLUDE_DIR )