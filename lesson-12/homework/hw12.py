#task1 
from bs4 import BeautifulSoup
with open("weather.html", "r", encoding="utf-8") as file:
    content = file.read()
soup = BeautifulSoup(content, "html.parser")
weather_data = []
for row in soup.find_all("tr")[1:]:  
    columns = row.find_all("td")
    day = columns[0].text.strip()
    temp = int(columns[1].text.strip().replace("°C", ""))  
    condition = columns[2].text.strip()
    weather_data.append((day, temp, condition))
print("Weather Forecast:")
for day, temp, condition in weather_data:
    print(f"{day}: {temp}°C, {condition}")
max_temp_day = max(weather_data, key=lambda x: x[1])
print(f"\nHottest Day: {max_temp_day[0]} with {max_temp_day[1]}°C")
sunny_days = [day for day, temp, condition in weather_data if condition == "Sunny"]
print("\nSunny Days:", ", ".join(sunny_days))
average_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)
print(f"\nAverage Temperature: {average_temp:.2f}°C")

#task2
import requests
import sqlite3
import csv
from bs4 import BeautifulSoup
def setup_database():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(job_title, company, location)
        )
    ''')
    conn.commit()
    conn.close()
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    job_cards = soup.find_all("div", class_="card-content")
    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="description").text.strip()
        application_link = job.find("a")['href']
        jobs.append((title, company, location, description, application_link))
    return jobs
def store_jobs(jobs):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    for job in jobs:
        cursor.execute('''
            INSERT INTO jobs (job_title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(job_title, company, location) DO UPDATE SET
                description = excluded.description,
                application_link = excluded.application_link
        ''', job)
    conn.commit()
    conn.close()
def export_jobs(filter_by=None, value=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    query = "SELECT job_title, company, location, description, application_link FROM jobs"
    params = ()
    if filter_by and value:
        query += f" WHERE {filter_by} = ?"
        params = (value,)
    cursor.execute(query, params)
    jobs = cursor.fetchall()
    conn.close()
    with open("filtered_jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)
    print("Filtered jobs exported to filtered_jobs.csv")
if __name__ == "__main__":
    setup_database()
    job_listings = scrape_jobs()
    store_jobs(job_listings)
    print("Jobs successfully scraped and stored in the database.")

#task3
import requests
import json
from bs4 import BeautifulSoup
def scrape_laptops():
    base_url = "https://www.demoblaze.com"
    laptops_url = base_url + "/index.html#"
    laptops = []
    while True:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("div", class_="card-block")
        for product in products:
            name = product.find("h4", class_="card-title").text.strip()
            price = product.find("h5").text.strip()
            description = product.find("p", class_="card-text").text.strip()
            laptops.append({
                "name": name,
                "price": price,
                "description": description
            })
        next_button = soup.find("button", id="next2")
        if not next_button or "disabled" in next_button.attrs:
            break  
    return laptops
def save_to_json(data, filename="laptops.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")
if __name__ == "__main__":
    laptops_data = scrape_laptops()
    save_to_json(laptops_data)
