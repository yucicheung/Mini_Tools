#!/bin/bash


cppname=$1
outname=${cppname%.*}
outname=$outname".out"
g++ -std=c++11 $cppname -o $outname
#g++ $cppname -o $outname
./$outname
