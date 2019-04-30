#import libraries
import pandas as pd
import requests
import json
from pathlib import Path 
import numpy as np

api_key = 'xbXXa4oQZ'

paintings = []

def search_europeana(painter):
  
  wskey = str('wskey=') + api_key
  query= str('query=') + 'who:' + painter
  qf = str('qf=') + 'what:"painting"'
  
  reusability = str('reusability=') + 'open+AND+permission+AND+restricted'
  media = 'True'
  profile= str('profile=') + 'standard'
  rows = str('rows=') + '50'
  r = requests.get('https://www.europeana.eu/api/v2/search.json?'+ wskey + '&'+ query + '&' + qf + '&' + reusability+ '&' + media + '&' + profile + '&' +rows)
  data = r.json()
  
  #print title, score, concept (or 'type':painting), URL

  for item in data['items']:
    edmConceptPrefLabelLangAware_dict = item.get('edmConceptPrefLabelLangAware', {})
    paintings.append([item['title'], item['score'], edmConceptPrefLabelLangAware_dict.get('en', 'n/a') , item.get('edmIsShownAt', 'n/a'), item['edmPreview']])
    
  return paintings  

#Create a numpy array

def get_array(painter):
  '''
  Perform a search in the europeana app for the specified painter
  Returns a numpy array of paintings
  '''
  paintings = search_europeana(painter)
  array = np.array(paintings)
  return array

def download_csv(painter):

  paintings = search_europeana(painter)
  array = get_array(painter)
  df = pd.DataFrame(array, columns=['title', 'score', 'concept', 'ShownAT', 'ImageURL'])
  export_folder = Path(r"C:\Users\Jacopo\Desktop\Programming\Festina Lente\data")
  csv_to_write = export_folder/"paintings.csv"
  df.to_csv(csv_to_write, index = None, header=True)
  

if (__name__ == '__main__'):
    print('Executing as standalone script')
    download_csv(painter)




