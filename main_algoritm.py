import osmnx as ox
import networkx as nx


ox.config(log_console=True, use_cache=True)

start_latlng = (58.59886, 49.66779)
end_latlng = (58.555152, 49.64137)

place = 'Kirov,Kirov Oblast,Volga Federal District,Russia'
mode = 'drive'
optimizer = 'time'

graph = ox.graph_from_place(place, network_type = mode)
# найдите ближайший узел к начальному местоположению
orig_node = ox.nearest_nodes(graph, 49.66779, 58.59886)
# найдите ближайший узел к конечному местоположению
dest_node = ox.nearest_nodes(graph, 49.64137, 58.555152)
# найти кратчайший путь
shortest_route = nx.shortest_path(graph, orig_node, dest_node,
                                  weight=optimizer)
shortest_route_map = ox.plot_route_folium(graph, shortest_route,
                                          tiles='openstreetmap')
shortest_route_map.save('map.html')
