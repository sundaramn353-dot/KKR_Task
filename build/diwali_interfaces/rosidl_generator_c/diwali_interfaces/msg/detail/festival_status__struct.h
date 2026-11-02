// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "diwali_interfaces/msg/festival_status.h"


#ifndef DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__STRUCT_H_
#define DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"
// Member 'mode'
// Member 'lighting_mode'
// Member 'last_event'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/FestivalStatus in the package diwali_interfaces.
/**
  * Published on /festival/event_status (reliable, transient_local, depth 1)
 */
typedef struct diwali_interfaces__msg__FestivalStatus
{
  builtin_interfaces__msg__Time stamp;
  /// AUTONOMOUS | MANUAL
  rosidl_runtime_c__String mode;
  bool fireworks_enabled;
  bool lighting_enabled;
  bool sound_enabled;
  /// on | off | dim | bright | twinkle | festive
  rosidl_runtime_c__String lighting_mode;
  /// e.g. "golden_burst@fw_n1 ACCEPTED (topic)"
  rosidl_runtime_c__String last_event;
  uint32_t events_triggered;
  uint32_t events_rejected;
  /// -1 when autonomous mode is off
  float seconds_to_next_auto_event;
} diwali_interfaces__msg__FestivalStatus;

// Struct for a sequence of diwali_interfaces__msg__FestivalStatus.
typedef struct diwali_interfaces__msg__FestivalStatus__Sequence
{
  diwali_interfaces__msg__FestivalStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} diwali_interfaces__msg__FestivalStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__STRUCT_H_
