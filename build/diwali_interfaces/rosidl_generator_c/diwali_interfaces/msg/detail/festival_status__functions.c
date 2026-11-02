// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice
#include "diwali_interfaces/msg/detail/festival_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"
// Member `mode`
// Member `lighting_mode`
// Member `last_event`
#include "rosidl_runtime_c/string_functions.h"

bool
diwali_interfaces__msg__FestivalStatus__init(diwali_interfaces__msg__FestivalStatus * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    diwali_interfaces__msg__FestivalStatus__fini(msg);
    return false;
  }
  // mode
  if (!rosidl_runtime_c__String__init(&msg->mode)) {
    diwali_interfaces__msg__FestivalStatus__fini(msg);
    return false;
  }
  // fireworks_enabled
  // lighting_enabled
  // sound_enabled
  // lighting_mode
  if (!rosidl_runtime_c__String__init(&msg->lighting_mode)) {
    diwali_interfaces__msg__FestivalStatus__fini(msg);
    return false;
  }
  // last_event
  if (!rosidl_runtime_c__String__init(&msg->last_event)) {
    diwali_interfaces__msg__FestivalStatus__fini(msg);
    return false;
  }
  // events_triggered
  // events_rejected
  // seconds_to_next_auto_event
  return true;
}

void
diwali_interfaces__msg__FestivalStatus__fini(diwali_interfaces__msg__FestivalStatus * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // mode
  rosidl_runtime_c__String__fini(&msg->mode);
  // fireworks_enabled
  // lighting_enabled
  // sound_enabled
  // lighting_mode
  rosidl_runtime_c__String__fini(&msg->lighting_mode);
  // last_event
  rosidl_runtime_c__String__fini(&msg->last_event);
  // events_triggered
  // events_rejected
  // seconds_to_next_auto_event
}

bool
diwali_interfaces__msg__FestivalStatus__are_equal(const diwali_interfaces__msg__FestivalStatus * lhs, const diwali_interfaces__msg__FestivalStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  // mode
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->mode), &(rhs->mode)))
  {
    return false;
  }
  // fireworks_enabled
  if (lhs->fireworks_enabled != rhs->fireworks_enabled) {
    return false;
  }
  // lighting_enabled
  if (lhs->lighting_enabled != rhs->lighting_enabled) {
    return false;
  }
  // sound_enabled
  if (lhs->sound_enabled != rhs->sound_enabled) {
    return false;
  }
  // lighting_mode
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->lighting_mode), &(rhs->lighting_mode)))
  {
    return false;
  }
  // last_event
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->last_event), &(rhs->last_event)))
  {
    return false;
  }
  // events_triggered
  if (lhs->events_triggered != rhs->events_triggered) {
    return false;
  }
  // events_rejected
  if (lhs->events_rejected != rhs->events_rejected) {
    return false;
  }
  // seconds_to_next_auto_event
  if (lhs->seconds_to_next_auto_event != rhs->seconds_to_next_auto_event) {
    return false;
  }
  return true;
}

bool
diwali_interfaces__msg__FestivalStatus__copy(
  const diwali_interfaces__msg__FestivalStatus * input,
  diwali_interfaces__msg__FestivalStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  // mode
  if (!rosidl_runtime_c__String__copy(
      &(input->mode), &(output->mode)))
  {
    return false;
  }
  // fireworks_enabled
  output->fireworks_enabled = input->fireworks_enabled;
  // lighting_enabled
  output->lighting_enabled = input->lighting_enabled;
  // sound_enabled
  output->sound_enabled = input->sound_enabled;
  // lighting_mode
  if (!rosidl_runtime_c__String__copy(
      &(input->lighting_mode), &(output->lighting_mode)))
  {
    return false;
  }
  // last_event
  if (!rosidl_runtime_c__String__copy(
      &(input->last_event), &(output->last_event)))
  {
    return false;
  }
  // events_triggered
  output->events_triggered = input->events_triggered;
  // events_rejected
  output->events_rejected = input->events_rejected;
  // seconds_to_next_auto_event
  output->seconds_to_next_auto_event = input->seconds_to_next_auto_event;
  return true;
}

diwali_interfaces__msg__FestivalStatus *
diwali_interfaces__msg__FestivalStatus__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  diwali_interfaces__msg__FestivalStatus * msg = (diwali_interfaces__msg__FestivalStatus *)allocator.allocate(sizeof(diwali_interfaces__msg__FestivalStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(diwali_interfaces__msg__FestivalStatus));
  bool success = diwali_interfaces__msg__FestivalStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
diwali_interfaces__msg__FestivalStatus__destroy(diwali_interfaces__msg__FestivalStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    diwali_interfaces__msg__FestivalStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
diwali_interfaces__msg__FestivalStatus__Sequence__init(diwali_interfaces__msg__FestivalStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  diwali_interfaces__msg__FestivalStatus * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(diwali_interfaces__msg__FestivalStatus)) {
      return false;
    }
    data = (diwali_interfaces__msg__FestivalStatus *)allocator.zero_allocate(size, sizeof(diwali_interfaces__msg__FestivalStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = diwali_interfaces__msg__FestivalStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        diwali_interfaces__msg__FestivalStatus__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
diwali_interfaces__msg__FestivalStatus__Sequence__fini(diwali_interfaces__msg__FestivalStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      diwali_interfaces__msg__FestivalStatus__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

diwali_interfaces__msg__FestivalStatus__Sequence *
diwali_interfaces__msg__FestivalStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  diwali_interfaces__msg__FestivalStatus__Sequence * array = (diwali_interfaces__msg__FestivalStatus__Sequence *)allocator.allocate(sizeof(diwali_interfaces__msg__FestivalStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = diwali_interfaces__msg__FestivalStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
diwali_interfaces__msg__FestivalStatus__Sequence__destroy(diwali_interfaces__msg__FestivalStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    diwali_interfaces__msg__FestivalStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
diwali_interfaces__msg__FestivalStatus__Sequence__are_equal(const diwali_interfaces__msg__FestivalStatus__Sequence * lhs, const diwali_interfaces__msg__FestivalStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!diwali_interfaces__msg__FestivalStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
diwali_interfaces__msg__FestivalStatus__Sequence__copy(
  const diwali_interfaces__msg__FestivalStatus__Sequence * input,
  diwali_interfaces__msg__FestivalStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(diwali_interfaces__msg__FestivalStatus)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(diwali_interfaces__msg__FestivalStatus);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    diwali_interfaces__msg__FestivalStatus * data =
      (diwali_interfaces__msg__FestivalStatus *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!diwali_interfaces__msg__FestivalStatus__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          diwali_interfaces__msg__FestivalStatus__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!diwali_interfaces__msg__FestivalStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
