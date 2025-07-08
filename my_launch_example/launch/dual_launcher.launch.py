from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir

def generate_launch_description():

    launch_1 = IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(),"/talker_listener.launch.py"]),
        launch_arguments={
            "chatter_topic": "chatter_modified"
        }.items(),
        )

    launch_2 = IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(),"/other_talker_listener.launch.py"]),
        launch_arguments={
            "chatter_topic": "other_chatter_modified"
        }.items(),
        )
    
    launch_files = [launch_1, launch_2]
    return LaunchDescription(launch_files)
