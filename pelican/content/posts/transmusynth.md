Title: Behold, the TransmuSynth!
Category: Blog
Tags: coding,  
Date: 2026-04-13
Author: John Beers
Summary: Documenting the evolution of a creative "media alchemy" tool 

### The beginning: image2sound

Back in January 2023, I made the first commits of a tool I called **[image2sound](https://codeberg.org/jaerrib/image2sound)**. The premise was simple: I wanted to use the color values from a user-supplied image, convert them to various frequencies, and output a WAV file. To build that very basic CLI tool, I learned a little about argparse, numpy, and wavio.

Here's that first iteration, in all its humble glory:

```python
from PIL import Image
import numpy as np
import wavio
import argparse


def image_to_array(save_path):
    img = Image.open(save_path).convert(mode="RGB")
    img_arr = np.asarray(img, dtype='int64')
    return img_arr


def rgb_to_frequency(r, g, b):
    freq = (r * g * b) / 829.06875
    return freq


def array_to_sound(array):
    temp_array = []
    for x in array:
        for y in x:
            red = y[0]
            green = y[1]
            blue = y[2]
            freq = rgb_to_frequency(red, green, blue)
            tone = np.sin(2 * np.pi * freq)
            temp_array.append(tone)
    return temp_array


def save_wav(save_path, array):
    rate = 22050
    split_test = save_path.split(".")
    file_name = split_test[0]+".wav"
    wavio.write(file_name, array, rate, sampwidth=4, scale=2, clip="ignore")
    print("Saved file as ", file_name)


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str)
args = parser.parse_args()
path = args.path
image_array = image_to_array(path)
sound_array = array_to_sound(image_array)
save_wav(path, sound_array)
```

I began to add more features over time which would give the user more control over the output. By the time version 0.5 came out, you could specify a musical key, how long you wanted the tracks to be, and export stereo audio. There were some bugs, of course, such as the distinctive "click" each time a note was sounded. It was usable, though, and over the course of the year, I released several works under the name **[PLACEB0_BUTT0N](https://placebobutton.bandcamp.com/)** to demonstrate what could be done with it. I was also ecstatic that the project had its first external contributor in gregroni (Gregor Niehl)!

As my knowledge of Python grew, image2sound grew as well. Version 0.7 finally removed the characteristic "clickiness" by adding Blackman smoothing, and version 0.8 added the ability to specify a time signature. By the time 0.9 rolled around, a "quartet mode" was added to map CMYK images to the instruments associated with a string quartet (i.e., two violins, viola plus cello). Different waveforms were added, which allowed users to select sawtooth or square waves instead of being limited to the original sine waves, and envelope filters let them choose from several attack and decay presets.

The biggest evolution of image2sound came when I opted to expand into MIDI exporting alongside a composition engine. The former allowed a wider range of sounds to be used via applications like [MuseScore](https://musescore.org/) or [LMMS](https://lmms.io/), while the latter allowed movements to be defined in terms of phrases and sections.

For example:

```python
movement_type = {
    "sonata": {
        "phrases": [
            {"label": "A", "length": 16},
            {"label": "B", "length": 12},
            {"label": "C", "length": 6},
            {"label": "D", "length": 12},
            {"label": "E", "length": 8},
            {"label": "F", "length": 6},
            {"label": "G", "length": 12},
            {"label": "H", "length": 12},
            {"label": "I", "length": 4},
            {"label": "J", "length": 4},
        ],
        "sections": [
            {"label": "Exposition", "sequence": ["A", "B", "C", "D"]},
            {"label": "Development", "sequence": ["E", "F", "C", "F", "E"]},
            {"label": "Recapitulation", "sequence": ["G", "H", "C", "D"]},
            {"label": "Coda", "sequence": ["I", "J"]},
        ],
    },
}
```

There's been more refinement, bug fixes, and other improvements. However, this is only half of the story.

### Part 2: prompt2pixel

In April 2024, I began working on another tool. Although less ambitious, it was still based on things changing form, but this time, it was converting text prompts into images. I don't mean this in a generative AI sense; it's all done algorithmically. I got the idea from an Elixir tutorial I did that generated GitHub-style avatars from usernames via cryptographic hashes. That said, calling the tool **[prompt2pixel](https://codeberg.org/jaerrib/prompt2pixel)** might be misleading to some people.

Anyway, the basic premise is:

1. the user provides text input
2. that text is encoded as a cryptographic hash *(not for security, just deterministic mapping)*
3. the hex pairs from the hash are converted to RGB values
4. those RGB values are used to generate the pixels of a small image
5. the created image is enlarged to a desired size
6. finally, the image is saved to a file

Of course, I expanded it with more features to fit my needs. I added CMYK support, swapping user input with random sentences via [wonderwords](https://pypi.org/project/wonderwords/), remapping colors from .gpl palette files, and multiple hash types. I also used salts as the basis of video generation. If the user provides a FPS value and a desired video length, the tool calculates the total number of frames needed. While looping through the image generation, the index is used to salt the original text, which modifies the output. When the final video is viewed, these subtle changes create a sort of animation. Granted, it's abstract and more akin to 90s-style visualizers, but the effect is pretty cool.

### Bringing it all together

The original idea for **TransmuSynth** was simply to combine both of these into a single CLI tool. Being able to supply text that would go through various changes to arrive at a piece of music appealed to my sense of creativity. In fact, I actually started to build it that way. However, having the user go through various text prompts to select parameters made for a less than stellar experience. So, I scrapped the entire thing and started building it as a Flask app.

Why did I use Flask? Both tools were originally written Python, and I knew I wanted to have a GUI of some sort. I briefly entertained the idea of building a desktop app. However, I'm more familiar with web dev and wanted to build something quicker instead of fussing around with other toolkits. Being able to deploy it on a server would let people check out what I was working on without needing to download or install anything, which effectively made it cross-platform as a bonus. Django was going to be too much for a small project like this, so I ended up with Flask.

Since I was already familiar with feeding the output of prompt2pixel into image2sound, the conversion to Flask was relatively easy. An initial complication came about from needing to work with user uploads for source images and color palettes without saving them to a database. Having worked through that, I also wanted to limit features that would make it less cost-effective to deploy the app on a free / pay-as-you-go provider like Fly.io (e.g., WAV and video files). For anyone wanting to run the app locally, there are config settings to turn some of those features back on while other, less used features were simply stripped out.

### Conclusion

Building my own creative tools has been a rewarding experience. I've learned a lot about cryptography and audio / image processing with Python while extending my web development skills. I'm still adding user-controlled features that had been previously hard-coded, such as instrument selection, panning, etc. If you're interested in seeing the source code or trying a demo of the app, check out the following links:

- [Source code on Codeberg](https://codeberg.org/jaerrib/TransmuSynth)
- [Demo on Fly.io](https://transmusynth.fly.dev/)

---

**Note:** I plan on writing a follow-up post with more details about how I'm using TransmuSynth alongside other opensource tools in my own music projects. 



