import json
import csv

# Load the JSON-LD file
file_path = './Medieval_Movies.jsonld'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract 'datePublished', 'name', and 'image' (image URLs) from each movie object
movies = []
for movie in data["@graph"]:
    if movie["@type"] == "Movie":
        movies.append({
            "name": movie["name"],
            "datePublished": movie["datePublished"],
            "image": movie.get("image", "")
        })

# Save the data to a CSV file
csv_file_path = './timeline2.csv'
with open(csv_file_path, 'w') as csvfile:
    fieldnames = ['name', 'datePublished', 'image']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for movie in movies:
        writer.writerow({k: (v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in movie.items()})
