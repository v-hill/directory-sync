import argparse
import json
import os
from datetime import datetime
from pathlib import Path


def to_tree(p):
    """
    Takes in the string representation of a windows file path and returns a
    nested dictionary representation of the file/folder structure.

    Parameters
    ----------
    p : str
        Directory path.

    Returns
    -------
    dict
        Dictionary of input directory structure.
    """
    dir_tree = []
    for i in os.listdir(p):
        if os.path.isfile(f'{p}/{i}'):
            dir_tree.append({'name': i})
        else:
            dir_tree.append({'name': i, 'children': to_tree(f'{p}/{i}')})
    return dir_tree


prefix_components = {'prefix': '',
                     'space': '    ',
                     'branch': '│   ',
                     'tee': '├── ',
                     'last': '└── '}


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path)
    p = parser.parse_args()

    # Create filename out output json file
    str_now = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    out_file = p.file_path.__str__().split(":")[1][1:].replace("\\", "_")
    out_file = out_file.replace("\\", "__").replace(" ", "_")
    out_file = f'{out_file}_{str_now}.json'

    # Create directory tree dict
    dir_tree = to_tree(str(p.file_path))

    # Export to json format
    with open(out_file, 'w') as f:
        json.dump(dir_tree, f, indent=4, sort_keys=True)
