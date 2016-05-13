#!/usr/bin/env python

#
# author: G.A. vd. Hoorn (TU Delft Robotics Institute)
#

from setuptools import setup, find_packages

setup(
    name='ros_cgio_py',
    version='0.0.1',
    packages=find_packages(),
    author='G.A. vd. Hoorn',
    author_email='g.a.vanderhoorn@tudelft.nl',
    maintainer='G.A. vd. Hoorn',
    maintainer_email='g.a.vanderhoorn@tudelft.nl',
    description=('A Python library for interfacing with the ROS_CGIO Karel'
        ' programming running on a Fanuc controller'),
    license='Apache2',
    install_requires=['requests']
)
