"""
File: babynames.py
Name: Cindy
--------------------------
This program is part of the SC101 Baby Names Project.

It is adapted from Nick Parlante's Baby Names assignment
and has been modified by Jerry Liao to align with the
learning objectives of the stanCode SC101 course.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name not in name_data:
        name_data[name] = {}

    year_dict = name_data[name]

    if year not in year_dict:
        year_dict[year] = rank  # If a new year comes, save it
    else:
        old_rank = int(year_dict[year])
        new_rank = int(rank)
        if new_rank < old_rank:
            year_dict[year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    with open(filename, 'r') as f:
        year = f.readline().strip()  # remove extra space or line break
        for line in f:
            parts = line.split(',')  # output: separate line by using ,; then it would be rank, name1, name2
            if len(parts) == 3:  # Ensure every part has complete data
                rank = parts[0].strip()
                name1 = parts[1].strip()
                name2 = parts[2].strip()
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containingby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}  # store all data to dict as it is Key-Value Pairs, i.e. {'Amy': rank}
    for filename in filenames:
        add_file(name_data, filename)  # add filename to name_data dict
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data
 ba
    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_names = []
    target_lower = target.lower()  # Convert the searched data to lower case
    for name in name_data:  # Search the name (key)
        if target_lower in name.lower():
            matching_names.append(name)  # if the name matches the target_lower, add the name (original format) to list
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
