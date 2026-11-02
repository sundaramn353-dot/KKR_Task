// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "diwali_interfaces/msg/festival_status.hpp"


#ifndef DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__TRAITS_HPP_
#define DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "diwali_interfaces/msg/detail/festival_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace diwali_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const FestivalStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
    out << ", ";
  }

  // member: mode
  {
    out << "mode: ";
    rosidl_generator_traits::value_to_yaml(msg.mode, out);
    out << ", ";
  }

  // member: fireworks_enabled
  {
    out << "fireworks_enabled: ";
    rosidl_generator_traits::value_to_yaml(msg.fireworks_enabled, out);
    out << ", ";
  }

  // member: lighting_enabled
  {
    out << "lighting_enabled: ";
    rosidl_generator_traits::value_to_yaml(msg.lighting_enabled, out);
    out << ", ";
  }

  // member: sound_enabled
  {
    out << "sound_enabled: ";
    rosidl_generator_traits::value_to_yaml(msg.sound_enabled, out);
    out << ", ";
  }

  // member: lighting_mode
  {
    out << "lighting_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.lighting_mode, out);
    out << ", ";
  }

  // member: last_event
  {
    out << "last_event: ";
    rosidl_generator_traits::value_to_yaml(msg.last_event, out);
    out << ", ";
  }

  // member: events_triggered
  {
    out << "events_triggered: ";
    rosidl_generator_traits::value_to_yaml(msg.events_triggered, out);
    out << ", ";
  }

  // member: events_rejected
  {
    out << "events_rejected: ";
    rosidl_generator_traits::value_to_yaml(msg.events_rejected, out);
    out << ", ";
  }

  // member: seconds_to_next_auto_event
  {
    out << "seconds_to_next_auto_event: ";
    rosidl_generator_traits::value_to_yaml(msg.seconds_to_next_auto_event, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FestivalStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }

  // member: mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "mode: ";
    rosidl_generator_traits::value_to_yaml(msg.mode, out);
    out << "\n";
  }

  // member: fireworks_enabled
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fireworks_enabled: ";
    rosidl_generator_traits::value_to_yaml(msg.fireworks_enabled, out);
    out << "\n";
  }

  // member: lighting_enabled
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lighting_enabled: ";
    rosidl_generator_traits::value_to_yaml(msg.lighting_enabled, out);
    out << "\n";
  }

  // member: sound_enabled
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sound_enabled: ";
    rosidl_generator_traits::value_to_yaml(msg.sound_enabled, out);
    out << "\n";
  }

  // member: lighting_mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lighting_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.lighting_mode, out);
    out << "\n";
  }

  // member: last_event
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "last_event: ";
    rosidl_generator_traits::value_to_yaml(msg.last_event, out);
    out << "\n";
  }

  // member: events_triggered
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "events_triggered: ";
    rosidl_generator_traits::value_to_yaml(msg.events_triggered, out);
    out << "\n";
  }

  // member: events_rejected
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "events_rejected: ";
    rosidl_generator_traits::value_to_yaml(msg.events_rejected, out);
    out << "\n";
  }

  // member: seconds_to_next_auto_event
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "seconds_to_next_auto_event: ";
    rosidl_generator_traits::value_to_yaml(msg.seconds_to_next_auto_event, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FestivalStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace diwali_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use diwali_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const diwali_interfaces::msg::FestivalStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  diwali_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use diwali_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const diwali_interfaces::msg::FestivalStatus & msg)
{
  return diwali_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<diwali_interfaces::msg::FestivalStatus>()
{
  return "diwali_interfaces::msg::FestivalStatus";
}

template<>
inline const char * name<diwali_interfaces::msg::FestivalStatus>()
{
  return "diwali_interfaces/msg/FestivalStatus";
}

template<>
struct has_fixed_size<diwali_interfaces::msg::FestivalStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<diwali_interfaces::msg::FestivalStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<diwali_interfaces::msg::FestivalStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__TRAITS_HPP_
