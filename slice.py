#!/usr/bin/env python3
import sys, os
from PIL import Image, ImageSequence
from moviepy.editor import VideoFileClip

DEFAULT_TARGET_SIZE = (480, 272)

def slice_gif(path, cols, rows, outdir, target_size):

    if os.path.splitext(path)[1] == ".mp4":
        raw = input("Converting from video. What should I make the .gif's FPS?: ")
        try:
            fps = int(raw)           # or float(raw) if you want non-integer fps
            print(f"Thanks! Converting {path} at {fps} fps.")
        except ValueError:
            print("Invalid input. Defaulting to 30 fps.")
            fps = 30
        clip = VideoFileClip(path)
        clip = clip.set_fps(fps)
        clip.write_gif("convert.gif",
            program="imageio",      # uses imageios writer
            opt="nq",               # neuQuant quantizer
            fuzz=10,                # allow 10% color difference for smaller palette
            colors=64,               # limit to 64 colors 
            fps = fps
        )
        path = "convert.gif"

    
    im = Image.open(path)
    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
    if im.size != target_size:
        frames = [f.resize(target_size, Image.LANCZOS) for f in frames]
        w, h = target_size
    else:
        w, h = im.size
    tw, th = w // cols, h // rows

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # Extract frames once
    

    for r in range(rows):
        for c in range(cols):
            x, y = c * tw, r * th
            # Crop each frame
            tiles = [f.crop((x, y, x + tw, y + th)) for f in frames]
            # Save as a new GIF
            out_path = os.path.join(outdir, f"tile_r{r}_c{c}.gif")
            tiles[0].save(
                out_path,
                save_all=True,
                append_images=tiles[1:],
                loop=0,
                duration=im.info.get("duration", 100),
            )
    print(f"Exported {cols*rows} tiles to {outdir}/")
    print("Thanks for using this application. Please consider checking out my portfolio at www.la5tella.com")

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc not in (5,7):
        print("Usage: slice_gif.py <in.gif> <cols> <rows> <outdir> <target_size>")
        sys.exit(1)
    _, path, cols, rows, outdir = sys.argv[:5]
    if argc == 7:
        try:
            tw = int(sys.argv[5])
            th = int(sys.argv[6])
            target_size = (tw,th)
        except ValueError:
            print ("Error: target width and/or height not in int.")
            sys.exit(1)
    else:
        target_size = DEFAULT_TARGET_SIZE

    slice_gif(path, int(cols), int(rows), outdir, target_size)
