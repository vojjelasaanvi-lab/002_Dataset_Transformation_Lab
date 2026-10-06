import pandas as pd
import numpy as np
df=pd.read_csv("day02_usage.csv")
print(df.head())
Day = df["Day"].to_numpy();
Chat = df["Chat"].to_numpy();
Video = df["Video"].to_numpy();
Study = df["Study"].to_numpy();
Games = df["Games"].to_numpy();
print(Day.shape)
print(Chat.shape)
print(Video.shape)
print(Study.shape)
print(Games.shape)

print(Day.sum())
print(Chat.sum())
print(Video.sum())
print(Study.sum())
print(Games.sum())

print("Day: ",round(Day.mean(),1))
print("Chat:",round(Chat.mean(),1))
print("Video:",round(Video.mean(),1))
print("Study:",round(Study.mean(),1))
print("Games:",round(Games.mean(),1))

diff = Study-Games
print(diff)


print(f"Best day for study vs games :,{int(diff.argmax())+1} with  a balance of {diff.max()} minutes")

