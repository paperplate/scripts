#!/bin/bash

# Check if input and output paths are provided
if [ $# -lt 2 ]; then
  echo "Usage: $0 <inputFile> <outputFile>"
  exit 1
fi

# Extract input arguments into variables
inputFile="$1"
outputFile="$2"

# Convert input to output and copy all subtitle streams
ffmpeg -i "$inputFile" -c:v libaom-av1 -c:v hevc_nvenc -map 0 -c:s copy "$outputFile"
