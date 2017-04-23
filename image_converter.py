#!/usr/bin/env python

import shlex
import os
import argparse
import subprocess


def converter(dimensions):
    size = dimensions

    def process(images):
        if not isinstance(images, list):
            images= [images]

        for image in images:
            cmd = 'convert -resize {} {} {}'.format(size,
                                                    image,
                                                    os.path.split(image)[1])

        subprocess.check_call(shlex.split(cmd))

    return process

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', help='size of images: ie. 1920x1080')
    parser.add_argument('-i', '--images', nargs='+', help='list of images')

    args = parser.parse_args()

    image_converter = converter(args.size)
    image_converter(args.images)
