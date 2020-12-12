## toPNG

toPNG is a python script that turns the white elements of a image into a PNG with a transparency layer.

### Running it:

The script takes in three arguments.
* Path to the input file
* Path to the output file
* Sensibility(optional): A value from 0 to 255 to determine how whitish an element has to be in order to be turned transparent. 255 would imply only pure whites are turned transparent.
* It also has a -h help command, which will explain  the arguments needed to run the script.

![terminal](images/terminal.jpg)


### Examples:

Input image:

![input](images/logo.jpg)

Outputs: The following are jpgs made to exemplify the transparency, the real pngs are inside the image folders and can be downloaded.

240 sensibility:

![output1](images/example1.jpg)

250 sensibility:

![output2](images/example2.jpg)

255 sensibility:

![output3](images/example4.jpg)
