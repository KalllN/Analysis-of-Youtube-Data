import numpy as np
import re
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import json, plotly
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from subprocess import check_output

channel = data.groupby("channel_title").size().reset_index(name="video_count")\
.sort_values("video_count", 
             ascending = False).head(30)

fig, ax = plt.subplots(figsize = (8, 8))

pb = sns.barplot(x = "video_count", 
                 y = "channel_title", data = channel,
                palette = sns.cubehelix_palette(start = .2, 
                                                rot = -.3, n_colors = 30, 
                                 reverse = True), ax = ax)

pb = ax.set(xlabel = "No. of videos", ylabel = "Channel")


matplotlib.pyplot.figure(figsize = (8, 6))
sns.scatterplot(x = data['views'], 
                y = data['likes'], color = 'gold')

f, ax = plt.subplots(figsize = (8, 10))

corr = data[column_correlation].corr()

sns.heatmap(corr, 
            mask = np.zeros_like(corr, dtype = np.bool), 
            cmap = "Spectral",
            square = True, ax = ax, 
            annot = True)

data1 = data.groupby(['category','channel_title']).size().rename('num_videos').reset_index()
data2 = data1[data1.groupby('category')['num_videos'].transform(max) == data1['num_videos']]
px.bar(data_frame = data2,x='channel_title', y='num_videos',template='ggplot2')


fig = sns.barplot(data = data2, x = 'channel_title', 
                  y = 'num_videos')
xlabels = (data2['category'] + ' / ' + 
           data2['channel_title']).to_list()
_ = plt.title('Channels with Highest no.of trending videos in each category', 
              fontsize = 20)
_ = plt.ylabel('Number of Videos', 
               fontsize = 10)
_ = plt.xlabel('')
_ = plt.xticks(np.arange(0, 16),
               xlabels, rotation = 90, 
               fontsize = 10)

data3 = data.groupby(['category']).agg({'views':'sum','likes':'sum','dislikes':'sum','comment_count':'sum'}).reset_index()
data31 = [go.Pie(labels = data3['category'], 
                 values = data3['views'], 
                 hoverinfo = 'label')]
plotly.offline.iplot(data31, 
                     filename = 'category')
