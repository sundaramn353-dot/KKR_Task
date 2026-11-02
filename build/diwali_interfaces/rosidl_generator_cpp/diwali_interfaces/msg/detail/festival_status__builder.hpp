// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "diwali_interfaces/msg/festival_status.hpp"


#ifndef DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__BUILDER_HPP_
#define DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "diwali_interfaces/msg/detail/festival_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace diwali_interfaces
{

namespace msg
{

namespace builder
{

class Init_FestivalStatus_seconds_to_next_auto_event
{
public:
  explicit Init_FestivalStatus_seconds_to_next_auto_event(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  ::diwali_interfaces::msg::FestivalStatus seconds_to_next_auto_event(::diwali_interfaces::msg::FestivalStatus::_seconds_to_next_auto_event_type arg)
  {
    msg_.seconds_to_next_auto_event = std::move(arg);
    return std::move(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_events_rejected
{
public:
  explicit Init_FestivalStatus_events_rejected(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  Init_FestivalStatus_seconds_to_next_auto_event events_rejected(::diwali_interfaces::msg::FestivalStatus::_events_rejected_type arg)
  {
    msg_.events_rejected = std::move(arg);
    return Init_FestivalStatus_seconds_to_next_auto_event(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_events_triggered
{
public:
  explicit Init_FestivalStatus_events_triggered(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  Init_FestivalStatus_events_rejected events_triggered(::diwali_interfaces::msg::FestivalStatus::_events_triggered_type arg)
  {
    msg_.events_triggered = std::move(arg);
    return Init_FestivalStatus_events_rejected(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_last_event
{
public:
  explicit Init_FestivalStatus_last_event(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  Init_FestivalStatus_events_triggered last_event(::diwali_interfaces::msg::FestivalStatus::_last_event_type arg)
  {
    msg_.last_event = std::move(arg);
    return Init_FestivalStatus_events_triggered(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_lighting_mode
{
public:
  explicit Init_FestivalStatus_lighting_mode(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  Init_FestivalStatus_last_event lighting_mode(::diwali_interfaces::msg::FestivalStatus::_lighting_mode_type arg)
  {
    msg_.lighting_mode = std::move(arg);
    return Init_FestivalStatus_last_event(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_sound_enabled
{
public:
  explicit Init_FestivalStatus_sound_enabled(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  Init_FestivalStatus_lighting_mode sound_enabled(::diwali_interfaces::msg::FestivalStatus::_sound_enabled_type arg)
  {
    msg_.sound_enabled = std::move(arg);
    return Init_FestivalStatus_lighting_mode(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_lighting_enabled
{
public:
  explicit Init_FestivalStatus_lighting_enabled(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  Init_FestivalStatus_sound_enabled lighting_enabled(::diwali_interfaces::msg::FestivalStatus::_lighting_enabled_type arg)
  {
    msg_.lighting_enabled = std::move(arg);
    return Init_FestivalStatus_sound_enabled(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_fireworks_enabled
{
public:
  explicit Init_FestivalStatus_fireworks_enabled(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  Init_FestivalStatus_lighting_enabled fireworks_enabled(::diwali_interfaces::msg::FestivalStatus::_fireworks_enabled_type arg)
  {
    msg_.fireworks_enabled = std::move(arg);
    return Init_FestivalStatus_lighting_enabled(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_mode
{
public:
  explicit Init_FestivalStatus_mode(::diwali_interfaces::msg::FestivalStatus & msg)
  : msg_(msg)
  {}
  Init_FestivalStatus_fireworks_enabled mode(::diwali_interfaces::msg::FestivalStatus::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return Init_FestivalStatus_fireworks_enabled(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

class Init_FestivalStatus_stamp
{
public:
  Init_FestivalStatus_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FestivalStatus_mode stamp(::diwali_interfaces::msg::FestivalStatus::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_FestivalStatus_mode(msg_);
  }

private:
  ::diwali_interfaces::msg::FestivalStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::diwali_interfaces::msg::FestivalStatus>()
{
  return diwali_interfaces::msg::builder::Init_FestivalStatus_stamp();
}

}  // namespace diwali_interfaces

#endif  // DIWALI_INTERFACES__MSG__DETAIL__FESTIVAL_STATUS__BUILDER_HPP_
