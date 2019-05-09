import numpy as np
import pandas as pd
from pathlib import Path
import os
from fastai.vision import *
from prepare_data import *

path = Path(r'E:\paintings dataset\wikiart')
basepath, fname = os.path.split(path)

for c in data.classes:
    print(c)
    verify_images(path/'train'/c, delete=True, max_workers = 0)



#for c in classes:
#     print(c)
#     verify_images(path/c, delete=True, max_workers=8)
