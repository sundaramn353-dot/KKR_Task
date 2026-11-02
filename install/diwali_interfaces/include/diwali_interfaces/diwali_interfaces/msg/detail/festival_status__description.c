// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from diwali_interfaces:msg/FestivalStatus.idl
// generated code does not contain a copyright notice

#include "diwali_interfaces/msg/detail/festival_status__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_diwali_interfaces
const rosidl_type_hash_t *
diwali_interfaces__msg__FestivalStatus__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x76, 0x18, 0x48, 0x64, 0x13, 0x12, 0x8f, 0x62,
      0x52, 0xde, 0x14, 0xb4, 0xdf, 0x36, 0x4b, 0x98,
      0x9a, 0xd4, 0xf5, 0xad, 0x6d, 0x37, 0x97, 0xde,
      0x3d, 0x74, 0x06, 0xf4, 0x89, 0x12, 0xf4, 0x41,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
#endif

static char diwali_interfaces__msg__FestivalStatus__TYPE_NAME[] = "diwali_interfaces/msg/FestivalStatus";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";

// Define type names, field names, and default values
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__stamp[] = "stamp";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__mode[] = "mode";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__fireworks_enabled[] = "fireworks_enabled";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__lighting_enabled[] = "lighting_enabled";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__sound_enabled[] = "sound_enabled";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__lighting_mode[] = "lighting_mode";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__last_event[] = "last_event";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__events_triggered[] = "events_triggered";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__events_rejected[] = "events_rejected";
static char diwali_interfaces__msg__FestivalStatus__FIELD_NAME__seconds_to_next_auto_event[] = "seconds_to_next_auto_event";

static rosidl_runtime_c__type_description__Field diwali_interfaces__msg__FestivalStatus__FIELDS[] = {
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__stamp, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__mode, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__fireworks_enabled, 17, 17},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__lighting_enabled, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__sound_enabled, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__lighting_mode, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__last_event, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__events_triggered, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__events_rejected, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {diwali_interfaces__msg__FestivalStatus__FIELD_NAME__seconds_to_next_auto_event, 26, 26},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription diwali_interfaces__msg__FestivalStatus__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
diwali_interfaces__msg__FestivalStatus__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {diwali_interfaces__msg__FestivalStatus__TYPE_NAME, 36, 36},
      {diwali_interfaces__msg__FestivalStatus__FIELDS, 10, 10},
    },
    {diwali_interfaces__msg__FestivalStatus__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# Published on /festival/event_status (reliable, transient_local, depth 1)\n"
  "builtin_interfaces/Time stamp\n"
  "string mode                       # AUTONOMOUS | MANUAL\n"
  "bool fireworks_enabled\n"
  "bool lighting_enabled\n"
  "bool sound_enabled\n"
  "string lighting_mode              # on | off | dim | bright | twinkle | festive\n"
  "string last_event                 # e.g. \"golden_burst@fw_n1 ACCEPTED (topic)\"\n"
  "uint32 events_triggered\n"
  "uint32 events_rejected\n"
  "float32 seconds_to_next_auto_event   # -1 when autonomous mode is off";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
diwali_interfaces__msg__FestivalStatus__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {diwali_interfaces__msg__FestivalStatus__TYPE_NAME, 36, 36},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 501, 501},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
diwali_interfaces__msg__FestivalStatus__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *diwali_interfaces__msg__FestivalStatus__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
