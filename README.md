This script turns the single TXT file outputs of a VoxCAD simulation that were 
recorded subsequently for one ongoing simulation into one CSV file.

To use this program, clone this repository and then create other directories
within the original directory, containing all the files belonging to the respective simulations. 
The structure should look similar to this:

```
\Stitching
    stitch.py
    \model_1
        1.txt
        2.txt
        3.txt
        ...
    \model_2
        ...
```

Then open a terminal within the "Stitching" directory and run `python3 stitch.py model_1`, which 
specifies that the code stitches together the files found in the directory "model_1", or
run only `python3 stitch.py`, which instead takes the directory specified in line 32 of the script.

The CSV file will be saved as "results.csv" in the respective directory.