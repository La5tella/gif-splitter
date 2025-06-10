Created by Mike LaStella c. June 2025.

# Desc

This file is a CLI program intended to grid a video or gif into tiles. This prgm is intended for use on streamdecks, specifically the VSDINSIDE Macro Keypad. It obviously has other use cases.

Indended Platform: Windows
Language: Python
Modules: Pillow, Moviepy, imageio-ffmpeg

If used, give me a shoutout! 

## Instructions

To use, place a video or .gif into the project directory. There have been two examples placed in there already. 

I would recommend running dependencies.bat beforehand. This checks for and installs the python modules needed for the program to run. If you already have everything installed, it does nothing, so no point in not checking.

After that, run the cmd:
```
python slice.py <filename> <col> <row> <outdir> <target_w> <target_h> 
```
in a terminal of the same directory.

> BEGINNERS NOTE:  Most file explorers have an option to right click and open a terminal in that directory. This is where you should run the above command. 

It will output your .gifs into the directory specified.

## Credits

Example images are from "ghythalmdadhh" on Pinterest.

All software written by Mike LaStella. You can contact me on my portfolio website at http://www.la5tella.com
