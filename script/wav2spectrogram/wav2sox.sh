#!/bin/bash    
FILES=*.wav
    for f in $FILES
    do
        #echo ${f%%.*}
        sox $f -n spectrogram -o ${f%%.*}.png
    done

    