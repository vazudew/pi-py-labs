#!/bin/bash

#package entire py script and archive
timestamp=$(date +%Y%m%d_%H%M%S)
echo $timestamp

#package product
product=ingyo
echo $product

filename=${product}"-"${timestamp}".zip" 
echo $filename

#source files
sourceLoc='../pi-py/*'
echo $sourceLoc

ls -la $sourceLoc
#package all the files now
gzip -r $sourceLoc > $filename
