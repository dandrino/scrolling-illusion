import numpy as np
from PIL import Image

def main():
  shape = (1280, 720)
  width, height = shape

  inverted = False

  num_gradient_bars = 10
  gradient_bar_size = height / num_gradient_bars
  xcoord, ycoord = np.meshgrid(*map(np.arange, shape))

  def fmod(a, b): return b * ((a / b) - np.floor(a / b))

  def generate_gradient_bars(offset=0):
    return fmod(ycoord + offset, gradient_bar_size) / gradient_bar_size

  mask = np.abs(xcoord - width / 2) < width * 0.2
  if inverted: mask = 1 - mask
  bg = generate_gradient_bars()

  dt = 1.0 / 60

  bar_period_sec = 0.1
  bar_period_frames = int(np.round(bar_period_sec / dt))

  waterfall_period_sec = 4.0
  waterfall_period_frames = int(np.round(waterfall_period_sec / dt))

  lcm = lambda a, b: a * b // int(np.gcd(a, b))
  total_frames = lcm(bar_period_frames, waterfall_period_frames)

  for frame in range(total_frames):
    print("Generating frame %d / %d" % (frame + 1, total_frames))

    t = frame * dt

    waterfall_dir = np.sign(np.sin(2 * np.pi * t / waterfall_period_sec))

    fg = generate_gradient_bars(
        waterfall_dir * gradient_bar_size * t / bar_period_sec) > 0.25

    result = bg * (1 - mask) + fg * mask

    path = 'generated_frames/%05d.png' % (frame,)
    img = Image.fromarray(255 * result).convert('RGB')
    img.save(path)

if __name__ == '__main__':
  main()
