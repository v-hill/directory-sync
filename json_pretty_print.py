import argparse
import json
from pathlib import Path


def tree_from_json(dir_tree, prefix_dict, prefix=''):
    """
    Function to recursivly traverse the directory specified by the 'dir_tree'
    dictionary and yield a tree structure print out.

    Parameters
    ----------
    dir_tree : dict
        Dictionary representation of a file/folder.
    prefix_dict : dict
        Dictionary of strings for formatting the tree structure print out.
    prefix : str, optional
        Current prefix. The default is ''.

    Yields
    ------
    str
        A single line of the directory structure.
    """
    if isinstance(dir_tree, list):
        pointers = [prefix_dict['tee']] * \
            (len(dir_tree) - 1) + [prefix_dict['last']]
        for pointer, path in zip(pointers, dir_tree):
            yield prefix + pointer + path['name']
            if 'children' in path:
                if pointer == prefix_dict['tee']:
                    extension = prefix_dict['branch']
                else:
                    extension = prefix_dict['space']
                yield from tree_from_json(path,
                                          prefix_dict,
                                          prefix=prefix + extension)
    elif 'children' in dir_tree:
        pointers = [prefix_dict['tee']] * \
            (len(dir_tree['children']) - 1) + [prefix_dict['last']]
        for pointer, path in zip(pointers, dir_tree['children']):
            yield prefix + pointer + path['name']
            if 'children' in path:
                if pointer == prefix_dict['tee']:
                    extension = prefix_dict['branch']
                else:
                    extension = prefix_dict['space']
                yield from tree_from_json(path['children'],
                                          prefix_dict,
                                          prefix=prefix + extension)
    else:
        pointer = prefix_dict['last']
        path = dir_tree
        yield prefix + pointer + path['name']


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

    # Load existing database
    with open(p.file_path) as f:
        dir_tree = json.load(f)

    for line in tree_from_json(dir_tree, prefix_components):
        print(line)
