// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "diwali_interfaces/msg/festival_status.hpp"


#ifndef DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__STRUCT_HPP_
#define DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__diwali_interfaces__msg__FestivalStatus __attribute__((deprecated))
#else
# define DEPRECATED__diwali_interfaces__msg__FestivalStatus __declspec(deprecated)
#endif

namespace diwali_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FestivalStatus_
{
  using Type = FestivalStatus_<ContainerAllocator>;

  explicit FestivalStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = "";
      this->fireworks_enabled = false;
      this->lighting_enabled = false;
      this->sound_enabled = false;
      this->lighting_mode = "";
      this->last_event = "";
      this->events_triggered = 0ul;
      this->events_rejected = 0ul;
      this->seconds_to_next_auto_event = 0.0f;
    }
  }

  explicit FestivalStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init),
    mode(_alloc),
    lighting_mode(_alloc),
    last_event(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = "";
      this->fireworks_enabled = false;
      this->lighting_enabled = false;
      this->sound_enabled = false;
      this->lighting_mode = "";
      this->last_event = "";
      this->events_triggered = 0ul;
      this->events_rejected = 0ul;
      this->seconds_to_next_auto_event = 0.0f;
    }
  }

  // field types and members
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;
  using _mode_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _mode_type mode;
  using _fireworks_enabled_type =
    bool;
  _fireworks_enabled_type fireworks_enabled;
  using _lighting_enabled_type =
    bool;
  _lighting_enabled_type lighting_enabled;
  using _sound_enabled_type =
    bool;
  _sound_enabled_type sound_enabled;
  using _lighting_mode_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _lighting_mode_type lighting_mode;
  using _last_event_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _last_event_type last_event;
  using _events_triggered_type =
    uint32_t;
  _events_triggered_type events_triggered;
  using _events_rejected_type =
    uint32_t;
  _events_rejected_type events_rejected;
  using _seconds_to_next_auto_event_type =
    float;
  _seconds_to_next_auto_event_type seconds_to_next_auto_event;

  // setters for named parameter idiom
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }
  Type & set__mode(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->mode = _arg;
    return *this;
  }
  Type & set__fireworks_enabled(
    const bool & _arg)
  {
    this->fireworks_enabled = _arg;
    return *this;
  }
  Type & set__lighting_enabled(
    const bool & _arg)
  {
    this->lighting_enabled = _arg;
    return *this;
  }
  Type & set__sound_enabled(
    const bool & _arg)
  {
    this->sound_enabled = _arg;
    return *this;
  }
  Type & set__lighting_mode(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->lighting_mode = _arg;
    return *this;
  }
  Type & set__last_event(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->last_event = _arg;
    return *this;
  }
  Type & set__events_triggered(
    const uint32_t & _arg)
  {
    this->events_triggered = _arg;
    return *this;
  }
  Type & set__events_rejected(
    const uint32_t & _arg)
  {
    this->events_rejected = _arg;
    return *this;
  }
  Type & set__seconds_to_next_auto_event(
    const float & _arg)
  {
    this->seconds_to_next_auto_event = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    diwali_interfaces::msg::FestivalStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const diwali_interfaces::msg::FestivalStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<diwali_interfaces::msg::FestivalStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<diwali_interfaces::msg::FestivalStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      diwali_interfaces::msg::FestivalStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<diwali_interfaces::msg::FestivalStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      diwali_interfaces::msg::FestivalStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<diwali_interfaces::msg::FestivalStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<diwali_interfaces::msg::FestivalStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<diwali_interfaces::msg::FestivalStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__diwali_interfaces__msg__FestivalStatus
    std::shared_ptr<diwali_interfaces::msg::FestivalStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__diwali_interfaces__msg__FestivalStatus
    std::shared_ptr<diwali_interfaces::msg::FestivalStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FestivalStatus_ & other) const
  {
    if (this->stamp != other.stamp) {
      return false;
    }
    if (this->mode != other.mode) {
      return false;
    }
    if (this->fireworks_enabled != other.fireworks_enabled) {
      return false;
    }
    if (this->lighting_enabled != other.lighting_enabled) {
      return false;
    }
    if (this->sound_enabled != other.sound_enabled) {
      return false;
    }
    if (this->lighting_mode != other.lighting_mode) {
      return false;
    }
    if (this->last_event != other.last_event) {
      return false;
    }
    if (this->events_triggered != other.events_triggered) {
      return false;
    }
    if (this->events_rejected != other.events_rejected) {
      return false;
    }
    if (this->seconds_to_next_auto_event != other.seconds_to_next_auto_event) {
      return false;
    }
    return true;
  }
  bool operator!=(const FestivalStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FestivalStatus_

// alias to use template instance with default allocator
using FestivalStatus =
  diwali_interfaces::msg::FestivalStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace diwali_interfaces

#endif  // DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__STRUCT_HPP_
