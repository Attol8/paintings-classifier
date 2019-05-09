import numpy as np
import pandas as pd
import json
from pathlib import Path
import os
from fastai.vision import *
import split_folders
from shutil import copyfile

#set path for dataset
path = r'E:\paintings-dataset\wikiart'
basepath, fname = os.path.split(path)

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
# os.chdir(path)
# split_folders.ratio(path, output="output", seed=1337, ratio=(.8, .1, .1)) # default values

#datablock API
tfms = get_transforms(flip_vert=True, max_lighting=0.1, max_zoom=1.05, max_warp=0.)
np.random.seed(42)
size = 128

src = (ImageList.from_folder(path, recurse=True)
       .split_by_folder()
       .label_from_folder())


data = (src.transform(tfms, size=size)
       .databunch(no_check=True, num_workers=0).normalize(imagenet_stats))

def create_df(src):
       items = []
       for i in src.items:
              items.append(i)
       df = pd.DataFrame(items)  
       return df      

def create_sample(df):
       df_sample = df.sample(n = 5000, random_state=1)
       return df_sample

def copy_to_sample(df_sample, dst):

       for i in df_sample[0]:
              shutil.copy(i, dst)

