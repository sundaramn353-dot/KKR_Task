"""Stage 1/2: Gazebo Harmonic + Diwali street world, optionally with the festival manager."""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import AppendEnvironmentVariable, DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression


def generate_launch_description():
    sim = get_package_share_directory('diwali_sim')
    world = os.path.join(sim, 'worlds', 'diwali_street.sdf')
    headless = PythonExpression(["'-s --headless-rendering' if '", LaunchConfiguration('headless'),
                                 "' == 'true' else ''"])
    return LaunchDescription([
        DeclareLaunchArgument('festival', default_value='false',
                              description='Also start festival_manager (fireworks/lighting/sound)'),
        DeclareLaunchArgument('autonomous', default_value='true',
                              description='Mode A: fireworks fire automatically (needs festival:=true)'),
        DeclareLaunchArgument('sound', default_value='true'),
        DeclareLaunchArgument('headless', default_value='false', description='Run gz server only'),
        AppendEnvironmentVariable('GZ_SIM_RESOURCE_PATH', os.path.join(sim, 'models')),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('ros_gz_sim'),
                                                       'launch', 'gz_sim.launch.py')),
            launch_arguments={'gz_args': ['-r ', world, ' ', headless], 'on_exit_shutdown': 'true'}.items()),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('diwali_festival'),
                                                       'launch', 'festival.launch.py')),
            launch_arguments={'autonomous': LaunchConfiguration('autonomous'),
                              'sound': LaunchConfiguration('sound'),
                              'lights_file': os.path.join(sim, 'config', 'festival_lights.yaml')}.items(),
            condition=IfCondition(LaunchConfiguration('festival'))),
    ])
