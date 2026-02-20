"""
File: stanCodoshop.py
Name: Cindy
----------------------------------------------
This program is SC101 Assignment 3 and is adapted
from Nick Parlante's Ghost assignment.

The assignment has been redesigned and extended
by Jerry Liao to fit the learning objectives of
the stanCode SC101 course.
"""

import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Computes the Euclidean color distance between a pixel's RGB values and a target mean RGB color.

    This function measures how similar a pixel is to a reference color by treating the
    red, green, and blue channels as coordinates in a 3D color space. A smaller distance
    indicates a closer color match.

    Parameters:
        pixel (Pixel): The pixel whose RGB components (pixel.red, pixel.green, pixel.blue)
            will be compared.
        red (int): The reference mean red value.
        green (int): The reference mean green value.
        blue (int): The reference mean blue value.

    Returns:
        float: The Euclidean distance between the pixel's RGB values and the reference color.
    """
    red_difference = red - pixel.red
    green_difference = green - pixel.green
    blue_difference = blue - pixel.blue
    sum_squares = (red_difference ** 2) + (green_difference ** 2) + (blue_difference ** 2)
    dist = math.sqrt(sum_squares)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    total_red = sum(pixel.red for pixel in pixels)
    total_green = sum(pixel.green for pixel in pixels)
    total_blue = sum(pixel.blue for pixel in pixels)

    # for pixel in pixels:
    #     # total_red += pixel.red
    #     total_green += pixel.green
    #     total_blue += pixel.blue

    avg_red = total_red // len(pixels)
    avg_green = total_green // len(pixels)
    avg_blue = total_blue // len(pixels)

    return [avg_red, avg_green, avg_blue]



def get_best_pixel(pixels):
    """
    Selects the pixel that is closest in color to the average color of a group of pixels.

    This function examines a list of pixels and determines which one has the smallest
    color distance to the average RGB values of all pixels in the list. It is useful
    for finding the most "representative" pixel in a set.

    Parameters:
        pixels (List[Pixel]): A list of Pixel objects to evaluate.

    Returns:
        Pixel: The pixel whose color is closest to the average color of the input list.
    """
    avg_rgb = get_average(pixels)
    avg_r = avg_rgb[0]
    avg_g = avg_rgb[1]
    avg_b = avg_rgb[2]

    min_dist = float('inf')
    best_pixel = None

    for pixel in pixels:
        distance = get_pixel_dist(pixel, avg_r, avg_g, avg_b)
        if distance < min_dist:
            min_dist = distance
            best_pixel = pixel
    return best_pixel

def solve(images):
    """
    Given a list of image objects, compute and display the solution image
    based on images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixels = []
            for img in images:
                pixel = img.get_pixel(x,y)
                pixels.append(pixel)
            best_pixel = get_best_pixel(pixels)

            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue


    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
