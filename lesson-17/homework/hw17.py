#1
import sqlite3
import pandas as pd
db_connection = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", db_connection)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", db_connection)
db_connection.close()
merged_df = pd.merge(customers_df, invoices_df, on="CustomerId", how="inner")
total_invoices_per_customer = merged_df.groupby("CustomerId")["InvoiceId"].count()
print(total_invoices_per_customer)
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
movie_df = pd.read_csv("movie.csv")
director_color_df = movie_df[["director_name", "color"]]
director_reviews_df = movie_df[["director_name", "num_critic_for_reviews"]]
left_join_df = pd.merge(director_color_df, director_reviews_df, on="director_name", how="left")
print("Rows in left join:", len(left_join_df))
outer_join_df = pd.merge(director_color_df, director_reviews_df, on="director_name", how="outer")
print("Rows in full outer join:", len(outer_join_df))

#2
import sqlite3
import pandas as pd
db_connection = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", db_connection)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", db_connection)
db_connection.close()
merged_df = pd.merge(customers_df, invoices_df, on="CustomerId", how="inner")
total_invoices_per_customer = merged_df.groupby("CustomerId")["InvoiceId"].count()
print(total_invoices_per_customer)
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
movie_df = pd.read_csv("movie.csv")
director_color_df = movie_df[["director_name", "color"]]
director_reviews_df = movie_df[["director_name", "num_critic_for_reviews"]]
left_join_df = pd.merge(director_color_df, director_reviews_df, on="director_name", how="left")
print("Rows in left join:", len(left_join_df))
outer_join_df = pd.merge(director_color_df, director_reviews_df, on="director_name", how="outer")
print("Rows in full outer join:", len(outer_join_df))

