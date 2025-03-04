#task1
import requests
API_KEY = "YOUR_API_KEY"
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Not available {response.status_code}")
#task2
import requests
import random
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.themoviedb.org/3"
def get_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("Not available")
        return {}
def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Not available")
        return []
def main():
    genres = get_genres()
    if not genres:
        return
    print("Available genres:")
    for genre in genres:
        print(f"- {genre.title()}")
    user_genre = input("\nEnter a movie genre from the list above: ").lower()
    if user_genre in genres:
        genre_id = genres[user_genre]
        movies = get_movies_by_genre(genre_id)
        if movies:
            random_movie = random.choice(movies)
            print(f"\n Movie Recommendation: {random_movie['title']}")
            print(f"Overview: {random_movie['overview']}")
            print(f"Rating: {random_movie['vote_average']} / 10")
        else:
            print("We could not find movies in this genre")
    else:
        print("Not available")
if __name__ == "__main__":
    main()
