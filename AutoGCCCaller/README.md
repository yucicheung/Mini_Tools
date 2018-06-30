# Auto GCC Caller

## Introduction
An easy shell script to call G++ compiler in Linux for releasing you from typing long commands each time to run the C++ programs.

 Only the basic operations are implemented in this file, by basic operations I mean:
- Call the g++ compiler to compile the specific `.cpp` file, where the standard follows c++11, you are able to change the setting by modifing the script.
- Name the runnable output file using the same name as that of `.cpp` file, say your cpp filename is `cppname.cpp`, the outputfile will be `cppname.out`.
- Run the output file.

## Usage
```shell
autorun.sh yourfile.cpp
```
Usually after downloading, it's already an executable file. 
However if it's not, run `chmod +x autorun.sh` to make it executable.

## More
You can always modify the code to make it fit your needs.

