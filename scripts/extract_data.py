import numpy as np
import pandas as pd
import requests
import json
from pathlib import Path
import os

#Extract the datatset pictures
path = r'E:\paintings dataset\wikiart.zip'
basepath, fname = os.path.split(path)

import zipfile
zip_ref = zipfile.ZipFile(path, 'r')

try:
    zip_ref.extractall(basepath)

except zipfile.BadZipFile:
    print('useless image')    
    
zip_ref.close()



