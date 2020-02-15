#!/bin/bash
mkdir generated_frames 2> /dev/null
rm generated_frames/*.png 2> /dev/null
delay=1.66666  # = 100 / 60
python3 generator.py && \
  convert -delay ${delay} -loop 0 generated_frames/*.png output.gif
