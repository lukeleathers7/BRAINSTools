# most of this file is copied and modified from the itk_common.cmake file
# found on the dashboard branch of ITK
# as well as the vxl_common.cmake file found on the dashboard branch of vxl

#=============================================================================
# Copyright 2010-2013 Kitware, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#=============================================================================
# BRAINSTools Common Dashboard Script
#
# This script is shared among most BRAINSTools dashboard client machines.
# It contains basic dashboard driver code common to all clients.
#
# Put this script in a directory such as "~/Dashboards/Scripts" or
# "c:/Dashboards/Scripts".  Create a file next to this script, say
# 'my_dashboard.cmake', with code of the following form:
#
#   # Client maintainer: someone@users.sourceforge.net
#   set(CTEST_SITE "machine.site")
#   set(CTEST_BUILD_NAME "Platform-Compiler")
#   set(CTEST_BUILD_CONFIGURATION Debug)
#   set(CTEST_CMAKE_GENERATOR "Unix Makefiles")
#   include(${CTEST_SCRIPT_DIRECTORY}/brainstools_common.cmake)
#
# Then run a scheduled task (cron job) with a command line such as
#
#   ctest -S ~/Dashboards/Scripts/my_dashboard.cmake -V
#
# By default the source and build trees will be placed in the path
# "../My_Tests/" relative to your script location.
#
# The following variables may be set before including this script
# to configure it:
#
#   dashboard_model       = Nightly | Experimental | Continuous
#   dashboard_root_name   = Change name of "My_Tests" directory
#   dashboard_source_name = Name of source directory (BRAINSTools)
#   
#   dashboard_cache       = Initial CMakeCache.txt file content
#   dashboard_do_coverage = True to enable coverage (ex: gcov)
#   dashboard_do_memcheck = True to enable memcheck (ex: valgrind)
#   CTEST_GIT_COMMAND     = path to git command-line client
#   CTEST_BUILD_FLAGS     = build tool arguments (ex: -j2)
#   CTEST_DASHBOARD_ROOT  = Where to put source and build trees
#   CTEST_TEST_TIMEOUT    = Per-test timeout length
#   CTEST_TEST_ARGS       = ctest_test args (ex: PARALLEL_LEVEL 4)
#   CMAKE_MAKE_PROGRAM    = Path to "make" tool to use
#
# Options to configure Git:
#   dashboard_git_url      = Custom git clone url
#   dashboard_git_branch   = Custom remote branch to track
#   dashboard_git_crlf     = Value of core.autocrlf for repository
#
# For Makefile generators the script may be executed from an
# environment already configured to use the desired compilers.
# Alternatively the environment may be set at the top of the script:
#
#   set(ENV{CC}  /path/to/cc)   # C compiler
#   set(ENV{CXX} /path/to/cxx)  # C++ compiler
#   set(ENV{LD_LIBRARY_PATH} /path/to/vendor/lib) # (if necessary)

cmake_minimum_required(VERSION 2.8.2 FATAL_ERROR) # 2.8.[01] will NOT work!

set(CTEST_PROJECT_NAME BRAINSTools)

# Set a default host name
if(NOT DEFINED CTEST_SITE )
 set(CTEST_SITE $ENV{HOSTNAME} )
endif()
message("HOSTNAME is ${HOSTNAME}" )
if(NOT DEFINED CTEST_SITE)
  message("ERROR:  Could not get hostname or username from environment setting host name to machine.site" )
  message(FATAL_ERROR "Please reconfigure the dashboard script to set the hostname manually")
endif()

# Select the top dashboard directory.
if(NOT DEFINED dashboard_root_name)
  set(dashboard_root_name "My_Tests")
endif()
if(NOT DEFINED CTEST_DASHBOARD_ROOT)
  get_filename_component(CTEST_DASHBOARD_ROOT "${CTEST_SCRIPT_DIRECTORY}/../${dashboard_root_name}" ABSOLUTE)
endif()

# Select the model (Nightly, Experimental, Continuous).
if(NOT DEFINED dashboard_model)
  set(dashboard_model Nightly)
endif()
if(NOT "${dashboard_model}" MATCHES "^(Nightly|Experimental|Continuous)$")
  message(FATAL_ERROR "dashboard_model must be Nightly, Experimental, or Continuous")
endif()

# Default to a Debug build.
# CMAKE_BUILD_TYPE takes priority as it is the variable passed to the cache
if(NOT DEFINED CMAKE_BUILD_TYPE)
  if(NOT DEFINED CTEST_BUILD_CONFIGURATION)
    set(CTEST_BUILD_CONFIGURATION Debug)
  endif()
  set(CMAKE_BUILD_TYPE ${CTEST_BUILD_CONFIGURATION})
else()
  if(DEFINED CTEST_BUILD_CONFIGURATION)
    message(WARNING "Both CTEST_BUILD_CONFIGURATION and CMAKE_BUILD_TYPE are set.  "
                    "Using value of CMAKE_BUILD_TYPE:${CMAKE_BUILD_TYPE} for both variables")
  endif()
  set(CTEST_BUILD_CONFIGURATION ${CMAKE_BUILD_TYPE})
endif()

# Setup compiler flags for code coverage
if(dashboard_do_coverage)
  message("setting up code coverage")
  if(NOT ${CMAKE_BUILD_TYPE} MATCHES "Debug")
    message(WARNING "Coverage is only available when building the \"Debug\" Configuration")
    message(WARNING "Setting CMAKE_BUILD_TYPE to \"Debug\"")
    set(CMAKE_BUILD_TYPE Debug)
    set(CTEST_BUILD_CONFIGURATION Debug)
  endif()
  set(COVERAGE_FLAGS "-fprofile-arcs -ftest-coverage")
  set(COVERAGE_DEBUG_FLAGS "-g -O0")
  set(COVERAGE_VARS CMAKE_CXX_FLAGS CMAKE_C_FLAGS )
  foreach(COVERAGE_VAR ${COVERAGE_VARS})
    set(${COVERAGE_VAR} "${${COVERAGE_VAR}} ${COVERAGE_DEBUG_FLAGS} ${COVERAGE_FLAGS}")
  endforeach()
  set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${COVERAGE_FLAGS}")
  set(COVERAGE_VARS ${COVERAGE_VARS} CMAKE_EXE_LINKER_FLAGS)
endif()

# NOTE: I need to figure out what launchers are
# Choose CTest reporting mode.
if(NOT "${CTEST_CMAKE_GENERATOR}" MATCHES "Make")
  # Launchers work only with Makefile generators.
  set(CTEST_USE_LAUNCHERS 0)
elseif(NOT DEFINED CTEST_USE_LAUNCHERS)
  set(CTEST_USE_LAUNCHERS 1)
endif()

# Configure testing.
if(NOT CTEST_TEST_TIMEOUT)
  set(CTEST_TEST_TIMEOUT 1500)
endif()



# Select Git source to use.
if(NOT DEFINED dashboard_git_url)
  set(dashboard_git_url "https://github.com/BRAINSIa/BRAINSTools.git")
endif()
if(NOT DEFINED dashboard_git_branch)
  set(dashboard_git_branch master)
endif()

# Look for a GIT command-line client.
if(NOT DEFINED CTEST_GIT_COMMAND)
  find_program(CTEST_GIT_COMMAND NAMES git git.cmd)
endif()

if(NOT DEFINED CTEST_GIT_COMMAND)
  message(FATAL_ERROR "No Git Found.")
endif()

# Look for coverage command
    message("CTEST_COMVERAGE_COMMAND:${CTEST_COVERAGE_COMMAND}")
if(dashboard_do_coverage)
  if(NOT DEFINED CTEST_COVERAGE_COMMAND)
    find_program(CTEST_COVERAGE_COMMAND NAMES gcov)
  endif()

  if(NOT DEFINED CTEST_COVERAGE_COMMAND)
    message(FATAL_ERROR "No coverage command found")
  else()
    message("CTEST_COMVERAGE_COMMAND:${CTEST_COVERAGE_COMMAND}")
  endif()
endif()


#set(CTEST_MEMORYCHECK_COMMAND "/home/aleinoff/prefix/bin/valgrind" )

# Look for memory checking command
   message("CTEST_MEMORYCHECK_COMMAND:${CTEST_MEMORYCHECK_COMMAND}")
if(dashboard_do_memcheck)
  if(NOT DEFINED CTEST_MEMORYCHECK_COMMAND)
    find_program(CTEST_MEMORYCHECK_COMMAND NAMES valgrind)
  endif()
  if(NOT DEFINED CTEST_MEMORYCHECK_COMMAND)
    message( "No memcheck command found")
  endif()
    message("CTEST_MEMORYCHECK_COMMAND:${CTEST_MEMORYCHECK_COMMAND}")
endif()



# Select a source directory name.
if(NOT DEFINED CTEST_SOURCE_DIRECTORY)
  if(DEFINED dashboard_source_name)
    set(CTEST_SOURCE_DIRECTORY ${CTEST_DASHBOARD_ROOT}/${dashboard_source_name})
  else()
    set(CTEST_SOURCE_DIRECTORY ${CTEST_DASHBOARD_ROOT}/BRAINSTools)
  endif()
endif()

# Select a build directory name.
# Modifying this so multiple ctests can run simultaniously 
# with different types but called from different scripts

if(NOT DEFINED CTEST_BINARY_DIRECTORY)
  if(DEFINED dashboard_binary_name)
    set(CTEST_BINARY_DIRECTORY ${CTEST_DASHBOARD_ROOT}/${dashboard_binary_name})
  else()
    set(CTEST_BINARY_DIRECTORY ${CTEST_SOURCE_DIRECTORY}-build-${CTEST_BUILD_CONFIGURATION})
    if(dashboard_do_coverage)
      set(CTEST_BINARY_DIRECTORY ${CTEST_BINARY_DIRECTORY}-coverage)
    endif()
    if(dashboard_do_memcheck)
      set(CTEST_BINARY_DIRECTORY ${CTEST_BINARY_DIRECTORY}-memcheck)
    endif()
  endif()
endif()

# Select a test directory name.
if(NOT DEFINED CTEST_TESTING_DIRECTORY)
  set(CTEST_TESTING_DIRECTORY ${CTEST_BINARY_DIRECTORY}/${CTEST_PROJECT_NAME}-build)
endif()

# Ctest Build location args
set(CTEST_BUILD_LOCATION_ARGS BUILD ${CTEST_TESTING_DIRECTORY})

# Select a data store.
if(NOT DEFINED ExternalData_OBJECT_STORES)
  if(DEFINED "ENV{ExternalData_OBJECT_STORES}")
    file(TO_CMAKE_PATH "$ENV{ExternalData_OBJECT_STORES}" ExternalData_OBJECT_STORES)
  else()
    if(DEFINED dashboard_data_name)
        set(ExternalData_OBJECT_STORES ${CTEST_DASHBOARD_ROOT}/${dashboard_data_name})
    else()
        set(ExternalData_OBJECT_STORES ${CTEST_DASHBOARD_ROOT}/ExternalData)
    endif()
  endif()
endif()

# Support initial checkout if necessary.
if(NOT EXISTS "${CTEST_SOURCE_DIRECTORY}"
    AND NOT DEFINED CTEST_CHECKOUT_COMMAND)
  get_filename_component(_name "${CTEST_SOURCE_DIRECTORY}" NAME)

  # Generate an initial checkout script.
  set(ctest_checkout_script ${CTEST_DASHBOARD_ROOT}/${_name}-init.cmake)
  file(WRITE ${ctest_checkout_script} "# git repo init script for ${_name}
execute_process(
  COMMAND \"${CTEST_GIT_COMMAND}\" clone -n -b ${dashboard_git_branch}
          -- \"${dashboard_git_url}\" \"${CTEST_SOURCE_DIRECTORY}\"
  )
if(EXISTS \"${CTEST_SOURCE_DIRECTORY}/.git\")
  execute_process(
    COMMAND \"${CTEST_GIT_COMMAND}\" config core.autocrlf ${dashboard_git_crlf}
    WORKING_DIRECTORY \"${CTEST_SOURCE_DIRECTORY}\"
    )
  execute_process(
    COMMAND \"${CTEST_GIT_COMMAND}\" checkout
    WORKING_DIRECTORY \"${CTEST_SOURCE_DIRECTORY}\"
    )
endif()
")
  set(CTEST_CHECKOUT_COMMAND "\"${CMAKE_COMMAND}\" -P \"${ctest_checkout_script}\"")
endif()


#-----------------------------------------------------------------------------

# Send the main script as a note.
list(APPEND CTEST_NOTES_FILES
  "${CTEST_SCRIPT_DIRECTORY}/${CTEST_SCRIPT_NAME}"
  "${CMAKE_CURRENT_LIST_FILE}"
  )

# Check for required variables.
foreach(req
    CTEST_CMAKE_GENERATOR
    CTEST_SITE
    CTEST_BUILD_NAME
    )
  message( "${req}:${${req}}")
  if(NOT DEFINED ${req})
    message(FATAL_ERROR "The containing script must set ${req}")
  endif()
endforeach(req)

# Print summary information.
set(vars "")
foreach(v
    CTEST_SITE
    CTEST_BUILD_NAME
    CTEST_SOURCE_DIRECTORY
    CTEST_BINARY_DIRECTORY
    CTEST_CMAKE_GENERATOR
    CTEST_BUILD_CONFIGURATION
    CTEST_GIT_COMMAND
    CTEST_CHECKOUT_COMMAND
    CTEST_CONFIGURE_COMMAND
    CTEST_SCRIPT_DIRECTORY
    CTEST_USE_LAUNCHERS
    )
  set(vars "${vars}  ${v}=[${${v}}]\n")
endforeach(v)
message("Dashboard script configuration:\n${vars}\n")

# Avoid non-ascii characters in tool output.
set(ENV{LC_ALL} C)

# put coverage vars into dashboard_cache
if(dashboard_do_coverage)
  foreach(COVERAGE_VAR ${COVERAGE_VARS})
    if(DEFINED dashboard_cache)
      set(dashboard_cache "${dashboard_cache}\n")
    endif()
    set(dashboard_cache "${dashboard_cache}${COVERAGE_VAR}=${${COVERAGE_VAR}}")
  endforeach()
endif()

# Helper macro to write the initial cache.
macro(write_cache)
  set(cache_build_type "")
  set(cache_make_program "")
  if(CTEST_CMAKE_GENERATOR MATCHES "Make")
    set(cache_build_type CMAKE_BUILD_TYPE:STRING=${CTEST_BUILD_CONFIGURATION})
    if(CMAKE_MAKE_PROGRAM)
      set(cache_make_program CMAKE_MAKE_PROGRAM:FILEPATH=${CMAKE_MAKE_PROGRAM})
    endif()
  endif()
  file(WRITE ${CTEST_BINARY_DIRECTORY}/CMakeCache.txt "
SITE:STRING=${CTEST_SITE}
BUILDNAME:STRING=${CTEST_BUILD_NAME}
CTEST_USE_LAUNCHERS:BOOL=${CTEST_USE_LAUNCHERS}
DART_TESTING_TIMEOUT:STRING=${CTEST_TEST_TIMEOUT}
ExternalData_OBJECT_STORES:STRING=${ExternalData_OBJECT_STORES}
${cache_build_type}
${cache_make_program}
${dashboard_cache}
")
endmacro()

# Start with a fresh build tree.
set(dashboard_no_clean 1)
if(NOT EXISTS "${CTEST_BINARY_DIRECTORY}")
  file(MAKE_DIRECTORY "${CTEST_BINARY_DIRECTORY}")
elseif(NOT "${CTEST_SOURCE_DIRECTORY}" STREQUAL "${CTEST_BINARY_DIRECTORY}"
    AND NOT dashboard_no_clean)
  message("Clearing build tree...")
  ctest_empty_binary_directory(${CTEST_BINARY_DIRECTORY})
endif()

set(dashboard_continuous 0)
if("${dashboard_model}" STREQUAL "Continuous")
  set(dashboard_continuous 1)
endif()
if(NOT DEFINED dashboard_loop)
  if(dashboard_continuous)
    set(dashboard_loop 43200)
  else()
    set(dashboard_loop 0)
  endif()
endif()

if(COMMAND dashboard_hook_init)
  dashboard_hook_init()
endif()

set(dashboard_done 0)
while(NOT dashboard_done)
  if(dashboard_continuous)
    set(START_TIME ${CTEST_ELAPSED_TIME})
  endif()

  # Start a new submission.
  if(COMMAND dashboard_hook_start)
    dashboard_hook_start()
  endif()
message("############### ctest_start")
  ctest_start(${dashboard_model} ${CTEST_SOURCE_DIRECTORY} ${CTEST_TESTING_DIRECTORY})
message("############### END ctest_start")
  set(CTEST_CHECKOUT_COMMAND) # checkout on first iteration only

  # Always build if the tree is fresh.
  set(dashboard_fresh 0)
  if(NOT EXISTS "${CTEST_BINARY_DIRECTORY}/CMakeCache.txt")
    set(dashboard_fresh 1)
    message("Starting fresh build...")
    write_cache()
  endif()

# Look for updates.
  if(NOT dashboard_model MATCHES "Experimental")
    ctest_update(RETURN_VALUE count)
    message("Found ${count} changed files")
  endif()
  if(dashboard_fresh OR NOT dashboard_continuous OR count GREATER 0)
message("####################ctest_configure")
    ctest_configure()
message("####################END ctest_configure")
message("#################### ctest_read_custom_files")
    ctest_read_custom_files(${CTEST_BINARY_DIRECTORY})
message("#################### END ctest_read_custom_files")
    if(COMMAND dashboard_hook_build)
      dashboard_hook_build()
    endif()
message("#############ctest_build")
    ctest_build()
message("#############END ctest_build")

    if(COMMAND dashboard_hook_test)
      dashboard_hook_test()
    endif()
message("################ ctest_test")
    #ctest_test()
    ctest_test(${CTEST_BUILD_LOCATION_ARGS} ${CTEST_TEST_ARGS})
message("################ END ctest_test")
    if(dashboard_do_coverage)
message("######### about ot do coverage")
#ctest_coverage()
      ctest_coverage(${CTEST_BUILD_LOCATION_ARGS})
      ctest_submit()
#      ctest_coverage(BUILD ${CTEST_TESTING_DIRECTORY})
message("##############end of ctest_coverage")
    endif()
    if(dashboard_do_memcheck)
message("############### ctest_memcheck")
# load the memory check suppressions file
set(CTEST_MEMORYCHECK_SUPPRESSIONS_FILE "${CTEST_BINARY_DIRECTORY}/ITKv4/CMake/InsightValgrind.supp")
message("CTEST_MEMORYCHECK_SUPPRESSIONS_FILE:${CTEST_MEMORYCHECK_SUPPRESSIONS_FILE}")
      ctest_memcheck(${CTEST_BUILD_LOCATION_ARGS})
message("############### END ctest_memcheck")
    endif()
    if(NOT dashboard_no_submit)
#      ctest_submit()
    endif()
    if(COMMAND dashboard_hook_end)
      dashboard_hook_end()
    endif()
  endif()

  if(dashboard_continuous)
    # Delay until at least 5 minutes past START_TIME
    ctest_sleep(${START_TIME} 300 ${CTEST_ELAPSED_TIME})
    if(${CTEST_ELAPSED_TIME} GREATER 43200)
      set(dashboard_done 1)
    endif()
  else()
    # Not continuous, so we are done.
    set(dashboard_done 1)
  endif()
endwhile()
