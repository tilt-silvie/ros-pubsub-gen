#!/bin/sh

python3 ../../ros-pubsub-gen/ros-pubsub-gen.py pubsub.yaml python > script/pubsub.py
python3 ../../ros-pubsub-gen/ros-pubsub-gen.py pubsub.yaml markdown > docs/pubsub.md
