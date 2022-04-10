# image-dithering
 
A script to apply color restriction to images. Uses the Floyd-Steinberg dithering algorithm.

## Usage

To process an image:

```
$ python color-restriction.py .\images\car.jpg --pallete Reddit
```

To apply color restriction without dithering:

```
$ python color-restriction.py .\images\car.jpg --pallete Reddit --no-dithering
```

## Examples

Color pallete restriction with dithering:

| Original image | With dithering |
|-----------------------------------|--------------------------------|
| ![original](examples/jeep.jpg) | ![dithering](examples/jeep-Reddit-dithering.jpg)


Color pallete restriction without dithering:

| Original image | Without dithering |
|-----------------------------------|--------------------------------|
| ![original](examples/jeep.jpg) | ![no dithering](examples/jeep-Reddit.jpg) |


Color restriction to black and white:

| Without dithering | With dithering |
|-----------------------------------|--------------------------------|
| ![b&w no dithering](examples/jeep-B&W.jpg) | ![b&w dithering](examples/jeep-B&W-dithering.jpg) |


Other samples:

| Original image | With dithering |
|-----------------------------------|--------------------------------|
| ![original](examples/train.jpg) | ![dithering](examples/train-Reddit-dithering.jpg) |
| ![original](examples/cityscape.jpg) | ![dithering](examples/cityscape-Reddit-dithering.jpg) |
| ![original](examples/landscape.jpg) | ![dithering](examples/landscape-Reddit-dithering.jpg) |

More in the `examples/` folder.