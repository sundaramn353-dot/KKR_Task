// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "diwali_interfaces/msg/detail/festival_status__rosidl_typesupport_introspection_c.h"
#include "diwali_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "diwali_interfaces/msg/detail/festival_status__functions.h"
#include "diwali_interfaces/msg/detail/festival_status__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"
// Member `mode`
// Member `lighting_mode`
// Member `last_event`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  diwali_interfaces__msg__FestivalStatus__init(message_memory);
}

void diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_fini_function(void * message_memory)
{
  diwali_interfaces__msg__FestivalStatus__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_member_array[10] = {
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "mode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, mode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "fireworks_enabled",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, fireworks_enabled),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "lighting_enabled",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, lighting_enabled),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sound_enabled",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, sound_enabled),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "lighting_mode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, lighting_mode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "last_event",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, last_event),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "events_triggered",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, events_triggered),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "events_rejected",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, events_rejected),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "seconds_to_next_auto_event",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(diwali_interfaces__msg__FestivalStatus, seconds_to_next_auto_event),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_members = {
  "diwali_interfaces__msg",  // message namespace
  "FestivalStatus",  // message name
  10,  // number of fields
  sizeof(diwali_interfaces__msg__FestivalStatus),
  false,  // has_any_key_member_
  diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_member_array,  // message members
  diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_type_support_handle = {
  0,
  &diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_members,
  get_message_typesupport_handle_function,
  &diwali_interfaces__msg__FestivalStatus__get_type_hash,
  &diwali_interfaces__msg__FestivalStatus__get_type_description,
  &diwali_interfaces__msg__FestivalStatus__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_diwali_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, diwali_interfaces, msg, FestivalStatus)() {
  diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_type_support_handle.typesupport_identifier) {
    diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &diwali_interfaces__msg__FestivalStatus__rosidl_typesupport_introspection_c__FestivalStatus_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
