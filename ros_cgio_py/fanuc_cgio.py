
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

# author: G.A. vd. Hoorn (TU Delft Robotics Institute)


import json
import requests


class FanucCGIOException(Exception):
    pass


# from kliotyps.kl
class PortTypes(object):
    DIN        =  1   # Digital input
    DOUT       =  2   # Digital output
    ANIN       =  3   # Analog input
    ANOUT      =  4   # Analog output
    TOOL       =  5   # Tool output
    RDI        =  8   # Robot digital input
    RDO        =  9   # Robot digital output
    GPIN       = 18   # Grouped inputs
    GPOUT      = 19   # Grouped outputs


BASE_URL='KAREL'

PROG_NAME='ros_cgio'

OP_READ='read'
OP_WRITE='write'

ARG_OP='io_op'
ARG_TYPE='io_type'
ARG_IDX='io_idx'
ARG_VAL='io_val'

JSON_RESULT='result'
JSON_OP='op'
JSON_TYPE='type'
JSON_IDX='idx'
JSON_VALUE='value'
JSON_SUCCESS='success'
JSON_ERROR='error'
JSON_REASON='reason'


class FanucCGIO(object):
    def __init__(self, robot_host):
        self.robot_host = robot_host
        self.url = 'http://{ip}/{base}/{prog}'.format(ip=self.robot_host,
            base=BASE_URL, prog=PROG_NAME)


    def __request(self, op, port_type, port_index, port_val=None):
        params = {
            ARG_OP   : op,
            ARG_TYPE : port_type,
            ARG_IDX  : port_index
        }

        if (op == OP_WRITE):
            if port_val is None:
                raise FanucCGIOException("Need a value to write ..")
            params[ARG_VAL] = port_val

        r = requests.get(self.url, params=params)
        if r.status_code != requests.codes.ok:
            raise FanucCGIOException("Controller web server returned an "
                "error: {0}".format())
        if 'Unable to run' in r.text:
            raise FanucCGIOException("Error: ROS_CGIO Karel program cannot"
                " be started on controller.")
        return r.json()


    def read(self, port_type, index):
        ret = self.__request(OP_READ, port_type, index)
        if ret[JSON_RESULT] != JSON_SUCCESS:
            raise FanucCGIOException("Read error: " + ret[JSON_REASON])
        return int(ret[JSON_VALUE])


    def write(self, port_type, index, val):
        ret = self.__request(OP_WRITE, port_type, index, val)
        if ret[JSON_RESULT] != JSON_SUCCESS:
            raise FanucCGIOException("Write error: " + ret[JSON_REASON])
        ret_val = int(ret[JSON_VALUE])
        if ret_val != val:
            raise FanucCGIOException("Write error: unexpected: {0} != {1}"
                .format(ret_val, val))


    def read_ain(self, index):
        return self.read(PortTypes.ANIN, index)


    def read_aout(self, index):
        return self.read(PortTypes.ANOUT, index)


    def read_din(self, index):
        return self.read(PortTypes.DIN, index)


    def read_dout(self, index):
        return self.read(PortTypes.DOUT, index)


    def read_robot_din(self, index):
        return self.read(PortTypes.RDI, index)


    def read_robot_dout(self, index):
        return self.read(PortTypes.RDO, index)


    def read_gpin(self, index):
        return self.read(PortTypes.GPIN, index)


    def read_gpout(self, index):
        return self.read(PortTypes.GPOUT, index)


    def write_aout(self, index, val):
        if type(val) == float:
            raise FanucCGIOException("Float analogue values currently not supported")
        return self.write(PortTypes.ANOUT, index, val)


    def write_dout(self, index, val):
        return self.write(PortTypes.DOUT, index, val)


    def write_robot_dout(self, index, val):
        return self.write(PortTypes.RDO, index, val)


    def write_gpout(self, index, val):
        return self.write(PortTypes.GPOUT, index, val)
