from PIL import Image
import numpy as np


def detect_grayscale(image_path, tolerance=10, threshold=0.70):
    with Image.open(image_path) as img:

        m = img.mode
        if m == 'L':
            return {
                'mode': m,
                'grayscale': True
            }

        ### splitting b,g,r channels
        r, g, b = img.split()

        ### PIL to numpy conversion:
        r = np.array(r).astype(int)
        g = np.array(g).astype(int)
        b = np.array(b).astype(int)

        ### getting differences between (b,g), (r,g), (b,r) channel pixels
        r_g=np.absolute(np.subtract(r, g))
        r_b=np.absolute(np.subtract(r, b))
        g_b=np.absolute(np.subtract(g, b))

        ### get image size:
        width, height = img.size

        ### get total pixels on image:
        totalPixels = width * height

        rgratio=len(r_g[r_g <= tolerance])/totalPixels
        rbratio=len(r_b[r_b <= tolerance])/totalPixels
        gbratio=len(g_b[g_b <= tolerance])/totalPixels

        result = False
        if rgratio>threshold and rbratio>threshold and gbratio>threshold:
            result = True

        return {
            'ratio': {
                'rg': rgratio,
                'rb': rbratio,
                'gb': gbratio,
            },
            'tolerance': tolerance,
            'threshold': threshold,
            'mode': m,
            'grayscale': result
        }
