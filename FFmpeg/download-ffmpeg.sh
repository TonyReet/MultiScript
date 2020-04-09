#!/bin/bash
source="ffmpeg-4.0"
if [ ! -r $source ]
then
    echo "没有FFmpeg库，需要下载..."
    curl https://ffmpeg.org/releases/${source}.tar.bz2 | tar xj || exit 1
fi
