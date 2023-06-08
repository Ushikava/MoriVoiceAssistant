import pandas as pd
import numpy as np

anime_comments = pd.read_csv("entertainment_anime.csv", names=['num', 'id', 'text', 'uid', 'subreddit', 'meta', 'time', 'author', 'ups', 'downs', 'authorlinkkarma', 'authorcommentkarma' ,'authorisgold'])
print(anime_comments)

comments_np = np.array(anime_comments['text'])
print(comments_np)
f = open("comments_in_txt.txt", "w")
for comment in comments_np:
    f.writelines(str(comment) + '\n')