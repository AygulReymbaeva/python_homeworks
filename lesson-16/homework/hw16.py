#q1
import sqlite3
import pandas as pd
db_connection = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", db_connection)
print(customers_df.head(10)) 
db_connection.close()
iris_df = pd.read_json("iris.json")
print("Shape of iris dataset:", iris_df.shape)
print("Column names:", iris_df.columns.tolist())
titanic_df = pd.read_excel("titanic.xlsx")
print(titanic_df.head())  
flights_df = pd.read_parquet("flights.parquet")
print(flights_df.info())  
movie_df = pd.read_csv("movie.csv")
print(movie_df.sample(10))  

#q2
import sqlite3
import pandas as pd
db_connection = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", db_connection)
print(customers_df.head(10))  
db_connection.close()
iris_df = pd.read_json("iris.json")
iris_df.columns = iris_df.columns.str.lower()  
selected_iris_df = iris_df[["sepal_length", "sepal_width"]]  
print(selected_iris_df.head())
titanic_df = pd.read_excel("titanic.xlsx")
filtered_titanic_df = titanic_df[titanic_df["Age"] > 30]  
print(filtered_titanic_df.head())
print(titanic_df["Sex"].value_counts()) 
flights_df = pd.read_parquet("flights.parquet")
print(flights_df[["origin", "dest", "carrier"]].head())  
print("Number of unique destinations:", flights_df["dest"].nunique())
movie_df = pd.read_csv("movie.csv")
filtered_movie_df = movie_df[movie_df["duration"] > 120]  
sorted_movie_df = filtered_movie_df.sort_values(by="director_facebook_likes", ascending=False)  
print(sorted_movie_df.head())

#q3
import sqlite3
import pandas as pd
db_connection = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", db_connection)
print(customers_df.head(10)) 
db_connection.close()
iris_df = pd.read_json("iris.json")
iris_df.columns = iris_df.columns.str.lower()  
selected_iris_df = iris_df[["sepal_length", "sepal_width"]]  
print(selected_iris_df.head())
print("Mean values:")
print(iris_df.mean())
print("Median values:")
print(iris_df.median())
print("Standard deviation values:")
print(iris_df.std())
titanic_df = pd.read_excel("titanic.xlsx")
filtered_titanic_df = titanic_df[titanic_df["Age"] > 30]  
print(filtered_titanic_df.head())
print(titanic_df["Sex"].value_counts()) 
print("Minimum age:", titanic_df["Age"].min())
print("Maximum age:", titanic_df["Age"].max())
print("Sum of ages:", titanic_df["Age"].sum())
flights_df = pd.read_parquet("flights.parquet")
print(flights_df[["origin", "dest", "carrier"]].head())  
print("Number of unique destinations:", flights_df["dest"].nunique())
print("Missing values:")
print(flights_df.isnull().sum())
num_cols = flights_df.select_dtypes(include=['number']).columns
for col in num_cols:
    flights_df[col].fillna(flights_df[col].mean(), inplace=True)
movie_df = pd.read_csv("movie.csv")
filtered_movie_df = movie_df[movie_df["duration"] > 120]  
sorted_movie_df = filtered_movie_df.sort_values(by="director_facebook_likes", ascending=False)  
print(sorted_movie_df.head())
top_director = movie_df.groupby("director_name")["director_facebook_likes"].sum().idxmax()
print("Director with highest total Facebook likes:", top_director)
longest_movies = movie_df.nlargest(5, "duration")[["title", "director_name", "duration"]]
print("5 longest movies and their directors:")
print(longest_movies)
