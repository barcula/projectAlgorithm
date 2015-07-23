## Abstract
In the first topic of the seminar was the exploration of the concept of algorithms. We build a list of instructions for People to execute with pen and paper with the intention to transform these results into a digital form. 

![Analog Example] (http://54593925.swh.strato-hosting.eu/web/fh-potsdam/input-output/weblog/img/algorithm/01/05.jpg)

The core of the analog version of the algorithm is the generation of random wax drops on a paper based on the age of the executing person. The contours around these drops shall end up in a organic overlaying grid which mesmerizes the viewer. 

![Random Wax Drops] (http://54593925.swh.strato-hosting.eu/web/fh-potsdam/input-output/weblog/img/algorithm/03/blobs.gif)

The digital result is a realized with python in processing and the openCV library. 

![Final Result] (http://54593925.swh.strato-hosting.eu/web/fh-potsdam/input-output/weblog/img/algorithm/03/contoursAnim.gif)

## Prerequisite
In Order to run the sketches and create some organic blobs you only need to add a couple of things

+  Download and install [Processing] (https://www.processing.org/download/)
+  Add Python Mode via the Mode Manager

## Dependencies
The OpenCV Library is responsible for the detection of the random generated blobs and has to be installed.

+ Download the [OpenCV Library] (http://ubaa.net/shared/processing/opencv/) unzip it and put it into your processing libraries folder.

## Installation
To run the project, clone the code folder with git to your local machine.

## Usage
The project contains two python sketches. **createBlobs** is emulating the generation of a random amount of wax drops and saves a an image into the folder. Run the sketch in processing to generate some images.

In the second step take one image and put it into the **findContours** folder and rename the file to **blobs.jpeg**

Inside the code you can set the number of drawn polygons by changing the number i counts up to in line 37.

## Contact
Uf you have a question write me an email [mail@fabiandinklage.com] (mailto:mail@fabiandinklage.com).

## License
if not further noticed
Copyright (c) 2015 Fabian Dinklage

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For further information click [here] (http://opensource.org/licenses/mit-license.php)




