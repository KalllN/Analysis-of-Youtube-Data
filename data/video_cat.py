id_video = []

video_name = []
for index, row in category.iterrows():
    x = row['items']
    
    id_video.append(x['id'])
    
    video_name.append(x['snippet']['title'])

category = pd.DataFrame(zip(id_video, video_name),columns=['category_id', 'category'])

category['category_id'] = category['category_id'].astype('int64')

#Instead of maintaining two different datasets, I merged both into one by adding categories into the original 'data' dataset.
data = pd.merge(data, category, on = 'category_id', how = 'inner')
