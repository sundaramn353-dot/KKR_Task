// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "diwali_interfaces/msg/festival_status.h"


#ifndef DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__FUNCTIONS_H_
#define DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_runtime_c/type_description/type_description__struct.h"
#include "rosidl_runtime_c/type_description/type_source__struct.h"
#include "rosidl_runtime_c/type_hash.h"
#include "rosidl_runtime_c/visibility_control.h"
#include "diwali_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "diwali_interfaces/msg/detail/festival_status__struct.h"

/// Initialize msg/FestivalStatus message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * diwali_interfaces__msg__FestivalStatus
 * )) before or use
 * diwali_interfaces__msg__FestivalStatus__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
bool
diwali_interfaces__msg__FestivalStatus__init(diwali_interfaces__msg__FestivalStatus * msg);

/// Finalize msg/FestivalStatus message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
void
diwali_interfaces__msg__FestivalStatus__fini(diwali_interfaces__msg__FestivalStatus * msg);

/// Create msg/FestivalStatus message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * diwali_interfaces__msg__FestivalStatus__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
diwali_interfaces__msg__FestivalStatus *
diwali_interfaces__msg__FestivalStatus__create(void);

/// Destroy msg/FestivalStatus message.
/**
 * It calls
 * diwali_interfaces__msg__FestivalStatus__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
void
diwali_interfaces__msg__FestivalStatus__destroy(diwali_interfaces__msg__FestivalStatus * msg);

/// Check for msg/FestivalStatus message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
bool
diwali_interfaces__msg__FestivalStatus__are_equal(const diwali_interfaces__msg__FestivalStatus * lhs, const diwali_interfaces__msg__FestivalStatus * rhs);

/// Copy a msg/FestivalStatus message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
bool
diwali_interfaces__msg__FestivalStatus__copy(
  const diwali_interfaces__msg__FestivalStatus * input,
  diwali_interfaces__msg__FestivalStatus * output);

/// Retrieve pointer to the hash of the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
const rosidl_type_hash_t *
diwali_interfaces__msg__FestivalStatus__get_type_hash(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
const rosidl_runtime_c__type_description__TypeDescription *
diwali_interfaces__msg__FestivalStatus__get_type_description(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the single raw source text that defined this type.
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
const rosidl_runtime_c__type_description__TypeSource *
diwali_interfaces__msg__FestivalStatus__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the recursive raw sources that defined the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
const rosidl_runtime_c__type_description__TypeSource__Sequence *
diwali_interfaces__msg__FestivalStatus__get_type_description_sources(
  const rosidl_message_type_support_t * type_support);

/// Initialize array of msg/FestivalStatus messages.
/**
 * It allocates the memory for the number of elements and calls
 * diwali_interfaces__msg__FestivalStatus__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
bool
diwali_interfaces__msg__FestivalStatus__Sequence__init(diwali_interfaces__msg__FestivalStatus__Sequence * array, size_t size);

/// Finalize array of msg/FestivalStatus messages.
/**
 * It calls
 * diwali_interfaces__msg__FestivalStatus__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
void
diwali_interfaces__msg__FestivalStatus__Sequence__fini(diwali_interfaces__msg__FestivalStatus__Sequence * array);

/// Create array of msg/FestivalStatus messages.
/**
 * It allocates the memory for the array and calls
 * diwali_interfaces__msg__FestivalStatus__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
diwali_interfaces__msg__FestivalStatus__Sequence *
diwali_interfaces__msg__FestivalStatus__Sequence__create(size_t size);

/// Destroy array of msg/FestivalStatus messages.
/**
 * It calls
 * diwali_interfaces__msg__FestivalStatus__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
void
diwali_interfaces__msg__FestivalStatus__Sequence__destroy(diwali_interfaces__msg__FestivalStatus__Sequence * array);

/// Check for msg/FestivalStatus message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
bool
diwali_interfaces__msg__FestivalStatus__Sequence__are_equal(const diwali_interfaces__msg__FestivalStatus__Sequence * lhs, const diwali_interfaces__msg__FestivalStatus__Sequence * rhs);

/// Copy an array of msg/FestivalStatus messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
bool
diwali_interfaces__msg__FestivalStatus__Sequence__copy(
  const diwali_interfaces__msg__FestivalStatus__Sequence * input,
  diwali_interfaces__msg__FestivalStatus__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__FUNCTIONS_H_
