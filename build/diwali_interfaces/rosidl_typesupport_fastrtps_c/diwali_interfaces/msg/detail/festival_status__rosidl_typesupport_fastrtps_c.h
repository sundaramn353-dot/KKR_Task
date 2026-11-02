// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice
#ifndef DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "diwali_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "diwali_interfaces/msg/detail/festival_status__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_diwali_interfaces
bool cdr_serialize_diwali_interfaces__msg__FestivalStatus(
  const diwali_interfaces__msg__FestivalStatus * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_diwali_interfaces
bool cdr_deserialize_diwali_interfaces__msg__FestivalStatus(
  eprosima::fastcdr::Cdr &,
  diwali_interfaces__msg__FestivalStatus * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_diwali_interfaces
size_t get_serialized_size_diwali_interfaces__msg__FestivalStatus(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_diwali_interfaces
size_t max_serialized_size_diwali_interfaces__msg__FestivalStatus(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_diwali_interfaces
bool cdr_serialize_key_diwali_interfaces__msg__FestivalStatus(
  const diwali_interfaces__msg__FestivalStatus * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_diwali_interfaces
size_t get_serialized_size_key_diwali_interfaces__msg__FestivalStatus(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_diwali_interfaces
size_t max_serialized_size_key_diwali_interfaces__msg__FestivalStatus(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_diwali_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, diwali_interfaces, msg, FestivalStatus)();

#ifdef __cplusplus
}
#endif

#endif  // DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
