# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target diwali_interfaces::diwali_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${diwali_interfaces_TARGETS}.
if(diwali_interfaces_TARGETS AND NOT TARGET diwali_interfaces::diwali_interfaces)
  add_library(diwali_interfaces::diwali_interfaces INTERFACE IMPORTED)
  set_target_properties(diwali_interfaces::diwali_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${diwali_interfaces_TARGETS}")
endif()
