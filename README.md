# image_converter
Python module for resizing images

Requires ImageMagick 6.x or higher installed. 

Module will resize images according to specified dimensions.<br />
Ie. convert_to_1080 = image_converter.converter('x1080')<br />
convert_to_1080(['image1', 'image2'])<br />
convert_to_square_100 = image_converter.converter('100x100') <br />
convert_to_square_100('image_100_100')


## Usage as a script <br />
python image_converter.py -s x1080 -i /image_dir/*

