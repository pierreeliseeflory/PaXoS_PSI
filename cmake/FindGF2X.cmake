find_path(GF2X_INCLUDE_DIR
          NAMES gf2x.h
          HINTS ENV GF2X_INC_DIR
                ENV GF2X_DIR
          PATH_SUFFIXES include
          DOC "The directory containing the GF2X include files"
          )

find_library(GF2X_LIB
              NAMES gf2x
              HINTS ENV GF2X_LIB_DIR
                    ENV GF2X_DIR
              PATH_SUFFIXES lib
              DOC "Path to the GF2X library"
            )

get_filename_component(GF2X_LIB_DIR ${GF2X_LIB} PATH CACHE )

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args( GF2X
                                    DEFAULT_MSG
                                    GF2X_LIB
                                    GF2X_INCLUDE_DIR )