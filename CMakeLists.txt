cmake_minimum_required(VERSION 3.10)
# TODO: named this project here
project(action)

set(CMAKE_CXX_STANDARD 17)

find_package(GTest REQUIRED)

aux_source_directory(src ALL_SOURCES)

set(SOURCES ${ALL_SOURCES})
list(FILTER SOURCES EXCLUDE REGEX "^.*Test.cpp$")
add_library(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PUBLIC include)

set(TEST_SOURCES ${ALL_SOURCES})
list(FILTER TEST_SOURCES INCLUDE REGEX "^.*Test.cpp$")
if(NOT "${TEST_SOURCES}" STREQUAL "")
    add_executable(${PROJECT_NAME}_test ${TEST_SOURCES})
    target_link_libraries(${PROJECT_NAME}_test GTest::GTest)
    enable_testing()
    add_test(NAME test COMMAND ${PROJECT_NAME}_test)
endif()
