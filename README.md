# Dump MNIST data 

Get MNIST data and export them as png files.
Chainer is required.

## Usage

This script first creates directories from 0/ to 9/.
Then it exports data in the directory corresponding to its label.

    $ python mnist_dump.py
    7/test0000.png
    2/test0001.png
    (snip)
    6/test0098.png
    9/test0099.png

