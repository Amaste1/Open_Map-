import osmnx as ox
import networkx as nx

ox.config(log_console=True, use_cache=True)

# define the start and end locations in latlng
start_latlng = (358.59354,-49.65522)
end_latlng = (58.59886, 49.66779)

# location where you want to find your route
place = 'Kirov, Russia'

# find shortest route based on the mode of travel
mode = 'walk' # 'drive', 'bike', 'walk'

# find shortest path based on distance or time
optimizer = 'time' # 'length','time'

# create graph from OSM within the boundaries of some
# geocodable place(s)
graph = ox.graph_from_place(place, network_type = mode)

# find the nearest node to the start location
orig_node = ox.get_nearest_node(graph, start_latlng)

# find the nearest node to the end location
dest_node = ox.get_nearest_node(graph, end_latlng)

# find the shortest path
shortest_route = nx.shortest_path(graph, orig_node,dest_node,
                                  weight=optimizer)