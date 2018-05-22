# ros-pubsub-gen

ros-pubsub-gen is simple code generator for ROS(Robot OS).
ros-pubsub-gen generate ROS publisher and subscriber code from yaml file.

## Supported format
- Python
- Markdown (for documentation)

## Requirements
- Python3
- pip3

Python libraries
- pyyaml
- click

## Installation
```
pip3 install click pyyaml
git clone https://github.com/tilt-silvie/ros-pubsub-gen.git
```

## Usage example (generate python code)

1. Write publisher/subscriber description file in yaml.

    ``` yaml
    publishers:
        pub_0:
            topic_name: /pub_0
            topic_type: std_msgs/String
            description: This is description of pub_0

        pub_1:
            topic_name: pub_1
            topic_type: std_msgs/Int32
            description: This is description of pub_1

    subscribers:
        sub_0:
            topic_name: /sub_0
            topic_type: std_msgs/String
            description: This is description of sub_0

        sub_1:
            topic_name: sub_1
            topic_type: std_msgs/Int32
            description: This is description of sub_1
    ```

2. Generate publisher/subscriber code.

    `python3 ros-pubsub-gen/ros-pubsub-gen.py your_yaml_file_path.yaml python > pubsub.py`

3. publisher/subscriber code is generated.

    `pubsub.py`
    ``` python
    #!/usr/bin/env python
    
    # This code was generated by ros-pubsub-gen
    # https://github.com/tilt-silvie/ros-pubsub-gen
    #
    # DO NOT modify this file.
    
    import rospy
    import std_msgs.msg
    
    # publishers
    # pub_0: This is description of pub_0
    pub_0 = rospy.Publisher('/pub_0', std_msgs.msg.String, queue_size=10)
    # pub_1: This is description of pub_1
    pub_1 = rospy.Publisher('pub_1', std_msgs.msg.Int32, queue_size=10)
    
    # subscribers (varibale definition only. Instantiation is in init().)
    # sub_0: This is description of sub_0
    sub_0 = None
    # sub_1: This is description of sub_1
    sub_1 = None
    
    def init(callbacks):
        global sub_0, sub_1
    
        sub_0 = rospy.Subscriber('/sub_0', std_msgs.msg.String, callbacks['sub_0'])
        sub_1 = rospy.Subscriber('sub_1', std_msgs.msg.Int32, callbacks['sub_1'])
    
    ```
    
4. Merge with your code.

    `your_package.py`
    ``` python
    #!/usr/bin/env python
    
    import rospy
    import std_msgs
    import pubsub
    
    def callback_sub_0(data):
        print(data.data)
    
    def callback_sub_1(data):
        print(data.data)
    
    if __name__ == '__main__':
        rospy.init_node('your_package', anonymous=True)
        r = rospy.Rate(10)
    
        # pub/sub initialization
        pubsub.init({'sub_0': callback_sub_0, 'sub_1': callback_sub_1})
    
        i = 0
        while not rospy.is_shutdown():
    
            # publish something
            pubsub.pub_0.publish("Hello world")
            pubsub.pub_1.publish(rospy.get_time())
    
            i += 1
    
            r.sleep()
    
    ```
