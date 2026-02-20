"""
File: babygraphics.py
Name: Cindy
--------------------------------
This program is part of the SC101 Baby Names Project.

It is adapted from Nick Parlante's Baby Names assignment
and has been modified by Jerry Liao to align with the
learning objectives of the stanCode SC101 course.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, this function returns the x coordinate
    of the vertical line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    total_space = width - 2 * GRAPH_MARGIN_SIZE
    step = total_space / len(YEARS)  # The gap between each year
    return GRAPH_MARGIN_SIZE + year_index * step


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # Bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)  # Get x value
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)  # Create line
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for i in range(len(lookup_names)):
        name = lookup_names[i]  # Search every name
        color_index = i % len(COLORS)
        color = COLORS[color_index]

        for j in range(len(YEARS)):
            year =str(YEARS[j])
            x_current = get_x_coordinate(CANVAS_WIDTH, j)
            y_current = 0
            rank_current = ""
            if year in name_data[name]:
                rank_current = name_data[name][year]  # Get the name and ranking
                rank_val = int(rank_current)
                if rank_val <= MAX_RANK:
                    y_ratio = rank_val / MAX_RANK
                    drawable_height = CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE
                    y_current = GRAPH_MARGIN_SIZE + (y_ratio * drawable_height)
                else:
                    y_current = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    rank_current = "*"
            else:
                y_current = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                rank_current = "*"

            canvas.create_text(x_current + TEXT_DX, y_current, text=f"{name}{rank_current}", anchor = tkinter.SW, fill=color)

            if j < len(YEARS) - 1:
                next_year = str(YEARS[j + 1])
                x_next = get_x_coordinate(CANVAS_WIDTH, j + 1)
                y_next = 0

                if next_year in name_data[name]:
                    rank_next_val = int(name_data[name][next_year])
                    if rank_next_val <= MAX_RANK:
                        y_ratio = rank_next_val / MAX_RANK
                        drawable_height = CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE
                        y_next = GRAPH_MARGIN_SIZE + (y_ratio * drawable_height)
                    else:
                        y_next = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    y_next = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_line(x_current, y_current, x_next, y_next, width=LINE_WIDTH, fill=color)



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data

    top.mainloop()


if __name__ == '__main__':
    main()
