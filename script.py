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
    attractions_for_destination = destination_index[destination_index].append(attraction)
  except SyntaxError:
    return

test_destination_index = get_traveler_location(test_traveler)
print(attractions)
