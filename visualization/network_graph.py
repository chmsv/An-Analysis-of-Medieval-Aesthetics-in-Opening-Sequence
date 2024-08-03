import json
import codecs

# Prepare nodes and links from the JSON-LD data
# Load the JSON-LD file
file_path = './Medieval_Movies.jsonld'

with open(file_path, 'r') as file:
    data = json.load(file)

# Extract nodes and links
nodes = []
links = []

node_set = set()

# Add movies as nodes and create links
for movie in data["@graph"]:
    movie_node = {"id": movie["name"], "group": "movie"}
    nodes.append(movie_node)
    node_set.add(movie_node["id"])

    # Add director node and link
    if "director" in movie:
        for director in movie["director"]:
            director_node = {"id": director["name"], "group": "director"}
            if director_node["id"] not in node_set:
                nodes.append(director_node)
                node_set.add(director_node["id"])
            links.append({"source": movie["name"], "target": director["name"]})

    # Add production company node and link
    if "productionCompany" in movie:
        for company in movie["productionCompany"]:
            company_node = {"id": company["name"], "group": "productionCompany"}
            if company_node["id"] not in node_set:
                nodes.append(company_node)
                node_set.add(company_node["id"])
            links.append({"source": movie["name"], "target": company["name"]})

    # Add genre nodes and links
    if "genre" in movie:
        for genre in movie["genre"]:
            genre_node = {"id": genre, "group": "genre"}
            if genre_node["id"] not in node_set:
                nodes.append(genre_node)
                node_set.add(genre_node["id"])
            links.append({"source": movie["name"], "target": genre})

data = {"nodes": nodes, "links": links}

# Convert data to JSON format
data_json = json.dumps(data, indent=2, ensure_ascii=False)

# Print data to check (optional)
print(data_json)

# Save to a JSON file
output_path = './data_network_graph.json'
with codecs.open(output_path, 'w', encoding='utf-8') as f:
    f.write(data_json)
