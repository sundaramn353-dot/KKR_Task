#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "diwali_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__diwali_interfaces__msg__FestivalStatus() -> *const std::ffi::c_void;
}

#[link(name = "diwali_interfaces__rosidl_generator_c")]
extern "C" {
    fn diwali_interfaces__msg__FestivalStatus__init(msg: *mut FestivalStatus) -> bool;
    fn diwali_interfaces__msg__FestivalStatus__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<FestivalStatus>, size: usize) -> bool;
    fn diwali_interfaces__msg__FestivalStatus__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<FestivalStatus>);
    fn diwali_interfaces__msg__FestivalStatus__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<FestivalStatus>, out_seq: *mut rosidl_runtime_rs::Sequence<FestivalStatus>) -> bool;
}

// Corresponds to diwali_interfaces__msg__FestivalStatus
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Published on /festival/event_status (reliable, transient_local, depth 1)

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct FestivalStatus {

    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

    /// AUTONOMOUS | MANUAL
    pub mode: rosidl_runtime_rs::String,


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
    pub lighting_mode: rosidl_runtime_rs::String,

    /// e.g. "golden_burst@fw_n1 ACCEPTED (topic)"
    pub last_event: rosidl_runtime_rs::String,


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
    unsafe {
      let mut msg = std::mem::zeroed();
      if !diwali_interfaces__msg__FestivalStatus__init(&mut msg as *mut _) {
        panic!("Call to diwali_interfaces__msg__FestivalStatus__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for FestivalStatus {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { diwali_interfaces__msg__FestivalStatus__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { diwali_interfaces__msg__FestivalStatus__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { diwali_interfaces__msg__FestivalStatus__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for FestivalStatus {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for FestivalStatus where Self: Sized {
  const TYPE_NAME: &'static str = "diwali_interfaces/msg/FestivalStatus";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__diwali_interfaces__msg__FestivalStatus() }
  }
}


