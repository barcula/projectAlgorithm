## Abstract
The second experiment deals with BioCpomputing. The object of desire is the slime mould [Physarum Polycephalum] (https://en.wikipedia.org/wiki/Physarum_polycephalum). We made different sorts of experiments observing the growth of the slime mold. In the next Step, we set up a Raspberry Pi with a webcam to capture the growth of the mold for at least 12 Hours. 

The target of the project was to use the growth of the slime mold as some sort of input data to generate a visual output, which visualizes the behavior on chosen parameters.

The Idea is to orientate on the shape of the organic shapes which resulted in the first project. The analysis of the video material ist based on the number of bright pixels counted in every taken picture of the slime mold and the data basis for the final animation of the slime mold. 

The geometric elliptical shape is based on the **superformula**, which is invented 1997 to generalize all kinds of elliptical forms an describes the animation. The dataset transforms transforms the ellipsis over time and thus visualizes the growth of the slime mold.
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




