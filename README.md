# Sticker-pack-for-redbubble
Create perfectly distanced sticker packs for redbubble with 5 images

<img src="https://user-images.githubusercontent.com/60852205/151411329-d53e3ebc-b022-428f-b506-2ff4c0b8f4f9.png" width=200>

GUI included

![image](https://user-images.githubusercontent.com/60852205/151411389-f747a3eb-d339-4d06-8bfa-6cb9950180f1.png)

# Installation

Requires Python 3+
pip is a package-management. Starting with Python 3.4, it is included by default with the Python binary installers.

Run this commands through CMD or Bash

```pip install PySimpleGUI```

```pip install Pillow```

# Usage

Run ```stickerPack.pyw```

You can run it through CMD or Bash with this command
```python3 stickerPack.pyw```

- Browse and select 5 images (PNG and JPG surely supported)
- Set width and height of canvas (better if squared)
- Browse and select a folder where to output the pack
- Write the name wanted for the pack
- Click ```Generate```

Enjoy!

# Notes
- The extension of the script is ```pyw``` since no CLI is needed
- The coordinates where the images are placed are based on canvas size
- There is a variable distance between each image based on canvas size
  - You can reduce or increase it by changing line #36 and #37
  - ![image](https://user-images.githubusercontent.com/60852205/151418237-7039720d-2576-41d6-a1ba-1c9f44ff8f11.png)
  - The more you divide the less are distanced, and the other way around if you decrease the division factor
  - The image distance is not exactly tested, feel free to open an issue to change it for everyone
