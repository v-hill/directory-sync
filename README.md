# directory-sync
A collection of tools for analysing changes in file system structure.


### directory_to_json.py

This script takes in the filepath of a folder and saves a json file representation of the current contents and structure of the folder.


### json_pretty_print.py

This allows the contents of a json representation of the file structure to be printed out in a readable format.

For example:

```
├── Folder A
│   ├── gamma.txt
│   └── Inside folder
│       ├── alpha.txt
│       └── beta.txt
├── Folder B
│   ├── delta.txt
│   └── epsilon.txt
└── zeta.txt
```
