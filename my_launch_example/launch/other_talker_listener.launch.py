from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    topic_arg = LaunchConfiguration('chatter_topic')

    return LaunchDescription([
        DeclareLaunchArgument(
            'chatter_topic',
            default_value='other_chatter',
            description='Topic name for talker and listener nodes'
        ),
        DeclareLaunchArgument(
            'start_listener',
            default_value='true',
            description='Whether to launch the listener node or not'
        ),
        Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='my_other_talker',
            remappings=[('/chatter', topic_arg)]
        ),

        Node(
            package='demo_nodes_cpp',
            executable='listener',
            name='my_other_listener',
            remappings=[('/chatter', topic_arg)],
            condition=IfCondition(LaunchConfiguration('start_listener'))
        )

    ])