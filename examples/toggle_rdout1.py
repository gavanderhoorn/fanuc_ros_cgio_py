#!/usr/bin/env python

# Copyright (c) 2016, TU Delft Robotics Institute
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# A simple example showing how to use the FanucCGIO Python class to
# interact with the ROS_CGIO Fanuc Karel program on a controller.
#
# author: G.A. vd. Hoorn (TU Delft Robotics Institute)

from ros_cgio_py import FanucCGIO

import time


if __name__ == "__main__":
    # configure either hostname or ip (but hostname will need a working
    # dns server setup)
    robot = FanucCGIO('localhost')

    # get current state
    rdout1 = robot.read_robot_dout(1)
    print ("RDOUT[1] is currently {0}".format('ON' if rdout1 == 1 else 'OFF'))

    # start toggling
    print ("Toggling RDOUT[1] at 1 Hz, press ctrl+c to stop ..")
    while True:
        robot.write_robot_dout(1, (robot.read_robot_dout(1) ^ 1))
        time.sleep(1.0)
