# generated from rosidl_generator_py/resource/_idl.py.em
# with input from diwali_interfaces:msg/FestivalStatus.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FestivalStatus(type):
    """Metaclass of message 'FestivalStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('diwali_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'diwali_interfaces.msg.FestivalStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__festival_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__festival_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__festival_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__festival_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__festival_status

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FestivalStatus(metaclass=Metaclass_FestivalStatus):
    """Message class 'FestivalStatus'."""

    __slots__ = [
        '_stamp',
        '_mode',
        '_fireworks_enabled',
        '_lighting_enabled',
        '_sound_enabled',
        '_lighting_mode',
        '_last_event',
        '_events_triggered',
        '_events_rejected',
        '_seconds_to_next_auto_event',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'stamp': 'builtin_interfaces/Time',
        'mode': 'string',
        'fireworks_enabled': 'boolean',
        'lighting_enabled': 'boolean',
        'sound_enabled': 'boolean',
        'lighting_mode': 'string',
        'last_event': 'string',
        'events_triggered': 'uint32',
        'events_rejected': 'uint32',
        'seconds_to_next_auto_event': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())
        self.mode = kwargs.get('mode', str())
        self.fireworks_enabled = kwargs.get('fireworks_enabled', bool())
        self.lighting_enabled = kwargs.get('lighting_enabled', bool())
        self.sound_enabled = kwargs.get('sound_enabled', bool())
        self.lighting_mode = kwargs.get('lighting_mode', str())
        self.last_event = kwargs.get('last_event', str())
        self.events_triggered = kwargs.get('events_triggered', int())
        self.events_rejected = kwargs.get('events_rejected', int())
        self.seconds_to_next_auto_event = kwargs.get('seconds_to_next_auto_event', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.stamp != other.stamp:
            return False
        if self.mode != other.mode:
            return False
        if self.fireworks_enabled != other.fireworks_enabled:
            return False
        if self.lighting_enabled != other.lighting_enabled:
            return False
        if self.sound_enabled != other.sound_enabled:
            return False
        if self.lighting_mode != other.lighting_mode:
            return False
        if self.last_event != other.last_event:
            return False
        if self.events_triggered != other.events_triggered:
            return False
        if self.events_rejected != other.events_rejected:
            return False
        if self.seconds_to_next_auto_event != other.seconds_to_next_auto_event:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if self._check_fields:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value

    @builtins.property
    def mode(self):
        """Message field 'mode'."""
        return self._mode

    @mode.setter
    def mode(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'mode' field must be of type 'str'"
        self._mode = value

    @builtins.property
    def fireworks_enabled(self):
        """Message field 'fireworks_enabled'."""
        return self._fireworks_enabled

    @fireworks_enabled.setter
    def fireworks_enabled(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'fireworks_enabled' field must be of type 'bool'"
        self._fireworks_enabled = value

    @builtins.property
    def lighting_enabled(self):
        """Message field 'lighting_enabled'."""
        return self._lighting_enabled

    @lighting_enabled.setter
    def lighting_enabled(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'lighting_enabled' field must be of type 'bool'"
        self._lighting_enabled = value

    @builtins.property
    def sound_enabled(self):
        """Message field 'sound_enabled'."""
        return self._sound_enabled

    @sound_enabled.setter
    def sound_enabled(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'sound_enabled' field must be of type 'bool'"
        self._sound_enabled = value

    @builtins.property
    def lighting_mode(self):
        """Message field 'lighting_mode'."""
        return self._lighting_mode

    @lighting_mode.setter
    def lighting_mode(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'lighting_mode' field must be of type 'str'"
        self._lighting_mode = value

    @builtins.property
    def last_event(self):
        """Message field 'last_event'."""
        return self._last_event

    @last_event.setter
    def last_event(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'last_event' field must be of type 'str'"
        self._last_event = value

    @builtins.property
    def events_triggered(self):
        """Message field 'events_triggered'."""
        return self._events_triggered

    @events_triggered.setter
    def events_triggered(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'events_triggered' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'events_triggered' field must be an unsigned integer in [0, 4294967295]"
        self._events_triggered = value

    @builtins.property
    def events_rejected(self):
        """Message field 'events_rejected'."""
        return self._events_rejected

    @events_rejected.setter
    def events_rejected(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'events_rejected' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'events_rejected' field must be an unsigned integer in [0, 4294967295]"
        self._events_rejected = value

    @builtins.property
    def seconds_to_next_auto_event(self):
        """Message field 'seconds_to_next_auto_event'."""
        return self._seconds_to_next_auto_event

    @seconds_to_next_auto_event.setter
    def seconds_to_next_auto_event(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'seconds_to_next_auto_event' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'seconds_to_next_auto_event' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._seconds_to_next_auto_event = value
