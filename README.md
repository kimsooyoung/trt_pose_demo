# trt_pose_demo

# links

https://github.com/NVIDIA-AI-IOT/ros2_trt_pose
https://github.com/NVIDIA-AI-IOT/trt_pose
https://github.com/NVIDIA-AI-IOT/torch2trt
https://github.com/NVIDIA-AI-IOT/jetcam

## Install All Dependencies for trt_pose

```
git clone https://github.com/kimsooyoung/trt_pose_demo.git
cd trt_pose_demo/Setup
./trt_pose_setup.sh
```

## Install All Dependencies for ROS 2 & Build ros2_trt_pose

```
./ros2_setup.sh
```

## Run once for optimized model creation
 
For more efficient processing, trt_pose requires trt optimized model.
And you can create them easily by runnig provided rosnode once.

```
cd ros2_seminar_ws/
roseloq
ros2 run ros2_trt_pose pose-estimation --ros-args -p base_dir:='/home/<your-username>/Downloads/trt_pose/tasks/human_pose'
```

Goto base_dir, there'll be optimized model named with `<model-name>_trt.pth`

## Execute

Before launching, you'll need to edit base_dir for your env.
Open pose-estimation.launch.py then edit 'base_dir' to your folder contains model files.

```
    trt_pose_node = Node(
            package="ros2_trt_pose",
            node_executable="pose-estimation",
            node_name="pose_estimation",
            output="screen",
            parameters = [{
                'base_dir':'/home/rb-nano/Downloads/trt_pose/tasks/human_pose',
                'model': 'resnet18',
                'point_range' : 10,
                'show_image' : False,
                }],
            )
```

Lastly, Execution!!!

```
cd ros2_seminar_ws/
roseloq
ros2 launch ros2_trt_pose pose-estimation.launch.py
```
