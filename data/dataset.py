import pandas as pd
import os

category = pd.read_json('../input/youtube-new/IN_category_id.json')

data = pd.read_csv("../input/youtube-new/INvideos.csv", index_col = 'video_id')
