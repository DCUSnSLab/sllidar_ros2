#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # shared
    channel_type = LaunchConfiguration('channel_type', default='serial')
    serial_baudrate = LaunchConfiguration('serial_baudrate', default='460800')
    inverted = LaunchConfiguration('inverted', default='false')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')
    scan_mode = LaunchConfiguration('scan_mode', default='Standard')

    # lidar1
    lidar1_serial_port = LaunchConfiguration('lidar1_serial_port', default='/dev/ttyUSB1')
    lidar1_frame_id = LaunchConfiguration('lidar1_frame_id', default='lidar1_laser')

    # lidar2
    lidar2_serial_port = LaunchConfiguration('lidar2_serial_port', default='/dev/ttyUSB2')
    lidar2_frame_id = LaunchConfiguration('lidar2_frame_id', default='lidar2_laser')

    return LaunchDescription([
        DeclareLaunchArgument(
            'channel_type',
            default_value=channel_type,
            description='Specifying channel type of lidar'),

        DeclareLaunchArgument(
            'serial_baudrate',
            default_value=serial_baudrate,
            description='Specifying usb port baudrate to connected lidar (C1: 460800)'),

        DeclareLaunchArgument(
            'inverted',
            default_value=inverted,
            description='Specifying whether or not to invert scan data'),

        DeclareLaunchArgument(
            'angle_compensate',
            default_value=angle_compensate,
            description='Specifying whether or not to enable angle_compensate of scan data'),

        DeclareLaunchArgument(
            'scan_mode',
            default_value=scan_mode,
            description='Specifying scan mode of lidar'),

        DeclareLaunchArgument(
            'lidar1_serial_port',
            default_value=lidar1_serial_port,
            description='Serial port for lidar1'),

        DeclareLaunchArgument(
            'lidar1_frame_id',
            default_value=lidar1_frame_id,
            description='frame_id for lidar1'),

        DeclareLaunchArgument(
            'lidar2_serial_port',
            default_value=lidar2_serial_port,
            description='Serial port for lidar2'),

        DeclareLaunchArgument(
            'lidar2_frame_id',
            default_value=lidar2_frame_id,
            description='frame_id for lidar2'),

        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            namespace='lidar1',
            name='sllidar_node',
            parameters=[{'channel_type': channel_type,
                         'serial_port': lidar1_serial_port,
                         'serial_baudrate': serial_baudrate,
                         'frame_id': lidar1_frame_id,
                         'inverted': inverted,
                         'angle_compensate': angle_compensate,
                         'scan_mode': scan_mode}],
            output='screen'),

        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            namespace='lidar2',
            name='sllidar_node',
            parameters=[{'channel_type': channel_type,
                         'serial_port': lidar2_serial_port,
                         'serial_baudrate': serial_baudrate,
                         'frame_id': lidar2_frame_id,
                         'inverted': inverted,
                         'angle_compensate': angle_compensate,
                         'scan_mode': scan_mode}],
            output='screen'),
    ])
