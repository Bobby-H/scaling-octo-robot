destinations = ["Paris, France",
                "Shanghai, China",
                "Los Angeles, USA",
                "Sao Paulo, Brazil",
                "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ['historical site', 'art']]

attractions = [[] for destination in destinations]


def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_the_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

print(attractions)
