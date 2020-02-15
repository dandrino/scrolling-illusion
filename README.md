# Scrolling Illusion Generator

## The Illusion

Stare at the center of the following image such that the gradient bars are in
your peripheral vision. You should see the sides lighten and darken as the
scrolling lines change direction.

<p align="center">
  <img src="output.gif"
</p>

## How to Generate

Requires Python 3 and ImageMagick

```bash
pip3 install -r requirements-pip3.txt

bash ./create_gif.sh
```

This will output the final result as `output.gif`. You can inspect individual
frames in the `generated_frames/` directory. The core generation logic is in
`generator.py`.
