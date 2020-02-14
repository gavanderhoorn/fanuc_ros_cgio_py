# fanuc_ros_cgio_py

## Deprecated

This library and the Karel programs are deprecated.

Please see [gavanderhoorn/dominh](https://github.com/gavanderhoorn/dominh) for a replacement.

This readme and all files in this repository are kept for archival purposes only.

## Overview

This is a small Python library usable with the [fanuc_ros_cgio][] Fanuc Karel
program.

**NOTE**: this is only meant as a convenience tool for quick and incidental
external access to a controller's IO without needing to use any additional
hardware. Do not use this on production systems or in contexts where any kind
of determinism is required. The author recommends using any of the supported
fieldbuses in those cases.


## Requirements

Python 2 (this has not been written with Python 3 compatibility in mind) and
the `requests` library. If using `pip` to install, this will automatically be
resolved and taken care of.

The [fanuc_ros_cgio][] Karel program installed on the controller.

See [fanuc_ros_cgio][] for information on how to configure the controller to
allow external access to Karel programs via the web server.


## Installation

Installation is easiest with `pip` (make sure `pip` can find `git`):

```
$ (sudo) pip install git+https://github.com/gavanderhoorn/fanuc_ros_cgio_py.git
```

or, if cloned locally first:

```
$ (sudo) pip install /path/to/your/checkout
```

This should install the package in the right location.


## Example usage

In this example the robot is reachable under the `my_robot` hostname:

```python
import ros_cgio_py

my_m10ia = ros_cgio_py.FanucCGIO('my_robot')
...
dout1 = my_m10ia.read_dout(1)
...
my_m10ia.write_aout(1, 200)
...
```

See also the `examples` directory.


## Bugs, feature requests, etc

Please use the [GitHub issue tracker][].



[fanuc_ros_cgio]: https://github.com/gavanderhoorn/fanuc_ros_cgio
[GitHub issue tracker]: https://github.com/gavanderhoorn/fanuc_ros_cgio_py/issues
