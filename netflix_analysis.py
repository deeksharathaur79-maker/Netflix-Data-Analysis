import pandas as pd
df= pd.read_csv("netflix_titles.csv")
print("Dataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDataset Info:")
print(df.info())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("netflix_titles.csv")
print(df["type"].value_counts())
sns.countplot(data=df,x="type")
plt.title("Movies vs TV Shows")
plt.show()
movies=df.dropna(subset=["imdb_score"])
top_movies=movies.sort_values(
    by="imdb_score",
    ascending=False
).head(10)
print(top_movies[["title","imdb_score"]])
plt.figure(figsize=(10,6))
sns.barplot(
    data=top_movies,
    x="imdb_score",
    y="title"
)
genres=df['listed_in'].str.split('\
').explode()
top_genres=genres.value_counts().head(10)
top_genres.plot(kind='barh')
plt.title('Top 10 Genres on Netflix')
plt.show()
''
