# ROS Tutorial
This code in this repository is took from youtube course at this [link](https://youtu.be/C6BlNbeU3fQ?si=p6g8Fy_C7PBTyWP0)
> [!NOTE]
> Remember to delete build and devel folder each time you pull from the repository


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
3. build the Workspace
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
>[!NOTE]
> every time we add a folder inside our Workspace we need to rebuild the Workspace
### Add python files
if  you place all your python files inside `scripts` folder, inside CMakeList.txt inside your package add these code line before #BUILD# block
```
file(GLOB SCRIPTS scripts/*.py)
catkin_install_python(PROGRAMS ${SCRIPTS}
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
```
>[!IMPORTANT]
> Make sure after build the env. with `catkin_make` inside devel/lib/<pkg_name> will be present all the python files also present in `scripts` folder



### Source the environment
1. inside root project folder
```sh
source devel/setup.bash
```

### Run Master ROS node
```sh
roscore
```
> [!NOTE]
> ROS master need to be awake to allow the comunication, you must keep its terminal open, to run other node sumply open new terminal

## Run ROS node
>[!IMPORTANT]
> ROS MASTER must we awake
```sh
rosrun <pkg_name> <node.py>
```
## Launch File
### Structure 
```xml
<launch>
    <node pkg="pkg_name" type="node_name1.py" name="node_name1" output="screen"></node>
    <node pkg="pkg_name" type="node_name2.py" name="node_name2" output="screen"></node>
</launch>
```


## Run ROS launch file
roslaunch <pkg_name> <filenam>.launch
## Show Topic
``` sh
rostopic list
```
## Listen a Topic
```sh
rostopic echo \<topic_name>
```
