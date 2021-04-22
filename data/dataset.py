import numpy as np
import re
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import json, plotly
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from subprocess import check_output
import os

category = pd.read_json('../input/youtube-new/IN_category_id.json')

data = pd.read_csv("../input/youtube-new/INvideos.csv", index_col = 'video_id')

data.head()
