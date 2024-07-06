# ROS tutorial
Remember to delete build and devel folder each time you pull from the repository

# Commands

## create ROS workspace
1. create workspace folder
```sh
mkdir -p <workspace_mame>/src
```
2. move inside workspace
```sh
cd <workspace_mame>
```
3. buil the env
```sh
catkin_make
```
### create ROS package
Inside src
```sh
cd <workspace_mame>/src
```
```sh
catkin_create_pkg <pkg_name> [dependencies]
```


## Run ROS node
```sh
rosrun <pkg_name> <node.py>
```

## Show Topic
``` sh
rostopic list
```
## Listen a Topic
```sh
rostopic echo \<topic_name>
```