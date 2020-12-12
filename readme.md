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

240 sensibility:

![input](images/nueva240.png)

250 sensibility:

![input](images/nueva250.png)

255 sensibility:

![input](images/nueva255.png)
