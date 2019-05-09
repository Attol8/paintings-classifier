import numpy as np
import pandas as pd
import json
from pathlib import Path
import os
from fastai.vision import *
import split_folders

path = Path(r'E:\paintings-dataset\wikiart\train')
output_path = Path(r'E:\paintings-dataset')

split_folders.fixed(path, output=output_path, fixed=(100, 20), oversample=False) # default values

# for dir_class in split_folders.list_dirs(path):
#     print(len(split_folders.list_files(dir_class)))

ImageList