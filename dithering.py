from dataclasses import dataclass
from typing import Tuple
# import sys
from os import mkdir
from PIL import Image, ImageDraw


@dataclass
class Color:
    r: int
    g: int
    b: int


# Pallete B&W
PALLETE_BW = [
    Color(0, 0, 0),
    Color(255, 255, 255)
]

# Pallete 1
PALLETE_1 = [
    Color(190, 0, 57),
    Color(255, 69, 0),
    Color(255, 168, 0),
    Color(255, 214, 53),
    Color(0, 163, 104),
    Color(0, 204, 120),
    Color(126, 237, 86),
    Color(0, 117, 111),
    Color(0, 158, 170),
    Color(36, 80, 164),
    Color(54, 144, 234),
    Color(81, 233, 244),
    Color(73, 58, 193),
    Color(106, 92, 255),
    Color(129, 30, 159),
    Color(180, 74, 192),
    Color(255, 56, 129),
    Color(255, 153, 170),
    Color(109, 72, 47),
    Color(212, 215, 217),
    Color(156, 105, 38),
    Color(0, 0, 0),
    Color(137, 141, 144),
    Color(255, 255, 255),
]


def calc_distance(color1: Color, color2: Color):
    """Calculate the euclidean distance between two colors."""
    return ( (color1.r - color2.r)**2 + (color1.g - color2.g)**2 + (color1.b - color2.b)**2 )**0.5


def get_nearest_color(old_color: Color, pallete=PALLETE_BW):
    """Find the nearest color to the original color present in the selected color pallete."""
    distance = 500  # max distance between colors in the RGB space is 441.6 (black and white)
    nearest_color = Color(0, 0, 0)
    
    for color in pallete:
        new_distance = calc_distance(old_color, color)
        
        if new_distance < distance:
            distance = new_distance
            nearest_color = color

    return nearest_color


def pixel_to_color(pixel: Tuple[int, int, int]):
    return Color(pixel[0], pixel[1], pixel[2])


def color_to_pixel(color: Color):
    return (color.r, color.g, color.b)


def add_colors(color1: Color, color2: Color):
    """Two color addition."""
    return Color(
        color1.r + color2.r, 
        color1.g + color2.g, 
        color1.b + color2.b
    )


def multiply_color(color: Color, value: float):
    """Multiply a color by a value."""
    return Color(
        round(color.r * value), 
        round(color.g * value),
        round(color.b * value)
    )


def render(image: Image, output: str = 'imgout.png'):
    """Render a new image applying Floyd-Steinberg dithering."""
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            color = pixel_to_color(pixel)
            new_color = get_nearest_color(color, pallete=PALLETE_1)

            draw = ImageDraw.Draw(image)
            draw.point((x, y), color_to_pixel(new_color))

            quant_error = Color(
                color.r - new_color.r,
                color.g - new_color.g,
                color.b - new_color.b
            )

            if (x + 1 < image.width and y + 1 < image.height):

                temp_pixel = image.getpixel((x + 1, y))
                temp_color = pixel_to_color(temp_pixel)
                draw.point(
                    (x + 1, y), 
                    color_to_pixel( add_colors(temp_color, multiply_color(quant_error, 7/16)) )
                )

                temp_pixel = image.getpixel((x - 1, y + 1))
                temp_color = pixel_to_color(temp_pixel)
                draw.point(
                    (x - 1, y + 1), 
                    color_to_pixel( add_colors(temp_color, multiply_color(quant_error, 3/16)) )
                )

                temp_pixel = image.getpixel((x, y + 1))
                temp_color = pixel_to_color(temp_pixel)
                draw.point(
                    (x, y + 1), 
                    color_to_pixel( add_colors(temp_color, multiply_color(quant_error, 5/16)) )
                )

                temp_pixel = image.getpixel((x + 1, y + 1))
                temp_color = pixel_to_color(temp_pixel)
                draw.point(
                    (x + 1, y + 1), 
                    color_to_pixel( add_colors(temp_color, multiply_color(quant_error, 1/16)) )
                )

    image.save(output)


def main():
    img_path = 'images/boat.webp'
    
    with Image.open(img_path) as image:
        render(image, output='imgout2.png')


if __name__ == '__main__':
    main()
