#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to diwali_interfaces__msg__FestivalStatus
/// Published on /festival/event_status (reliable, transient_local, depth 1)

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct FestivalStatus {

    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::Time,

    /// AUTONOMOUS | MANUAL
    pub mode: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub fireworks_enabled: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub lighting_enabled: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub sound_enabled: bool,

    /// on | off | dim | bright | twinkle | festive
    pub lighting_mode: std::string::String,

    /// e.g. "golden_burst@fw_n1 ACCEPTED (topic)"
    pub last_event: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub events_triggered: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub events_rejected: u32,

    /// -1 when autonomous mode is off
    pub seconds_to_next_auto_event: f32,

}



impl Default for FestivalStatus {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::FestivalStatus::default())
  }
}

impl rosidl_runtime_rs::Message for FestivalStatus {
  type RmwMsg = super::msg::rmw::FestivalStatus;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.stamp)).into_owned(),
        mode: msg.mode.as_str().into(),
        fireworks_enabled: msg.fireworks_enabled,
        lighting_enabled: msg.lighting_enabled,
        sound_enabled: msg.sound_enabled,
        lighting_mode: msg.lighting_mode.as_str().into(),
        last_event: msg.last_event.as_str().into(),
        events_triggered: msg.events_triggered,
        events_rejected: msg.events_rejected,
        seconds_to_next_auto_event: msg.seconds_to_next_auto_event,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.stamp)).into_owned(),
        mode: msg.mode.as_str().into(),
      fireworks_enabled: msg.fireworks_enabled,
      lighting_enabled: msg.lighting_enabled,
      sound_enabled: msg.sound_enabled,
        lighting_mode: msg.lighting_mode.as_str().into(),
        last_event: msg.last_event.as_str().into(),
      events_triggered: msg.events_triggered,
      events_rejected: msg.events_rejected,
      seconds_to_next_auto_event: msg.seconds_to_next_auto_event,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      stamp: builtin_interfaces::msg::Time::from_rmw_message(msg.stamp),
      mode: msg.mode.to_string(),
      fireworks_enabled: msg.fireworks_enabled,
      lighting_enabled: msg.lighting_enabled,
      sound_enabled: msg.sound_enabled,
      lighting_mode: msg.lighting_mode.to_string(),
      last_event: msg.last_event.to_string(),
      events_triggered: msg.events_triggered,
      events_rejected: msg.events_rejected,
      seconds_to_next_auto_event: msg.seconds_to_next_auto_event,
    }
  }
}


