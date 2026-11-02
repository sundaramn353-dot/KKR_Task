import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sundar/Downloads/whatsapp/diwali_ros2_ws/install/diwali_festival'
